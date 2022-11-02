from typing import Any, Optional, Set

from java.lang import Object
from java.lang import String as String
from java.lang import Throwable
from java.util import Locale

class ExceptionContext(Object):
    def __init__(self, throwable: Throwable) -> None: ...
    def addMessage(self, pattern: String, *args: Any) -> None: ...
    def getKeys(self) -> Set[String]: ...
    def getLocalizedMessage(self) -> String: ...
    def getMessage(
        self, locale: Optional[Locale] = ..., separator: Optional[String] = ...
    ) -> String: ...
    def getThrowable(self) -> Throwable: ...
    def getValue(self, key: String) -> None: ...
    def setValue(self, key: String, value: Object) -> None: ...
