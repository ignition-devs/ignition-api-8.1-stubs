from typing import Any, Dict, List, Optional, Tuple

from com.inductiveautomation.ignition.common import BasicDataset
from java.lang import String

def copyEquipment(
    equipmentSource: String,
    newEquipmentName: String,
    enabled: bool,
    activeAddress: String,
    activePort: int,
    passiveAddress: String,
    passivePort: int,
    deviceId: int,
    dbTablePrefix: Optional[String] = ...,
    description: Optional[String] = ...,
) -> None: ...
def deleteToolProgram(ppid: String) -> None: ...
def enableDisableEquipment(
    enable: bool, names: Tuple[String, ...]
) -> List[unicode]: ...
def getResponse(
    transactionID: int,
    equipment: String,
    timeout: Optional[int] = ...,
    poll: Optional[int] = ...,
) -> Any: ...
def getToolProgram(ppid: String) -> Dict[String, Any]: ...
def getToolProgramDataset() -> BasicDataset: ...
def sendRequest(
    streamFunction: String, reply: bool, body: Any, equipment: String
) -> int: ...
def sendResponse(
    transactionID: int,
    systemBytes: int,
    streamFunction: String,
    body: Any,
    equipment: String,
) -> None: ...
def startSimEventRun(simulatorName: String, eventRunName: String) -> None: ...
def toDataSet(secsObject: Any) -> BasicDataset: ...
def toTreeDataSet(dataset: BasicDataset) -> BasicDataset: ...
