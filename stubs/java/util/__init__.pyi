from typing import Optional

from java.lang import Object

class Date(Object):
    def __init__(self, date: Optional[long] = ...) -> None: ...
    def __cmp__(self, other: Date) -> bool: ...
    def __ge__(self, other: Date) -> bool: ...
    def __gt__(self, other: Date) -> bool: ...
    def __lt__(self, other: Date) -> bool: ...
    def after(self, when: Date) -> bool: ...
    def before(self, when: Date) -> bool: ...
    def compareTo(self, anotherDate: Date) -> int: ...
    def getTime(self) -> long: ...
    def setTime(self, time: long) -> None: ...

class EventObject(Object):
    source: Object
    def __init__(self, source: Object) -> None: ...
    def getSource(self): ...

class classproperty(property):
    def __get__(self, cls, owner): ...

class Locale(Object):
    country: Optional[str]
    language: str
    variant: Optional[str]
    def __init__(
        self, language: str, country: Optional[str] = ..., variant: Optional[str] = ...
    ) -> None: ...
    def CANADA(self): ...
    def CANADA_FRENCH(self): ...
    def CHINA(self): ...
    def CHINESE(self): ...
    def ENGLISH(self): ...
    def FRANCE(self): ...
    def FRENCH(self): ...
    def GERMAN(self): ...
    def GERMANY(self): ...
    def ITALIAN(self): ...
    def ITALY(self): ...
    def JAPAN(self): ...
    def JAPANESE(self): ...
    def KOREA(self): ...
    def KOREAN(self): ...
    def PRC(self): ...
    def SIMPLIFIED_CHINESE(self): ...
    def TAIWAN(self): ...
    def TRADITIONAL_CHINESE(self): ...
    def UK(self): ...
    def US(self): ...
