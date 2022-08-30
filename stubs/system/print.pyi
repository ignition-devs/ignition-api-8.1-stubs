from typing import Optional

from com.inductiveautomation.factorypmi.application.script.builtin import PrintUtilities
from java.awt import Component
from java.awt.image import BufferedImage
from java.lang import String

LANDSCAPE: int
PORTRAIT: int

def createImage(component: Component) -> BufferedImage: ...
def createPrintJob(component: Component) -> PrintUtilities.JythonPrintJob: ...
def printToImage(component: Component, filename: Optional[String] = ...) -> None: ...
