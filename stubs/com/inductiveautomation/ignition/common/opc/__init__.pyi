from java.lang import Enum, Object
from typing import List

class OPCBrowseElement:
    def getDataType(self) -> None: ...
    def getDescription(self) -> None: ...
    def getDisplayName(self) -> None: ...
    def getElementType(self) -> None: ...
    def getServerNodeId(self) -> None: ...

class BasicOPCBrowseElement(Object, OPCBrowseElement):
    def __init__(self, *args) -> None: ...
    def getDataType(self) -> None: ...
    def getDescription(self) -> None: ...
    def getDisplayName(self) -> None: ...
    def getElementType(self) -> None: ...
    def getServerNodeId(self) -> None: ...

class BrowseElementType(Enum):
    def isSubscribable(self) -> bool: ...
    @staticmethod
    def values() -> List[BrowseElementType]: ...

class ServerBrowseElement(Object, OPCBrowseElement):
    def __init__(self, serverName) -> None: ...
    def getDataType(self) -> None: ...
    def getDescription(self) -> None: ...
    def getDisplayName(self) -> None: ...
    def getElementType(self) -> None: ...
    def getServerNodeId(self) -> None: ...
