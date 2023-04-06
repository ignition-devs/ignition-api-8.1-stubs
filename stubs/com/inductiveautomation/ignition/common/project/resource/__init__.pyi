from typing import Any, Mapping, Optional, Union

from com.google.common.collect import ImmutableSet
from com.inductiveautomation.ignition.common import StringPath
from com.inductiveautomation.ignition.common.gson import (
    JsonDeserializationContext,
    JsonElement,
    JsonObject,
    JsonSerializationContext,
)
from dev.thecesrom.helper.types import AnyStr
from java.lang import Comparable, Object
from java.lang.reflect import Type
from java.util.function import Consumer

class ProjectResource:
    @staticmethod
    def calculateContentDigest(resource: ProjectResource) -> bytearray: ...
    def copy(self, consumer: Optional[Consumer] = ...) -> ProjectResource: ...
    def getApplicationScope(self) -> int: ...
    def getAttribute(self, key: AnyStr) -> JsonElement: ...
    def getAttributes(self) -> Mapping[AnyStr, JsonElement]: ...
    def getContentDigest(self) -> bytearray: ...
    def getData(self) -> bytearray: ...
    def getDataKeys(self) -> ImmutableSet: ...
    def getDocumentation(self) -> AnyStr: ...
    def getFolderPath(self) -> AnyStr: ...
    def getProjectName(self) -> AnyStr: ...
    def getResourceId(self) -> ProjectResourceId: ...
    def getResourceName(self) -> AnyStr: ...
    def getResourcePath(self) -> ResourcePath: ...
    def getResourceSignature(self) -> ResourceSignature: ...
    def getResourceType(self) -> ResourceType: ...
    def getVersion(self) -> int: ...
    def isFolder(self) -> bool: ...
    def isLocked(self) -> bool: ...
    def isModuleFolder(self) -> bool: ...
    def isOverridable(self) -> bool: ...
    def isResourceTypeFolder(self) -> bool: ...
    def isRestricted(self) -> bool: ...
    def isSingletonResource(self) -> bool: ...
    @staticmethod
    def newBuilder() -> ProjectResourceBuilder: ...
    def toBuilder(self) -> ProjectResourceBuilder: ...

class ProjectResourceBuilder(Object):
    def build(self) -> ProjectResource: ...
    def clearAttributes(self) -> ProjectResourceBuilder: ...
    def clearData(self) -> ProjectResourceBuilder: ...
    def copyFrom(self, resource: ProjectResource) -> ProjectResourceBuilder: ...
    def putAttribute(self, key: AnyStr, value: Any) -> ProjectResourceBuilder: ...
    def putData(self, *args: Any) -> ProjectResourceBuilder: ...
    def removeAttribute(self, key: AnyStr) -> ProjectResourceBuilder: ...
    def removeData(self, name: AnyStr) -> ProjectResourceBuilder: ...
    def setApplicationScope(
        self, scope: Union[AnyStr, int]
    ) -> ProjectResourceBuilder: ...
    def setAttributes(
        self, attributes: Mapping[AnyStr, JsonElement]
    ) -> ProjectResourceBuilder: ...
    def setData(self, data: Mapping[AnyStr, bytearray]) -> ProjectResourceBuilder: ...
    def setDocumentation(self, documentation: AnyStr) -> ProjectResourceBuilder: ...
    def setFolder(self, folder: bool) -> ProjectResourceBuilder: ...
    def setLocked(self, locked: bool) -> ProjectResourceBuilder: ...
    def setOverridable(self, overridable: bool) -> ProjectResourceBuilder: ...
    def setProjectName(self, projectName: AnyStr) -> ProjectResourceBuilder: ...
    def setResourceId(self, id_: ProjectResourceId) -> ProjectResourceBuilder: ...
    def setResourcePath(self, resourcePath: ResourcePath) -> ProjectResourceBuilder: ...
    def setRestricted(self, restricted: bool) -> ProjectResourceBuilder: ...
    def setVersion(self, version: int) -> ProjectResourceBuilder: ...

class ProjectResourceId(Object):
    def __init__(self, *args: Any) -> None: ...
    @staticmethod
    def fromJson(e: JsonElement) -> ProjectResourceId: ...
    def getFolderPath(self) -> AnyStr: ...
    def getProjectName(self) -> AnyStr: ...
    def getResourcePath(self) -> ResourcePath: ...
    def getResourceType(self) -> ResourceType: ...
    def toJson(self) -> JsonObject: ...

class ResourcePath(Object, Comparable):
    def __init__(
        self, type_: ResourceType, path: Union[AnyStr, StringPath]
    ) -> None: ...
    def compareTo(self, o: Any) -> int: ...
    @staticmethod
    def createModuleRoot(moduleId: AnyStr) -> ResourcePath: ...
    def getChild(self, *pathParts: AnyStr) -> ResourcePath: ...
    def getFolderPath(self) -> AnyStr: ...
    def getModuleId(self) -> AnyStr: ...
    def getName(self) -> AnyStr: ...
    def getParent(self) -> ResourcePath: ...
    def getParentPath(self) -> AnyStr: ...
    def getPath(self) -> StringPath.CaseSensitiveStringPath: ...
    def getResourceType(self) -> ResourceType: ...
    def getType(self) -> ResourceType: ...
    def isAncestorOf(self, possibleDescendant: ResourcePath) -> bool: ...
    def isParentOf(self, possibleChild: ResourcePath) -> bool: ...
    def isResourceTypeFolder(self) -> bool: ...

class ResourceSignature(Object):
    def __init__(self, resourceId: ProjectResourceId, signature: bytearray) -> None: ...
    def getResourceId(self) -> ProjectResourceId: ...
    def getSignature(self) -> bytearray: ...

    class GsonAdapter(Object):
        def deserialize(
            self, json: JsonElement, typeOfT: Type, context: JsonDeserializationContext
        ) -> ResourceSignature: ...
        def serialize(
            self,
            src: ResourceSignature,
            typeOfSrc: Type,
            context: JsonSerializationContext,
        ) -> JsonElement: ...

class ResourceType(Object):
    def __init__(self, moduleId: AnyStr, typeId: AnyStr) -> None: ...
    def childOrSubPath(
        self, potentialFolder: ResourcePath, path: AnyStr
    ) -> ResourcePath: ...
    def getModuleId(self) -> AnyStr: ...
    def getTypeId(self) -> AnyStr: ...
    def matches(self, op: Any) -> bool: ...
    def rootPath(self) -> ResourcePath: ...
    def subPath(self, path: AnyStr) -> ResourcePath: ...