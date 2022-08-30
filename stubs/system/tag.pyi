from typing import Any, Callable, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import (
    BasicQualifiedValue,
    QualityCode,
)
from com.inductiveautomation.ignition.common.sqltags.history.annotations import (
    Annotation,
)
from java.lang import String
from java.util import Date

DEFAULT_TIMEOUT_MILLIS: int
LEGACY_DEFAULT_TIMEOUT_MILLIS: int
TAG_PATH: Any

def browse(path: String, filter: Optional[Dict[String, Any]] = ...) -> Results: ...
def browseHistoricalTags(
    path: String,
    nameFilters: Optional[List[String]] = ...,
    maxSize: Optional[int] = ...,
    continuationPoint: Optional[Any] = ...,
) -> Results: ...
def configure(
    basePath: String, tags: List[Dict[String, Any]], collisionPolicy: String = ...
) -> List[QualityCode]: ...
def copy(
    tags: List[String], destination: String, collisionPolicy: String = ...
) -> List[QualityCode]: ...
def deleteAnnotations(
    paths: List[String], storageIds: List[String]
) -> List[BasicQualifiedValue]: ...
def deleteTags(tagPaths: List[String]) -> List[QualityCode]: ...
def exists(tagPath: String) -> bool: ...
def exportTags(
    filePath: String,
    tagPaths: List[String],
    recursive: bool = ...,
    exportType: String = ...,
) -> None: ...
def getConfiguration(
    basePath: String, recursive: bool = ...
) -> List[Dict[String, Any]]: ...
def importTags(
    filePath: String, basePath: String, collisionPolicy: String = ...
) -> List[QualityCode]: ...
def isOverlaysEnabled() -> bool: ...
def move(
    tags: String, destination: String, collisionPolicy: String = ...
) -> List[QualityCode]: ...
def query(
    provider: Optional[String] = ...,
    query: Optional[Dict[String, Any]] = ...,
    limit: Optional[int] = ...,
    continuation: Optional[String] = ...,
) -> Results: ...
def queryAnnotations(
    paths: List[String],
    startTime: Optional[Date] = ...,
    endTime: Optional[Date] = ...,
    types: Optional[List[String]] = ...,
) -> List[Annotation]: ...
def queryTagCalculations(
    paths: List[String],
    calculations: List[String],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    rangeHours: Optional[int] = ...,
    rangeMinutes: Optional[int] = ...,
    aliases: Optional[List[String]] = ...,
    includeBoundingValues: bool = ...,
    validatesSCExec: bool = ...,
    noInterpolation: bool = ...,
    ignoreBadQuality: bool = ...,
) -> BasicDataset: ...
def queryTagDensity(
    paths: List[String], startDate: Date, endDate: Date
) -> BasicDataset: ...
def queryTagHistory(
    paths: List[String],
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    returnSize: int = ...,
    aggregationMode: String = ...,
    returnFormat: String = ...,
    columnNames: Optional[List[String]] = ...,
    intervalHours: Optional[int] = ...,
    intervalMinutes: Optional[int] = ...,
    rangeHours: Optional[int] = ...,
    rangeMinutes: Optional[int] = ...,
    aggregationModes: Optional[List[String]] = ...,
    includeBoundingValues: Optional[bool] = ...,
    validateSCExec: Optional[bool] = ...,
    noInterpolation: Optional[bool] = ...,
    ignoreBadQuality: Optional[bool] = ...,
    timeout: Optional[int] = ...,
    intervalSeconds: Optional[int] = ...,
    rangeSeconds: Optional[int] = ...,
) -> BasicDataset: ...
def readAsync(tagPaths: List[String], callback: Callable[..., Any]) -> None: ...
def readBlocking(
    tagPaths: List[String], timeout: int = ...
) -> List[BasicQualifiedValue]: ...
def rename(
    tag: String, newName: String, collisionPollicy: String = ...
) -> QualityCode: ...
def requestGroupExecution(provider: String, tagGroup: String) -> None: ...
def setOverlaysEnabled(enabled: bool) -> None: ...
def storeAnnotations(
    paths: List[String],
    startTimes: Optional[List[Date]] = ...,
    endTimes: Optional[List[Date]] = ...,
    types: Optional[List[Annotation]] = ...,
    data: Optional[List[String]] = ...,
    storageIds: Optional[List[int]] = ...,
    deleted: Optional[List[bool]] = ...,
) -> List[BasicQualifiedValue]: ...
def storeTagHistory(
    historyprovider: String,
    tagprovider: String,
    paths: List[String],
    values: List[Any],
    qualities: Optional[List[int]] = ...,
    timestamps: Optional[List[Date]] = ...,
) -> None: ...
def writeAsync(
    tagPaths: List[String],
    values: List[Any],
    callback: Optional[Callable[..., Any]] = ...,
) -> None: ...
def writeBlocking(
    tagPaths: List[String], values: List[Any], timeout: int = ...
) -> List[QualityCode]: ...
