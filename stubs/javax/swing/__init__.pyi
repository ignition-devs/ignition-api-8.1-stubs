from typing import Any, List, Optional

from java.awt import Container, Frame
from java.lang import String
from javax.swing.text import JTextComponent

class Icon:
    def getIconHeight(self) -> None: ...
    def getIconWidth(self) -> None: ...
    def paintIcon(self, c, g, x, y) -> None: ...

class JComponent(Container):
    def __init__(self) -> None: ...

class JFrame(Frame):
    def __init__(self, *args: Any) -> None: ...

class JInternalFrame(JComponent):
    def __init__(
        self,
        title: Optional[String] = ...,
        resizable: Optional[bool] = ...,
        closable: Optional[bool] = ...,
        maximizable: Optional[bool] = ...,
        iconifiable: Optional[bool] = ...,
    ) -> None: ...

class JLabel(JComponent):
    def __init__(self, *args: Any) -> None: ...

class JLayeredPane(JComponent):
    DEFAULT_LAYER: int
    DRAG_LAYER: int
    FRAME_CONTENT_LAYER: int
    LAYER_PROPERTY: str
    MODAL_LAYER: int
    PALETTE_LAYER: int
    POPUP_LAYER: int
    def __init__(self) -> None: ...
    def getComponentCountInLayer(self, layer) -> None: ...
    def getLayer(self, c) -> None: ...
    def highestLayer(self) -> None: ...
    def lowestLayer(self) -> None: ...
    def setPosition(self, c, position) -> None: ...

class JDesktopPane(JLayeredPane):
    def __init__(self) -> None: ...
    def getAllFrames(self) -> None: ...
    def getAllFramesInLayer(self) -> None: ...
    def getDesktopManager(self) -> None: ...
    def getDragMode(self) -> None: ...
    def getSelectedFrame(self) -> None: ...
    def getUI(self) -> None: ...
    def getUIClassID(self) -> None: ...
    def updateUI(self) -> None: ...

class JOptionPane(JComponent):
    PLAIN_MESSAGE: int
    ERROR_MESSAGE: int
    INFORMATION_MESSAGE: int
    WARNING_MESSAGE: int
    QUESTION_MESSAGE: int
    DEFAULT_OPTION: int
    YES_NO_OPTION: int
    YES_NO_CANCEL_OPTION: int
    OK_CANCEL_OPTION: int
    CLOSED_OPTION: int
    OK_OPTION: int
    YES_OPTION: int
    NO_OPTION: int
    CANCEL_OPTION: int
    @staticmethod
    def showConfirmDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        optionType: Optional[int] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
    ) -> int: ...
    @staticmethod
    def showInputDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
        selectionValues: Optional[List[Any]] = ...,
        initialSelectionValue: Optional[Any] = ...,
    ) -> String: ...
    @staticmethod
    def showMessageDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
    ) -> None: ...
    @staticmethod
    def showOptionDialog(
        parentComponent: Optional[Any],
        message: Any,
        title: Optional[String] = ...,
        optionType: Optional[int] = ...,
        messageType: Optional[int] = ...,
        icon: Optional[Icon] = ...,
        options: Optional[List[Any]] = ...,
        initialValue: Optional[Any] = ...,
    ) -> int: ...

class JPanel(JComponent):
    def __init__(self, *args: Any) -> None: ...

class JToolTip(JComponent):
    def getAccessibleContext(self) -> None: ...
    def getComponent(self): ...
    def getTipText(self) -> None: ...

class JPopupMenu(JComponent):
    def __init__(self, label: Optional[String] = ...) -> None: ...
    def addAncestorListener(self, listener) -> None: ...
    def addNotify(self) -> None: ...
    def createToolTip(self): ...
    @staticmethod
    def getDefaultLocale() -> None: ...
    @staticmethod
    def isLightweightComponent(c) -> None: ...
    @staticmethod
    def setDefaultLocale(l) -> None: ...

class JTextField(JTextComponent):
    def __init__(self, *args: Any) -> None: ...
