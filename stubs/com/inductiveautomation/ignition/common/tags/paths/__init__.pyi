from typing import Any, List, Optional, Union

from com.inductiveautomation.ignition.common.config import Property
from com.inductiveautomation.ignition.common.tags.model import TagPath
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object

class AbstractTagPath(Object, TagPath):
    @staticmethod
    def compareNullLow(c1: Property, c2: Property) -> int: ...

class BasicTagPath(AbstractTagPath):
    def __init__(
        self,
        source: AnyStr,
        pathParts: Optional[List[AnyStr]] = ...,
        prop: Optional[Property] = ...,
    ) -> None: ...
    @staticmethod
    def append(root: TagPath, arg: Union[AnyStr, TagPath]) -> TagPath: ...
    @staticmethod
    def copy(path: TagPath) -> BasicTagPath: ...
    @staticmethod
    def renameParentFolder(path: TagPath, newParent: TagPath) -> BasicTagPath: ...
    @staticmethod
    def subPath(path: TagPath, *args: Any) -> BasicTagPath: ...

class PropertyAlteredTagPath(AbstractTagPath):
    def __init__(self, path: TagPath, prop: Property) -> None: ...

class SourceAlteredTagPath(AbstractTagPath):
    def __init__(self, path: TagPath, source: AnyStr) -> None: ...
