from typing import Any, Iterable, Optional, Union

from com.inductiveautomation.ignition.common.gson.reflect import TypeToken
from com.inductiveautomation.ignition.common.gson.stream import JsonReader, JsonWriter
from dev.coatl.helper.types import AnyNum, AnyStr
from java.io import Reader, Writer
from java.lang import Class, Enum, Object
from java.lang.reflect import Type

class ExclusionStrategy:
    def shouldSkipClass(self, clazz: Class) -> bool: ...
    def shouldSkipField(self, attributes: FieldAttributes) -> bool: ...

class FieldNamingStrategy:
    def translateName(self, arg: Any) -> AnyStr: ...

class JsonDeserializationContext:
    def deserialize(self, var1: JsonElement, var2: Type) -> Any: ...

class JsonSerializationContext:
    def serialize(self, var1: Object, var2: Optional[Type] = ...) -> JsonElement: ...

class TypeAdapterFactory:
    def create(self, gson: Gson, token: TypeToken) -> TypeAdapter: ...

class FieldAttributes(Object):
    def __init__(self, *args: Any) -> None: ...
    def getAnnotation(self, annotation: Class) -> Any: ...
    def getAnnotations(self) -> Iterable[Any]: ...
    def getDeclaredClass(self) -> Class: ...
    def getDeclaredType(self) -> Any: ...
    def getDeclaringClass(self) -> Class: ...
    def getName(self) -> AnyStr: ...
    def hasModifier(self, modifier: int) -> bool: ...
    def isSynthetic(self) -> bool: ...

class FieldNamingPolicy(Enum, FieldNamingStrategy):
    IDENTITY: AnyStr
    UPPER_CAMEL_CASE: AnyStr
    UPPER_CAMEL_CASE_WITH_SPACES: AnyStr
    LOWER_CASE_WITH_UNDERSCORES: AnyStr
    LOWER_CASE_WITH_DASHES: AnyStr
    LOWER_CASE_WITH_DOTS: AnyStr
    def translateName(self, arg: Any) -> AnyStr: ...

class Gson(Object):
    def excluder(self) -> Any: ...
    def fieldNamingStrategy(self) -> FieldNamingStrategy: ...
    def fromJson(self, *args: Any) -> Any: ...
    def getAdapter(self, type: Optional[TypeToken] = ...) -> TypeAdapter: ...
    def getDelegateAdapter(
        self, skipPast: TypeAdapterFactory, type: TypeToken
    ) -> TypeAdapter: ...
    def htmlSafe(self) -> bool: ...
    def newBuilder(self) -> GsonBuilder: ...
    def newJsonReader(self, reader: Reader) -> JsonReader: ...
    def newJsonWriter(self, writer: Writer) -> JsonWriter: ...
    def serializeNulls(self) -> bool: ...
    def toJson(self, *args: Any) -> Optional[AnyStr]: ...
    def toJsonTree(self, src: Object, typeOfSrc: Any = ...) -> JsonElement: ...

class GsonBuilder:
    def __init__(self, *args: Any) -> None: ...
    def addDeserializationExclusionStrategy(
        self, strategy: ExclusionStrategy
    ) -> GsonBuilder: ...
    def addSerializationExclusionStrategy(
        self, strategy: ExclusionStrategy
    ) -> GsonBuilder: ...
    def create(self) -> Gson: ...
    def disableHtmlEscaping(self) -> GsonBuilder: ...
    def disableInnerClassSerialization(self) -> GsonBuilder: ...
    def enableComplexMapKeySerialization(self) -> GsonBuilder: ...
    def excludeFieldsWithoutExposeAnnotation(self) -> GsonBuilder: ...
    def excludeFieldsWithModifiers(self, *args: int) -> GsonBuilder: ...
    def generateNonExecutableJson(self) -> GsonBuilder: ...
    def setLenient(self) -> GsonBuilder: ...
    def registerTypeAdapter(self, type: Any, typeAdapter: Object) -> GsonBuilder: ...
    def registerTypeAdapterFactory(
        self, factory: TypeAdapterFactory
    ) -> GsonBuilder: ...
    def registerTypeHierarchyAdapter(
        self, baseType: Class, typeAdapter: Object
    ) -> GsonBuilder: ...
    def serializeNulls(self) -> GsonBuilder: ...
    def serializeSpecialFloatingPointValues(self) -> GsonBuilder: ...
    def setDateFormat(self, *args: Any) -> GsonBuilder: ...
    def setExclusionStrategies(self, *args: ExclusionStrategy) -> GsonBuilder: ...
    def setFieldNamingPolicy(
        self, namingConvention: FieldNamingPolicy
    ) -> GsonBuilder: ...
    def setFieldNamingStrategy(
        self, fieldNamingStrategy: FieldNamingStrategy
    ) -> GsonBuilder: ...
    def setLongSerializationPolicy(
        self, policy: LongSerializationPolicy
    ) -> GsonBuilder: ...
    def setPrettyPrinting(self) -> GsonBuilder: ...
    def setVersion(self, ignoreVersionsAfter: float) -> GsonBuilder: ...

class JsonElement:
    def deepCopy(self) -> JsonElement: ...
    def getAsBigDecimal(self) -> float: ...
    def getAsBigInteger(self) -> int: ...
    def getAsBoolean(self) -> bool: ...
    def getAsByte(self) -> Any: ...
    def getAsCharacter(self) -> str: ...
    def getAsDouble(self) -> float: ...
    def getAsFloat(self) -> float: ...
    def getAsInt(self) -> int: ...
    def getAsJsonArray(self) -> JsonArray: ...
    def getAsJsonObject(self) -> JsonObject: ...
    def getAsJsonPrimitive(self) -> JsonPrimitive: ...
    def getAsJsonNull(self) -> JsonNull: ...
    def getAsLong(self) -> long: ...
    def getAsNumber(self) -> AnyNum: ...
    def getAsShort(self) -> int: ...
    def isJsonArray(self) -> bool: ...
    def isJsonObject(self) -> bool: ...
    def isJsonPrimitive(self) -> bool: ...
    def isJsonNull(self) -> bool: ...

class JsonArray(JsonElement):
    def __init__(self, capacity: Optional[int] = ...) -> None: ...
    def add(self, arg: Any) -> None: ...
    def addAll(self, array: JsonArray) -> None: ...
    def contains(self, element: JsonElement) -> bool: ...
    def get(self, i: int) -> JsonElement: ...
    def getAsBigDecimal(self) -> float: ...
    def getAsBigInteger(self) -> int: ...
    def getAsBoolean(self) -> bool: ...
    def getAsByte(self) -> Any: ...
    def getAsCharacter(self) -> str: ...
    def getAsDouble(self) -> float: ...
    def getAsFloat(self) -> float: ...
    def getAsInt(self) -> int: ...
    def getAsLong(self) -> long: ...
    def getAsNumber(self) -> AnyNum: ...
    def getAsShort(self) -> int: ...
    def iterator(self) -> Iterable[JsonElement]: ...
    def remove(self, index: int) -> JsonElement: ...
    def size(self) -> int: ...

class JsonNull(JsonElement):
    def equals(self, other: Object) -> bool: ...
    def getAsBigDecimal(self) -> float: ...
    def getAsBigInteger(self) -> int: ...
    def getAsBoolean(self) -> bool: ...
    def getAsByte(self) -> Any: ...
    def getAsCharacter(self) -> str: ...
    def getAsDouble(self) -> float: ...
    def getAsFloat(self) -> float: ...
    def getAsInt(self) -> int: ...
    def getAsLong(self) -> long: ...
    def getAsNumber(self) -> AnyNum: ...
    def getAsShort(self) -> int: ...
    def hashCode(self) -> int: ...

class JsonObject(JsonElement):
    def add(self, property: AnyStr, value: JsonElement) -> None: ...
    def addProperty(self, property: AnyStr, value: Any) -> None: ...
    def createJsonElement(self, value: Object) -> JsonElement: ...
    def get(self, memberName: AnyStr) -> JsonElement: ...
    def getAsBigDecimal(self) -> float: ...
    def getAsBigInteger(self) -> int: ...
    def getAsBoolean(self) -> bool: ...
    def getAsByte(self) -> Any: ...
    def getAsCharacter(self) -> str: ...
    def getAsDouble(self) -> float: ...
    def getAsFloat(self) -> float: ...
    def getAsInt(self) -> int: ...
    def getAsLong(self) -> long: ...
    def getAsNumber(self) -> AnyNum: ...
    def getAsShort(self) -> int: ...
    def has(self, memberName: AnyStr) -> bool: ...
    def remove(self, property: AnyStr) -> JsonElement: ...
    def size(self) -> int: ...

class JsonPrimitive(JsonElement):
    def __init__(self, arg: Any) -> None: ...
    def equals(self, other: Object) -> bool: ...
    def getAsBigDecimal(self) -> float: ...
    def getAsBigInteger(self) -> int: ...
    def getAsBoolean(self) -> bool: ...
    def getAsByte(self) -> Any: ...
    def getAsCharacter(self) -> str: ...
    def getAsDouble(self) -> float: ...
    def getAsFloat(self) -> float: ...
    def getAsInt(self) -> int: ...
    def getAsLong(self) -> long: ...
    def getAsNumber(self) -> AnyNum: ...
    def getAsShort(self) -> int: ...
    def hashCode(self) -> int: ...
    def isBoolean(self) -> bool: ...
    @staticmethod
    def isPrimitiveOrString(target: Object) -> bool: ...
    @staticmethod
    def isIntegral(primitive: JsonPrimitive) -> bool: ...
    def isString(self) -> bool: ...

class LongSerializationPolicy:
    DEFAULT: JsonElement
    STRING: JsonElement
    def serialize(self, arg: long) -> JsonElement: ...

class TypeAdapter:
    def fromJson(self, arg: Union[Reader, AnyStr]) -> Any: ...
    def fromJsonTree(self, jsonTree: JsonElement) -> Any: ...
    def nullSafe(self) -> TypeAdapter: ...
    def read(self, reader: JsonReader) -> Any: ...
    def toJson(self, out: Writer, value: Any) -> Optional[AnyStr]: ...
    def toJsonTree(self, value: Any) -> JsonElement: ...
    def write(self, var1: JsonWriter, var2: Any) -> None: ...
