from typing import Any

import org.slf4j.event
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object

class Level(Object):
    @staticmethod
    def convertAnSLF4JLevel(slf4jLevel: org.slf4j.event.Level) -> Level: ...
    @staticmethod
    def fromLocationAwareLoggerInteger(levelInt: int) -> Level: ...
    def isGreaterOrEqual(self, r: Level) -> bool: ...
    def toInt(self) -> int: ...
    def toInteger(self) -> int: ...
    @staticmethod
    def toLevel(*args: Any) -> Level: ...
    @staticmethod
    def toLocationAwareLoggerInteger(level: Level) -> int: ...
    @staticmethod
    def valueOf(sArg: AnyStr) -> Level: ...