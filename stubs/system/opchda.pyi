from typing import Any, List

from com.inductiveautomation.ignition.common.browsing import Results
from com.inductiveautomation.ignition.common.model.values import QualityCode
from com.inductiveautomation.ignition.common.sqltags.history import AggregateInfo
from java.lang import String
from java.util import Date

def browse(root: String) -> List[Results]: ...
def getAggregates(serverName: String) -> List[AggregateInfo]: ...
def getAttributes(serverName: String) -> List[AggregateInfo]: ...
def getServers() -> List[String]: ...
def insert(
    serverName: String, itemId: String, value: Any, date: Any, quality: int
) -> QualityCode: ...
def insertReplace(
    serverName: String, itemId: String, value: Any, date: Date, quality: int
) -> QualityCode: ...
def isServerAvailable(serverName: String) -> bool: ...
def readAttributes(
    serverName: String,
    itemId: String,
    attributeIds: String,
    startDate: Date,
    endDate: Date,
) -> List[Any]: ...
def readProcessed(
    serverName: String,
    itemIds: List[String],
    startDate: Date,
    endDate: Date,
    resampleIntervalMS: int,
    aggregates: List[Any],
) -> List[Any]: ...
def readRaw(
    serverName: String,
    itemIds: List[String],
    startDate: Date,
    endDate: Date,
    maxValues: int,
    boundingValues: bool,
) -> List[Any]: ...
def replace(
    serverName: String, itemId: String, value: Any, date: Date, quality: int
) -> QualityCode: ...
