class BaseMapper:
    def __init__(self, pitch_min=None, pitch_max=None, **params):
        self.name = "basemapper"
        if pitch_min is None:
            self.pitch_min = 16
        if pitch_max is None:
            self.pitch_max = 96

    def _mapper(self, data):

        raise NotImplementedError("Please implement this method")

    def map(self, data):

        return self._mapper(data)


class LinearMinMaxMapper(BaseMapper):
    def __init__(self, pitch_min=None, pitch_max=None, **params):
        super().__init__(pitch_min=pitch_min, pitch_max=pitch_max, **params)
        self.name = "LinearMinMaxMapper"

    def _mapper(self, data):
        data_min = min(data)
        data_max = max(data)

        res = [self.pitch_min + int(i/(data_max - data_min)) for i in data]

        return res
