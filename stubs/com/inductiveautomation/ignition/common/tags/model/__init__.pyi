from typing import Union

from com.inductiveautomation.ignition.common import Path
from com.inductiveautomation.ignition.common.config import Property
from java.lang import String

class TagPath(Path):
    def compareTo(self, that: TagPath) -> int: ...
    def getChildPath(self, arg: Union[Property, String]) -> TagPath: ...
    def getItemName(self) -> String: ...
    def getLastPathComponent(self) -> String: ...
    def getParentPath(self) -> Path: ...
    def getPathComponent(self, i: int) -> String: ...
    def getPathLength(self) -> int: ...
    def getProperty(self) -> Property: ...
    def getSource(self) -> String: ...
    def isAncestorOf(self, path: Path) -> bool: ...
    def toStringFull(self) -> String: ...
    def toStringPartial(self) -> String: ...
