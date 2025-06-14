from typing import Any

from dev.coatl.helper.types import AnyStr
from java.lang import Object
from org.python.core import PyObject

class SerialScriptModule(Object):
    class PortManager:
        def __init__(self, *args: Any) -> None: ...
        def __enter__(self) -> None: ...
        def __exit__(
            self, exc_type: object, exc_val: object, exc_tb: object
        ) -> None: ...

    class SerialConfigurator:
        def setBitRate(self, value: int) -> SerialScriptModule.SerialConfigurator: ...
        def setDataBits(self, value: int) -> SerialScriptModule.SerialConfigurator: ...
        def setFlowControl(
            self, value: bool
        ) -> SerialScriptModule.SerialConfigurator: ...
        def setHandshake(self, value: int) -> SerialScriptModule.SerialConfigurator: ...
        def setHardwareFlowControl(
            self, value: int
        ) -> SerialScriptModule.SerialConfigurator: ...
        def setParity(self, value: int) -> SerialScriptModule.SerialConfigurator: ...
        def setStopBits(self, value: int) -> SerialScriptModule.SerialConfigurator: ...

    class SerialPortWrapper(PyObject):
        def __init__(self, port: AnyStr, serialPort: Any) -> None: ...
        def readBytes(
            self, port: AnyStr, numberOfBytes: int, timeout: int = ...
        ) -> bytearray: ...
        def readBytesAsString(
            self,
            port: AnyStr,
            numberOfBytes: int,
            timeout: int = ...,
            encoding: AnyStr = ...,
        ) -> AnyStr: ...
        def readLine(
            self,
            port: AnyStr,
            timeout: int = ...,
            encoding: AnyStr = ...,
            crlfRequired: bool = ...,
        ) -> AnyStr: ...
        def readUntil(
            self,
            port: AnyStr,
            delimiter: str,
            includeDelimiter: bool,
            timeout: int = ...,
        ) -> AnyStr: ...
        def sendBreak(self, port: AnyStr, millis: long) -> None: ...
        def write(
            self, port: AnyStr, toWrite: bytearray, encoding: AnyStr = ...
        ) -> None: ...
        def writeBytes(
            self, port: AnyStr, toWrite: bytearray, timeout: int = ...
        ) -> None: ...

    def __init__(self) -> None: ...
    @staticmethod
    def setTrialExpired(trialExpired: bool) -> None: ...
