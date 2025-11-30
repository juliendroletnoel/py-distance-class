class Distance (object):

    def __init__(self, km: float) -> None:
        self.km = km

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers"

    def __add_(self, distance: object) -> object:
        if isinstance(distance, (int, float)):
            return Distance(self.km + distance)

        return Distance(self.km + distance.km)

    def __iadd__(self, distance: int) -> None:
        if isinstance(distance, (int, float)):
            self.km = self.km + distance
        else:
            self.km = self.km + distance.km

    def __mul__(self, multiplicator: int) -> object:
        return Distance(self.km * multiplicator)

    def __truediv__(self, divisor: int) -> object:
        return Distance(round(self.km / divisor, 2))

    def __lt__(self, distance: object) -> bool:
        if isinstance(distance, (int, float)):
            return self.km < distance
        return self.km < distance.km

    def __le__(self, distance: object) -> bool:
        if isinstance(distance, (int, float)):
            return self.km <= distance
        return self.km <= distance.km

    def __eq__(self, distance: object) -> bool:
        if isinstance(distance, (int, float)):
            return self.km == distance
        return self.km == distance.km

    def __ge__(self, distance: object) -> bool:
        if isinstance(distance, (int, float)):
            return self.km >= distance
        return self.km >= distance.km

    def __gt__(self, distance: object) -> bool:
        if isinstance(distance, (int, float)):
            return self.km > distance
        return self.km > distance.km
