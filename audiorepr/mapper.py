class BaseMapper:
    def __init__(
        self, pitch_min=None, pitch_max=None, data_min=None, data_max=None, **params
    ):
        self.name = "basemapper"
        if pitch_min is None:
            self.pitch_min = 16
        if pitch_max is None:
            self.pitch_max = 96

        self.data_min = data_min
        self.data_max = data_max

    def _mapper(self, data, **params):

        raise NotImplementedError("Please implement this method")

    def map(self, data, **params):

        return self._mapper(data, **params)


class LinearMinMaxMapper(BaseMapper):
    def __init__(
        self, pitch_min=None, pitch_max=None, data_min=None, data_max=None, **params
    ):
        super().__init__(
            pitch_min=pitch_min,
            pitch_max=pitch_max,
            data_min=data_min,
            data_max=data_max,
            **params
        )
        self.name = "LinearMinMaxMapper"

    def _transformed_pitch(self, x, data_max, data_min):

        return int(
            self.pitch_min
            + (x - data_min) * (self.pitch_max - self.pitch_min) / (data_max - data_min)
        )

    def _mapper(self, data, **params):

        data_min = params.get("data_min", self.data_min)
        data_max = params.get("data_max", self.data_max)

        if data_min is None:
            data_min = min(data)
        if data_max is None:
            data_max = max(data)

        res = [self._transformed_pitch(i, data_max, data_min) for i in data]

        return res
