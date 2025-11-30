class Distance (object):

    def __init__(self, km: float) -> None:
        self.km = km

    def __repr__(self) -> None:
        print(f"Distance(km={self.km})")

    def __str__(self) -> None:
        print(f"Distance: {self.km} kilometers")

    def __add_(self, distance: object) -> object:
        return Distance(self.km + distance.km)

    def __iadd__(self, distance: int) -> object:
        return Distance(self.km + distance)

    def __mul__(self, multiplicator: int) -> object:
        return Distance(self.km * multiplicator)

    def __truediv__(self, divisor: int) -> object:
        return Distance(round(self.km / divisor), 2)

    def __lt__(self, distance: object) -> bool:
        return self.km < distance.km

    def __le__(self, distance: object) -> bool:
        return self.km <= distance.km

    def __eq__(self, distance: object) -> bool:
        return self.km == distance.km

    def __ge__(self, distance: object) -> bool:
        return self.km >= distance.km

    def __gt__(self, distance: object) -> bool:
        return self.km > distance.km
