from typing import Any, Dict, List, Optional, Tuple

from com.inductiveautomation.ignition.common import BasicDataset
from dev.thecesrom.helper.types import AnyStr

def copyEquipment(
    equipmentSource: AnyStr,
    newEquipmentName: AnyStr,
    enabled: bool,
    activeAddress: AnyStr,
    activePort: int,
    passiveAddress: AnyStr,
    passivePort: int,
    deviceId: int,
    dbTablePrefix: Optional[AnyStr] = ...,
    description: Optional[AnyStr] = ...,
) -> None: ...
def deleteToolProgram(ppid: AnyStr) -> None: ...
def enableDisableEquipment(
    enable: bool, names: Tuple[AnyStr, ...]
) -> List[unicode]: ...
def getResponse(
    transactionID: int,
    equipment: AnyStr,
    timeout: Optional[int] = ...,
    poll: Optional[int] = ...,
) -> Any: ...
def getToolProgram(ppid: AnyStr) -> Dict[AnyStr, Any]: ...
def getToolProgramDataset() -> BasicDataset: ...
def sendRequest(
    streamFunction: AnyStr, reply: bool, body: Any, equipment: AnyStr
) -> int: ...
def sendResponse(
    transactionID: int,
    systemBytes: int,
    streamFunction: AnyStr,
    body: Any,
    equipment: AnyStr,
) -> None: ...
def startSimEventRun(simulatorName: AnyStr, eventRunName: AnyStr) -> None: ...
def toDataSet(secsObject: Any) -> BasicDataset: ...
def toTreeDataSet(dataset: BasicDataset) -> BasicDataset: ...
