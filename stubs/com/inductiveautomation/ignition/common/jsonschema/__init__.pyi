from typing import Any, Dict, List, Optional, Set, Tuple

from com.inductiveautomation.ignition.common import JsonPath as JsonPath
from com.inductiveautomation.ignition.common.gson import JsonArray as JsonArray
from com.inductiveautomation.ignition.common.gson import JsonElement as JsonElement
from java.io import InputStream
from java.lang import Enum, Object
from java.lang import String as String
from java.util.regex import Pattern

class JsonValidator:
    AT_ROOT: String
    def validate(self, *args: Any) -> Set[ValidationMessage]: ...

class BaseJsonValidator(Object, JsonValidator):
    def __init__(self, *args: Any) -> None: ...
    def asInt(self, element: JsonElement) -> int: ...
    def validate(self, *args: Any) -> Set[ValidationMessage]: ...

class ItemsValidator(BaseJsonValidator):
    PROPERTY: String
    def __init__(self, *args: Any) -> None: ...
    def deriveDefaultArray(self, includeExample: Optional[bool] = ...) -> JsonArray: ...
    def findSchemaForIndex(self, index: int) -> Optional[JsonSchema]: ...
    def getDefaultItem(self) -> Optional[JsonElement]: ...
    def getSchemas(self) -> List[JsonSchema]: ...
    def isBoundedSchema(self) -> Set[ValidationMessage]: ...

class JsonSchema(BaseJsonValidator):
    IGNITION_SCHEMA_PATTERN: Pattern
    IGNITION_SCHEMA_URN: String
    def __init__(self, *args: Any) -> None: ...
    def acceptsType(self, type: JsonType) -> bool: ...
    def findAncestor(self) -> JsonSchema: ...
    def findAncestorMatchingPath(
        self, matchingPath: String
    ) -> Optional[JsonSchema]: ...
    def findSchemaForPath(self, path: JsonPath) -> Optional[JsonSchema]: ...
    def getChildDefaultValue(self, type: JsonType) -> Optional[JsonElement]: ...
    def getDeclaredProperties(self) -> List[String]: ...
    def getDefaultValue(self, includeExamples: Optional[bool] = ...) -> JsonElement: ...
    def getDescription(self) -> String: ...
    def getDynamicSuggestionPath(self) -> String: ...
    def getEnumChoices(self) -> Dict[String, JsonElement]: ...
    def getExamples(self) -> List[JsonElement]: ...
    def getExampleValue(self) -> Optional[JsonElement]: ...
    def getExtension(self, key: String) -> Optional[JsonElement]: ...
    def getFormat(self) -> String: ...
    def getItemsValidator(self) -> ItemsValidator: ...
    def getRefSchemaNode(self, String: String = ...) -> JsonElement: ...
    def getSchemasForItems(self) -> List[JsonSchema]: ...
    def getSchemasForProperties(self) -> Dict[String, JsonSchema]: ...
    def getSuggestions(self) -> Dict[String, JsonElement]: ...
    def getTitle(self) -> String: ...
    def getTypeValidator(self) -> TypeValidator: ...
    def getVisibleWhenCondition(self) -> Optional[Tuple[String, List[JsonElement]]]: ...
    def hasChildren(self) -> bool: ...
    def isDeprecated(self) -> bool: ...
    def isType(self, type: JsonType) -> bool: ...
    @staticmethod
    def parse(stream: InputStream) -> JsonSchema: ...

class JsonType(Enum):
    OBJECT: str
    ARRAY: str
    STRING: str
    NUMBER: str
    INTEGER: str
    BOOLEAN: str
    NULL: str
    DATASET: str
    DATE: str
    UNKNOWN: str
    @staticmethod
    def typeOf(element: JsonElement) -> JsonType: ...
    @staticmethod
    def values() -> List[JsonType]: ...

class ValidationMessage(Object):
    def getCode(self) -> String: ...
    def getMessage(self) -> String: ...
    def getPath(self) -> String: ...
    def getType(self) -> String: ...
    def setArguments(self, *args: String) -> None: ...
    def setType(self, type: String) -> None: ...

    class Builder(Object):
        def arguments(self, *args: String) -> ValidationMessage.Builder: ...
        def build(self) -> ValidationMessage: ...
        def code(self, code: String) -> ValidationMessage.Builder: ...
        def format(self, format: String) -> ValidationMessage.Builder: ...
        def path(self, path: String) -> ValidationMessage.Builder: ...
        def type(self, type: String) -> ValidationMessage.Builder: ...

class TypeValidator(BaseJsonValidator):
    def __init__(self, *args: Any) -> None: ...
    def getAcceptedTypes(self) -> Set[JsonType]: ...
