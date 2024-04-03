import numpy as np


class Point:
    def __init__(self, long, lat):
        try:
            int(long)
            int(lat)
        except TypeError:
            raise TypeError("make sure long and lat are numbers")

        self._long = long
        self._lat = lat

    def __eq__(self, other):
        return self._long == other.long and self._lat == other.lat

    def __hash__(self):
        return hash((self._long, self._lat))

    def __getitem__(self, index):
        return self.coords()[index]

    def __len__(self):
        return 2

    def coords(self):
        return (self._long, self._lat)

    def distance(self, other):
        try:
            len(other)
            long = np.array(list(map(lambda x: x.long, other)))
            lat = np.array(list(map(lambda x: x.lat, other)))
            return np.sqrt(abs(self._long - long)**2 +
                           abs(self._lat - lat)**2)
        except TypeError:
            return np.sqrt(abs(self._long - other.long)**2 +
                           abs(self._lat - other.lat)**2)

    def update_pos(self, pos):
        assert type(pos) == Point

        self._long, self._lat = pos.coords()

    @property
    def long(self):
        return self._long

    @property
    def lat(self):
        return self._lat

    def __str__(self):
        return f"({self._long}, {self._lat})"

    def __repr__(self):
        return f"({self._long}, {self._lat})"
