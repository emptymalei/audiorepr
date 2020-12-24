import pandas as pd
from loguru import logger
from midiutil import MIDIFile

from .data import data_standardize as _pitch_data_standardize
from .data import shape_validator as _shape_validator
from .mapper import LinearMinMaxMapper


def build_track(pitches, midi_object, track, **params):
    """
    build_track builds the specified track for the midi object

    :param pitches: specified series of pitch for the track
    :type pitches: Union[pd.Series, np.ndarray, list, tuple]
    :param midi_object: instantiated midi object
    :param track: specified track id
    :type track: int
    """
    channel = params.get("channel", 0)
    duration = params.get("duration", 2)
    begin_beat = params.get("begin_beat", 0)  # In beats
    volume = params.get("volume", 127)  # 0-127, as per the MIDI standard

    for t, pitch in enumerate(pitches):
        midi_object.addNote(
            track, channel, pitch, begin_beat + t * duration, duration, volume
        )


def audiolizer(data, target, **params):
    """
    audiolize audiolizes the input data

    :param data: input tabular data to be audiolized
    :type data: Union[pd.DataFrame, pd.Series, ndarray, list, tuple]
    """
    midi_data = data.copy()

    # get params
    midi_object = params.get("midi_object")
    channel = params.get("channel", 0)
    begin_beat = params.get("begin_beat", 0)  # In beats
    duration = params.get("duration", 2)  # In beats
    tempo = params.get("tempo", 200)  # In BPM
    volume = params.get("volume", 127)  # 0-127, as per the MIDI standard

    # set mapper params
    mapper = params.get("mapper")
    pitch_min = params.get("pitch_min")
    pitch_max = params.get("pitch_max")

    # determine track names if the input data is a dataframe
    pitch_columns = params.get("pitch_columns")
    track_names = params.get("track_names")
    if isinstance(midi_data, pd.DataFrame):
        track_names = midi_data.columns.tolist()
        logger.debug(f"Track names:\n{track_names}")

    # standardize data
    if pitch_columns:
        pitch_raw_data = midi_data[pitch_columns]
    else:
        pitch_raw_data = midi_data.copy()
    pitch_raw_data = _pitch_data_standardize(pitch_raw_data)
    all_track_pitches = pitch_raw_data.get("pitches")
    n_tracks = pitch_raw_data.get("n_tracks")
    track_max = pitch_raw_data.get("max")
    track_min = pitch_raw_data.get("min")

    # instantiate midifile object
    if midi_object is None:
        midi_object = MIDIFile(n_tracks)

    if mapper is None:
        mapper = LinearMinMaxMapper(
            pitch_min=pitch_min,
            pitch_max=pitch_max,
            data_min=min(track_min),
            data_max=max(track_max),
        )

    for track in range(n_tracks):
        # add tempo
        midi_object.addTempo(track, 0, tempo)

        # add track names if track names are given
        if track_names:
            midi_object.addTrackName(track, 0, track_names[track])

    for track, pitches in enumerate(all_track_pitches):
        pitches = mapper.map(pitches)

        build_track(
            pitches,
            midi_object,
            track,
            channel=channel,
            duration=duration,
            begin_beat=begin_beat,
            volume=volume,
        )

    # export midi file
    with open(target, "wb") as output_file:
        midi_object.writeFile(output_file)
