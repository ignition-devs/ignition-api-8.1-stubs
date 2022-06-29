from com.inductiveautomation.ignition.common.opc import BrowseElementType
from com.inductiveautomation.ignition.common.sqltags.model.types import DataType
from com.inductiveautomation.ignition.common.tags.config.types import TagObjectType
from java.lang import Class, Object
from typing import Optional

class BrowseTag(Object):
    dataType: DataType
    name: str
    fullPath: str
    path: str
    type: TagObjectType
    valueSource: str
    def __init__(self, name: str, path: str, fullPath: str, type_: TagObjectType, valueSource: str, dataType: DataType) -> None: ...
    def getDataType(self): ...
    def getFullPath(self): ...
    def getPath(self): ...
    def getTagType(self): ...
    def getValueSource(self): ...
    def isDB(self): ...
    def isExpression(self): ...
    def isFolder(self): ...
    def isMemory(self): ...
    def isOPC(self): ...
    def isQuery(self): ...
    def isUDT(self): ...

class OPCBrowseTag(Object):
    def __init__(self, opcServer: Optional[str] = ..., type_: Optional[BrowseElementType] = ..., displayName: Optional[str] = ..., displayPath: Optional[str] = ..., dataType: Optional[Class] = ..., opcItemPath: Optional[str] = ...) -> None: ...
    def getDataType(self): ...
    def getDisplayName(self): ...
    def getDisplayPath(self): ...
    def getOpcItemPath(self): ...
    def getOpcServer(self): ...
    def getType(self): ...
