import numpy as np
import pandas as pd
from loguru import logger


def shape_validator(data):
    """
    shape_validator validates the shape of the input data

    :param data: numpy array to be validated
    :type data: np.ndarray
    """

    shape = data.shape

    if len(shape) > 2:
        raise ValueError(f"input data:\n{data}\nshould have rank 1 or 2.")
    elif len(shape) == 2 and shape[-1] > 12:
        raise ValueError(
            f"input data:\n{data}\nshould have less or equal to 12 columns."
        )
    elif len(shape) == 1:
        data = data.reshape(len(data), 1)

    return data.shape


def data_standardize(data):
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
        raise TypeError(
            f"Input data\n {data} \nshould be one of the following: DataFrame, Series, ndarray, list, tuple"
        )

    shape = shape_validator(data)
    n_tracks = shape[-1]

    res = {"n_tracks": n_tracks, "pitches": np.transpose(data)}
    logger.debug(f"number of tracks: {n_tracks}")

    return res
