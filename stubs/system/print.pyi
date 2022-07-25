from typing import Optional

from com.inductiveautomation.factorypmi.application.script.builtin import PrintUtilities
from java.awt import Component
from java.awt.image import BufferedImage
from java.lang import String

JythonPrintJob = PrintUtilities.JythonPrintJob

def createImage(component: Component) -> BufferedImage: ...
def createPrintJob(component: Component) -> JythonPrintJob: ...
def printToImage(component: Component, filename: Optional[String] = ...) -> None: ...
