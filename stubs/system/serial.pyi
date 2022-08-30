from typing import Any, List, Optional

from com.inductiveautomation.ignition.modules.serial.scripting import SerialScriptModule
from java.lang import String

BIT_RATE_110: int
BIT_RATE_150: int
BIT_RATE_300: int
BIT_RATE_600: int
BIT_RATE_1200: int
BIT_RATE_2400: int
BIT_RATE_4800: int
BIT_RATE_9600: int
BIT_RATE_19200: int
BIT_RATE_38400: int
BIT_RATE_57600: int
BIT_RATE_115200: int
BIT_RATE_230400: int
BIT_RATE_460800: int
BIT_RATE_921600: int
DATA_BITS_5: int
DATA_BITS_6: int
DATA_BITS_7: int
DATA_BITS_8: int
HANDSHAKE_CTS_DTR: int
HANDSHAKE_CTS_RTS: int
HANDSHAKE_DSR_DTR: int
HANDSHAKE_HARD_IN: int
HANDSHAKE_HARD_OUT: int
HANDSHAKE_NONE: int
HANDSHAKE_SOFT_IN: int
HANDSHAKE_SOFT_OUT: int
HANDSHAKE_SPLIT_MASK: int
HANDSHAKE_XON_XOFF: int
PARITY_EVEN: int
PARITY_ODD: int
PARITY_MARK: int
PARITY_SPACE: int
PARITY_NONE: int
STOP_BITS_1: int
STOP_BITS_2: int

def closeSerialPort(port: String) -> None: ...
def configureSerialPort(
    port: String,
    bitRate: Optional[int] = ...,
    dataBits: Optional[int] = ...,
    handshake: Optional[int] = ...,
    hardwareFlowControl: Optional[bool] = ...,
    parity: Optional[int] = ...,
    stopBits: Optional[int] = ...,
) -> SerialScriptModule.SerialConfigurator: ...
def openSerialPort(port: String) -> None: ...
def port(
    port: String,
    bitRate: Optional[int] = ...,
    dataBits: Optional[int] = ...,
    handshake: Optional[int] = ...,
    hardwareFlowControl: Optional[bool] = ...,
    parity: Optional[int] = ...,
    stopBits: Optional[int] = ...,
) -> SerialScriptModule.PortManager: ...
def readBytes(
    port: String, numberOfBytes: int, timeout: Optional[int] = ...
) -> List[Any]: ...
def readBytesAsString(
    port: String, numberOfBytes: int, timeout: int = ..., encoding: String = ...
) -> String: ...
def readLine(
    port: String, timeout: int = ..., encoding: String = ..., crlfRequired: bool = ...
) -> String: ...
def readUntil(
    port: String,
    delimiter: String,
    includeDelimiter: bool,
    timeout: Optional[int] = ...,
) -> String: ...
def sendBreak(port: String, millis: int) -> None: ...
def write(port: String, toWrite: String, encoding: Optional[String] = ...) -> None: ...
def writeBytes(port: String, toWrite: Any, timeout: Optional[int] = ...) -> None: ...
