from typing import Any, List

from com.inductiveautomation.ignition.common.tags.model import TagPath
from java.lang import Object, String

class TagPathParser(Object):
    PARENT_RELATIVE: String
    PATH_SEPARATOR: String
    PROPERTY_SEPARATOR: String
    RELATIVE_DIR_UP: String
    ROOT_RELATIVE: String
    @staticmethod
    def chopPath(string: String) -> List[String]: ...
    @staticmethod
    def derelativize(tagPath: TagPath, relativeRoot: TagPath) -> TagPath: ...
    @staticmethod
    def isRelativePath(path: TagPath) -> bool: ...
    @staticmethod
    def parse(*args: Any) -> TagPath: ...
    @staticmethod
    def parseSafe(*args: Any) -> TagPath: ...
    @staticmethod
    def relativize(newPath: TagPath, relativeTo: TagPath) -> TagPath: ...
