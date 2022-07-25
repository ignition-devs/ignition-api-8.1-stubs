from typing import List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.messages import UIResponse
from java.lang import String
from java.util import Date

def getGroups() -> List[String]: ...
def queryAgentHistory(
    groupIds: Optional[List[String]] = ...,
    agentIds: Optional[List[String]] = ...,
    startDate: Optional[Date] = ...,
    endDate: Optional[Date] = ...,
    limit: int = ...,
) -> BasicDataset: ...
def queryAgentStatus(
    groupIds: Optional[List[String]] = ...,
    agentIds: Optional[List[String]] = ...,
    isConnected: bool = ...,
) -> BasicDataset: ...
def runTask(taskname: String) -> UIResponse: ...
