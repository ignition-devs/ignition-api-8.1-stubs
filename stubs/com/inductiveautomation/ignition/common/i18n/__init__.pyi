from java.lang import Object
from java.util import Locale
from typing import Any, List, Optional

class LocalizedString(Object):
    def __init__(self, *args: Any) -> None: ...
    def compareTo(self, other: LocalizedString) -> int: ...
    @staticmethod
    def createRaw(stringVal: str) -> LocalizedString: ...
    def getDefaultVal(self) -> str: ...
    def getKey(self) -> str: ...
    def getParams(self) -> List[Object]: ...
    def setDefaultVal(self, defaultVal: str) -> None: ...
    def setKey(self, key: str) -> None: ...
    def setParams(self, params: List[Object]) -> None: ...
    def toString(self, locale: Optional[Locale] = ...) -> str: ...
