from typing import Any, Dict, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String

def executeAndDistribute(
    path: String,
    project: String = ...,
    parameters: Optional[Dict[String, int]] = ...,
    action: Optional[String] = ...,
    actionSettings: Optional[Dict[String, Any]] = ...,
) -> None: ...
def executeReport(
    path: String,
    project: String = ...,
    parameters: Optional[Dict[String, int]] = ...,
    fileType: String = ...,
) -> Any: ...
def getReportNamesAsDataset(
    project: Optional[String] = ..., includeReportName: Optional[bool] = ...
) -> BasicDataset: ...
def getReportNamesAsList(project: Optional[String] = ...) -> List[String]: ...
