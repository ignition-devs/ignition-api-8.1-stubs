from typing import Any, Dict, List, Optional, Tuple, Union

from com.inductiveautomation.ignition.common.alarming.evaluation import ShelvedPath
from com.inductiveautomation.ignition.common.alarming.query import AlarmQueryResultImpl
from java.lang import String
from java.util import Date

def acknowledge(
    alarmIds: List[String], notes: String, username: Optional[String] = ...
) -> None: ...
def cancel(alarmIds: List[String]) -> None: ...
def createRoster(name: String, description: String) -> None: ...
def getRosters() -> Dict[String, List[String]]: ...
def getShelvedPaths() -> List[ShelvedPath]: ...
def listPipelines(projectName: String = ...) -> List[String]: ...
def queryJournal(
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    journalName: Optional[String] = ...,
    priority: Optional[List[Union[String, int]]] = ...,
    state: Optional[List[Union[String, int]]] = ...,
    path: Optional[List[String]] = ...,
    source: Optional[List[String]] = ...,
    displaypath: Optional[List[String]] = ...,
    all_properties: Optional[List[Tuple[String, String, Any]]] = ...,
    any_properties: Optional[List[Tuple[String, String, Any]]] = ...,
    defined: Optional[List[String]] = ...,
    includeData: Optional[bool] = ...,
    includeSystem: Optional[bool] = ...,
    isSystem: Optional[bool] = ...,
) -> AlarmQueryResultImpl: ...
def queryStatus(
    priority: Optional[List[Union[String, int]]] = ...,
    state: Optional[List[Union[String, int]]] = ...,
    path: Optional[List[String]] = ...,
    source: Optional[List[String]] = ...,
    displaypath: Optional[List[String]] = ...,
    all_properties: Optional[List[Tuple[String, String, Any]]] = ...,
    any_properties: Optional[List[Tuple[String, String, Any]]] = ...,
    defined: Optional[List[String]] = ...,
    includeShelved: bool = ...,
) -> AlarmQueryResultImpl: ...
def shelve(
    path: List[String], timeoutSeconds: int = ..., timeoutMinutes: int = ...
) -> None: ...
def unshelve(path: List[String]) -> None: ...
