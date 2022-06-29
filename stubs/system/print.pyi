from com.inductiveautomation.factorypmi.application.script.builtin import PrintUtilities
from java.awt import Component
from java.awt.image import BufferedImage
from typing import Optional, Union

JythonPrintJob = PrintUtilities.JythonPrintJob
String = Union[str, unicode]

def createImage(component: Component) -> BufferedImage: ...
def createPrintJob(component: Component) -> JythonPrintJob: ...
def printToImage(component: Component, filename: Optional[String] = ...) -> None: ...
