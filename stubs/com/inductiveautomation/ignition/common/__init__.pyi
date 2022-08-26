from typing import Any, List, Optional, TypeVar, Union

from com.inductiveautomation.ignition.common.document import DocumentElement
from com.inductiveautomation.ignition.common.gson import Gson
from com.inductiveautomation.ignition.common.gson import JsonElement as JsonElement
from com.inductiveautomation.ignition.common.model.values import (
    QualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.sqltags.model.types import (
    DataQuality,
    DataType,
)
from java.awt import Color
from java.lang import Class, Number, Object, String
from java.util import UUID, Comparator, Date, Locale
from org.json import JSONObject
from org.python.core import PyObject

T = TypeVar("T")

class Dataset:
    def binarySearch(self, column: int, key: Any) -> int: ...
    def getColumnAsList(self, col: int) -> List[Any]: ...
    def getColumnCount(self) -> int: ...
    def getColumnIndex(self, colName: String) -> int: ...
    def getColumnName(self, col: int) -> String: ...
    def getColumnNames(self) -> List[String]: ...
    def getColumnType(self, col: int) -> Class: ...
    def getColumnTypes(self) -> List[Class]: ...
    def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
    def getQualityAt(self, row: int, col: int) -> QualityCode: ...
    def getRowCount(self) -> int: ...
    def getValueAt(self, row: int, col: Union[int, String]) -> Any: ...
    def hasQualityData(self) -> bool: ...

class AbstractDataset(Dataset):
    def __init__(
        self,
        columnNames: List[String],
        columnTypes: List[Class],
        qualityCodes: Optional[List[List[QualityCode]]] = ...,
    ) -> None: ...
    @staticmethod
    def convertToQualityCodes(
        dataQualities: List[List[DataQuality]],
    ) -> List[List[QualityCode]]: ...
    def getBulkQualityCodes(self) -> List[List[QualityCode]]: ...
    def getColumnCount(self) -> int: ...
    def getColumnIndex(self, colName: String) -> int: ...
    def getColumnName(self, col: int) -> String: ...
    def getColumnNames(self) -> List[String]: ...
    def getColumnType(self, col: int) -> Class: ...
    def getColumnTypes(self) -> List[Class]: ...
    def getPrimitiveValueAt(self, row: int, col: int) -> float: ...
    def getQualityAt(self, row: int, col: int) -> QualityCode: ...
    def getRowCount(self) -> int: ...
    def getValueAt(self, row: int, col: Union[int, String]) -> Any: ...
    def setColumnNames(self, arg: List[str]) -> None: ...
    def setColumnTypes(self, arg: List[Class]) -> None: ...
    def setDirty(self) -> None: ...

class BasicDataset(AbstractDataset):
    def __init__(self, *args: Any) -> None: ...
    def columnContainsNulls(self, col: int) -> bool: ...
    def datasetContainsNulls(self) -> bool: ...
    def getData(self) -> Any: ...
    def setAllDirectly(
        self, columnNames: List[String], columnTypes: List[Class], data: Any
    ) -> None: ...
    def setDataDirectly(self, arg: Any) -> None: ...
    def setFromXML(
        self,
        columnNames: List[String],
        columnTypes: List[Class],
        encodedData: String,
        rowCount: int,
    ) -> None: ...
    def setValueAt(self, row: int, col: int, value: Any) -> None: ...

class JsonPath(Object):
    ROOT: JsonPath
    def createChildPath(self, arg: Union[JsonPath, int, String]) -> JsonPath: ...
    def getAsLinkedList(self) -> Any: ...
    def getDepth(self) -> int: ...
    def getKey(self) -> Object: ...
    def getParent(self) -> JsonPath: ...
    def getPathElements(self) -> List[JsonPath]: ...
    def getSubPath(self, startingDepth: int) -> JsonPath: ...
    def isAncestorOf(self, element: JsonPath) -> bool: ...
    def isRelatedTo(self, other: JsonPath) -> bool: ...
    def isRoot(self) -> bool: ...
    @staticmethod
    def isValidIdentifier(test: String) -> bool: ...
    @staticmethod
    def parse(path: String) -> String: ...

class Path:
    def getLastPathComponent(self) -> str: ...
    def getParentPath(self) -> Path: ...
    def getPathLength(self) -> int: ...
    def isAncestorOf(self, path: Path) -> bool: ...

class QualifiedPath(Object):
    def extend(self, id_, value) -> None: ...
    def getFirstPathComponent(self) -> None: ...
    def getFirstPathComponentId(self) -> None: ...

class TypeUtilities(Object):
    DATE_FORMAT_STRING: String
    NULL_SAFE_CASE_INSENSITIVE_ORDER: Comparator
    @staticmethod
    def anyEqual(value: T, *args: T) -> bool: ...
    @staticmethod
    def coerce(value: Object, destType: Class) -> Object: ...
    @staticmethod
    def coerceForLocale(
        value: Object, target: Class, valueLocale: Locale
    ) -> Object: ...
    @staticmethod
    def coerceGeneric(value: Object, destType: Class) -> T: ...
    @staticmethod
    def coerceLocaleSafe(str: String, type: Class) -> Object: ...
    @staticmethod
    def coerceNullSafe(value: Object, destType: Class) -> Object: ...
    @staticmethod
    def coerceNumberForLocale(
        value: Object, destType: Class, locale: Locale
    ) -> Object: ...
    @staticmethod
    def coerceNumberNullSafe(
        value: Object, destType: Class, locale: Locale
    ) -> Object: ...
    @staticmethod
    def colorToHex(c: Color) -> String: ...
    @staticmethod
    def compareInts(foo: int, bar: int) -> int: ...
    @staticmethod
    def compareNullHigh(c1: T, c2: T) -> T: ...
    @staticmethod
    def compareNullLow(c1: T, c2: T) -> T: ...
    @staticmethod
    def datasetFromJSON(json: JSONObject) -> Dataset: ...
    @staticmethod
    def datasetFromJsonString(jsonStr: String) -> Dataset: ...
    @staticmethod
    def datasetToGson(data: Dataset, gson: Optional[Gson] = ...) -> JsonElement: ...
    @staticmethod
    def datasetToJSON(data: Dataset) -> JSONObject: ...
    @staticmethod
    def deepEquals(o1: Object, o2: Object, checkArrayTypes: bool) -> bool: ...
    @staticmethod
    def equalsIgnoreCase(o1: Object, o2: Object) -> bool: ...
    @staticmethod
    def fromString(value: String, dest: Class, locale: Locale) -> Object: ...
    @staticmethod
    def getColorFromString(color: String) -> Color: ...
    @staticmethod
    def getFirstOrNull(list_: List[T]) -> T: ...
    @staticmethod
    def getInitValueForClass(c: Class) -> Object: ...
    @staticmethod
    def getLastNameComponent(name: String) -> String: ...
    @staticmethod
    def getPrimitiveType(c: Class) -> Object: ...
    @staticmethod
    def getWrapperType(c: Class) -> Class: ...
    @staticmethod
    def gsonToPy(element: JsonElement) -> PyObject: ...
    @staticmethod
    def hasPrimitiveType(c: Class) -> bool: ...
    @staticmethod
    def hasValueChanged(
        currentValue: QualifiedValue,
        previousValue: QualifiedValue,
        expectedType: DataType,
        deadband: float,
    ) -> bool: ...
    @staticmethod
    def isAssignable(dest: Class, source: Class) -> bool: ...
    @staticmethod
    def isBoolean(clazz: Class) -> bool: ...
    @staticmethod
    def isDirectlyAssignable(dest: Class, source: Class) -> bool: ...
    @staticmethod
    def isFractional(clazz: Class) -> bool: ...
    @staticmethod
    def isNullOrEmpty(s: String) -> bool: ...
    @staticmethod
    def isNumber(clazz: Class) -> bool: ...
    @staticmethod
    def isPrimitive(clazz: Class) -> bool: ...
    @staticmethod
    def isProperNumber(clazz: Class) -> bool: ...
    @staticmethod
    def neq(o1: Object, o2: Object) -> bool: ...
    @staticmethod
    def pyToGson(
        pyObject: PyObject, customGson: Optional[Gson] = ...
    ) -> JsonElement: ...
    @staticmethod
    def pyToJava(pyObject: PyObject) -> Object: ...
    @staticmethod
    def setArrayValue(arrayValue: Object, newVal: Object, pos: int) -> QualityCode: ...
    @staticmethod
    def setClassInitializer(init: TypeUtilities.ClassInitializer) -> None: ...
    @staticmethod
    def toBool(value: Object) -> bool: ...
    @staticmethod
    def toByteArray(uuid: UUID) -> bytearray: ...
    @staticmethod
    def toColor(color: Object) -> Color: ...
    @staticmethod
    def toDataset(value: Object) -> Dataset: ...
    @staticmethod
    def toDate(value: Object) -> Date: ...
    @staticmethod
    def toDocument(value: Object) -> DocumentElement: ...
    @staticmethod
    def toDouble(value: Object) -> float: ...
    @staticmethod
    def toEnum(enumType: Class, value: String) -> T: ...
    @staticmethod
    def toFloat(value: Object) -> float: ...
    @staticmethod
    def toInteger(value: Object) -> int: ...
    @staticmethod
    def toLong(value: Object) -> long: ...
    @staticmethod
    def toNumber(value: Object, locale: Optional[Locale] = ...) -> Number: ...
    @staticmethod
    def toShort(value: Object) -> int: ...
    @staticmethod
    def toStr(value: Object) -> String: ...
    @staticmethod
    def toStringLocalized(value: Object, locale: Optional[Locale] = ...) -> String: ...
    @staticmethod
    def toStringOnlyNumberLocalized(value: Object, locale: Locale) -> String: ...
    @staticmethod
    def toUUID(barr: bytearray) -> UUID: ...

    class ClassInitializer:
        def createNew(self, claz: Class) -> Object: ...
