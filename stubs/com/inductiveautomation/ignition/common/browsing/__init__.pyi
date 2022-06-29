from java.lang import Object
from typing import Optional

class Result:
    def getDisplayPath(self) -> None: ...
    def getPath(self) -> None: ...
    def getType(self) -> None: ...
    def hasChildren(self) -> None: ...

class Results(Object):
    def __init__(self, *args) -> None: ...
    @staticmethod
    def error(result): ...
    def getContinuationPoint(self): ...
    def getResultQuality(self): ...
    def getResults(self): ...
    def getReturnedSize(self): ...
    def getTotalAvailableSize(self): ...
    @staticmethod
    def of(results): ...
    def setContinuationPoint(self, continuationPoint: Optional[str] = ...) -> None: ...
    def setResultQuality(self, value) -> None: ...
    def setResults(self, results) -> None: ...
    def setTotalAvailableResults(self, totalAvailableResults) -> None: ...
