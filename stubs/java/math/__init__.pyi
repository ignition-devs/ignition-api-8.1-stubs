from typing import List

from java.lang import Enum as Enum

class RoundingMode(Enum):
    CEILING: RoundingMode
    DOWN: RoundingMode
    FLOOR: RoundingMode
    HALF_DOWN: RoundingMode
    HALF_EVEN: RoundingMode
    HALF_UP: RoundingMode
    UNNECESSARY: RoundingMode
    UP: RoundingMode
    @staticmethod
    def values() -> List[RoundingMode]: ...
