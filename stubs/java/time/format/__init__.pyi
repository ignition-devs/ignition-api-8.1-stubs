from typing import List

from java.lang import Enum as Enum

class ResolverStyle(Enum):
    LENIENT: ResolverStyle
    SMART: ResolverStyle
    STRICT: ResolverStyle
    @staticmethod
    def values() -> List[ResolverStyle]: ...
