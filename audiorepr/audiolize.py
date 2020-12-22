from midiutil import MIDIFile
import numpy as np
import pandas as pd


def _shape_validator(data):

    shape = data.shape

    if len(shape) > 2:
        raise ValueError(f"input data:\n{data}\nshould have rank 1 or 2.")
    elif len(shape) == 2 and shape[-1] > 12:
        raise ValueError(f"input data:\n{data}\nshould have less or equal to 12 columns.")
    elif len(shape) == 1:
        data = data.reshape(len(data),1)


def _data_standardize(data):
    """
    _data_standardize standardize data input

    :param data: Input data
    :type data: Union[pd.DataFrame, pd.Series, np.ndarray, list, tuple]
    """

    if isinstance(data, (pd.DataFrame, pd.Series)):
        data = data.to_numpy()
    elif isinstance(data, np.ndarray):
        data = data
    elif isinstance(data, (list, tuple)):
        data = np.array(data)
    else:
        raise TypeError(f"Input data\n {data} \nshould be one of the following: DataFrame, Series, ndarray, list, tuple")

    _shape_validator(data)

    return data


def audiolize(data, **params):

    data = _data_standardize(data)

    shape = data.shape

    if len(shape) == 2:
        n_tracks = shape[-1]
    else:
        n_tracks = 1

    degrees_list  = data

    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 2    # In beats
    tempo    = 100   # In BPM
    volume   = 127  # 0-127, as per the MIDI standard

    MyMIDI = MIDIFile(3)  # One track, defaults to format 1 (tempo track is created
                        # automatically)

    MyMIDI.addTrackName(track,time,"Sample Track")
    #MyMIDI.addTempo(track,time,360)

    MyMIDI.addTempo(track, time, tempo)

    for degrees in degrees_list:
        for i, pitch in enumerate(degrees):
            MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)

        track += 1

    #for degrees in degrees_list:
    #    for i, pitch in enumerate(degrees):
    #        MyMIDI.addNote(track, channel, pitch, time + i, duration, volume)
    #
    #    channel += 1


    with open("demo-music.mid", "wb") as output_file:
        MyMIDI.writeFile(output_file)
