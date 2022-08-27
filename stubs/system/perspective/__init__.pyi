from typing import Any, Dict, List, Optional, Union

from com.inductiveautomation.ignition.common.script.adapters import PyJsonObjectAdapter
from java.lang import String

def alterDock(
    dockId: String,
    config: Optional[Dict[String, Any]] = ...,
    sessionId: String = ...,
    pageId: String = ...,
) -> None: ...
def alterLogging(
    remoteLoggingEnabled: bool = ...,
    level: String = ...,
    remoteLoggingLevel: String = ...,
    sessionId: String = ...,
    pageId: String = ...,
) -> None: ...
def authenticationChallenge(
    sessionId: String = ...,
    pageId: String = ...,
    idp: String = ...,
    forceAuth: bool = ...,
    timeout: int = ...,
    payload: Optional[Dict[String, Any]] = ...,
    framing: String = ...,
) -> None: ...
def closeDock(id: String, sessionId: String = ..., pageId: String = ...) -> None: ...
def closePage(
    message: Optional[String] = ..., sessionId: String = ..., pageId: String = ...
) -> None: ...
def closePopup(id: String, sessionId: String = ..., pageId: String = ...) -> None: ...
def closeSession(message: Optional[String] = ..., sessionId: String = ...) -> None: ...
def download(
    filename: String,
    data: Any,
    contentType: Optional[String] = ...,
    sessionId: String = ...,
    pageId: String = ...,
) -> None: ...
def getProjectInfo() -> Dict[String, Any]: ...
def getSessionInfo(
    usernameFilter: Optional[String] = ..., projectFilter: Optional[String] = ...
) -> List[PyJsonObjectAdapter]: ...
def isAuthorized(
    isAllOf: bool, securityLevels: List[String], sessionId: String = ...
) -> bool: ...
def login(
    sessionId: String = ..., pageId: String = ..., forceAuth: bool = ...
) -> None: ...
def logout(
    sessionId: String = ..., pageId: String = ..., message: String = ...
) -> None: ...
def navigate(
    page: String,
    url: Optional[String] = ...,
    view: Optional[String] = ...,
    params: Optional[Dict[String, String]] = ...,
    sessionId: String = ...,
    pageId: String = ...,
    newTab: bool = ...,
) -> None: ...
def navigateBack(sessionId: String = ..., pageId: String = ...) -> None: ...
def navigateForward(sessionId: String = ..., pageId: String = ...) -> None: ...
def openDock(
    id: String,
    sessionId: String = ...,
    pageId: String = ...,
    params: Optional[Dict[String, String]] = ...,
) -> None: ...
def openPopup(
    id: String,
    view: String,
    params: Optional[Dict[String, Any]] = ...,
    title: String = ...,
    position: Optional[Dict[String, Union[int, String]]] = ...,
    showCloseIcon: bool = ...,
    draggable: bool = ...,
    resizable: bool = ...,
    modal: bool = ...,
    overlayDismiss: bool = ...,
    sessionId: String = ...,
    pageId: String = ...,
    viewPortBound: bool = ...,
) -> None: ...
def print(
    message: String,
    sessionId: String = ...,
    pageId: String = ...,
    destination: String = ...,
) -> None: ...
def refresh(
    sessionId: Optional[String] = ..., pageId: Optional[String] = ...
) -> None: ...
def sendMessage(
    messageType: String,
    payload: Dict[String, String],
    scope: String = ...,
    sessionId: String = ...,
    pageId: String = ...,
) -> None: ...
def setTheme(
    name: String, sessionId: Optional[String] = ..., pageId: Optional[String] = ...
) -> None: ...
def toggleDock(
    id: String,
    sessionId: String = ...,
    pageId: String = ...,
    params: Optional[Dict[String, String]] = ...,
) -> None: ...
def togglePopup(
    id: String,
    view: String,
    params: Optional[Dict[String, Any]],
    title: String = ...,
    position: Optional[Dict[String, Union[int, String]]] = ...,
    showCloseIcon: bool = ...,
    draggable: bool = ...,
    resizable: bool = ...,
    modal: bool = ...,
    overlayDismiss: bool = ...,
    sessionId: String = ...,
    pageId: String = ...,
    viewPortBound: bool = ...,
) -> None: ...
def vibrateDevice(duration: int, sessionId: Optional[String] = ...) -> None: ...
