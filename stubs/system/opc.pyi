from com.inductiveautomation.ignition.common.model.values import BasicQualifiedValue, QualityCode
from com.inductiveautomation.ignition.common.opc import BasicOPCBrowseElement
from com.inductiveautomation.ignition.common.script.builtin import AbstractOPCUtilities
from com.inductiveautomation.ignition.common.script.builtin.ialabs import OPCBrowseTag
from typing import Any, List, Optional, Union

String = Union[str, unicode]
PyOPCTag = AbstractOPCUtilities.PyOPCTag

def browse(opcServer: String, device: String, folderPath: String, opcItemPath: String) -> List[OPCBrowseTag]: ...
def browseServer(opcServer: String, nodeId: String) -> List[Union[BasicOPCBrowseElement, PyOPCTag]]: ...
def browseSimple(opcServer: String, device: String, folderPath: String, opcItemPath: String) -> List[OPCBrowseTag]: ...
def getServerState(opcServer: String) -> Optional[String]: ...
def getServers(includeDisabled: Optional[bool] = ...) -> List[String]: ...
def isServerEnabled(serverName: String) -> bool: ...
def readValue(opcServer: String, itemPath: String) -> BasicQualifiedValue: ...
def readValues(opcServer: String, itemPaths: List[String]) -> List[BasicQualifiedValue]: ...
def setServerEnabled(serverName: String, enabled: bool) -> None: ...
def writeValue(opcServer: String, itemPath: String, value: Any) -> QualityCode: ...
def writeValues(opcServer: String, itemPaths: List[String], values: List[Any]) -> List[QualityCode]: ...
