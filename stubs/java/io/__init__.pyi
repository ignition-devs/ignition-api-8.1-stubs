from typing import Any, Union

from java.lang import Appendable, AutoCloseable, CharSequence, Object

class Closeable(AutoCloseable):
    def close(self) -> None: ...

class FileDescriptor(Object):
    def sync(self) -> None: ...
    def valid(self) -> None: ...

class OutputStream(Object):
    def close(self) -> None: ...
    def flush(self) -> None: ...
    @staticmethod
    def nullOutputStream(): ...
    def write(self, *args) -> None: ...

class FileOutputStream(OutputStream):
    def __init__(self, *args) -> None: ...
    def getChannel(self) -> None: ...
    def getFD(self): ...

class FilterOutputStream(OutputStream):
    def __init__(self, out: OutputStream) -> None: ...

class DataOutputStream(FilterOutputStream):
    out: OutputStream
    written: int
    def __init__(self, out) -> None: ...
    def size(self) -> None: ...
    def writeBoolean(self, v) -> None: ...
    def writeByte(self, v) -> None: ...
    def writeBytes(self, s) -> None: ...
    def writeChar(self, v) -> None: ...
    def writeChars(self, s) -> None: ...
    def writeDouble(self, v) -> None: ...
    def writeFloat(self, v) -> None: ...
    def writeInt(self, v) -> None: ...
    def writeLong(self, v) -> None: ...
    def writeShort(self, v) -> None: ...
    def writeUTF(self, s) -> None: ...

class PrintStream(FilterOutputStream):
    def __init__(self, *args) -> None: ...
    def append(self, *args) -> None: ...
    def checkError(self) -> None: ...
    def clearError(self) -> None: ...
    def format(self, *args) -> None: ...
    def print(self, arg) -> None: ...
    def printf(self, *args) -> None: ...
    def println(self, arg) -> None: ...
    def setError(self) -> None: ...

class Flushable:
    def flush(self) -> None: ...

class InputStream(Object):
    def available(self) -> None: ...
    def close(self) -> None: ...
    def mark(self, readlimit) -> None: ...
    def markSupported(self) -> None: ...
    def nullInputStream(self) -> None: ...
    def read(self, *args) -> None: ...
    def readAllBytes(self) -> None: ...
    def readNBytes(self, *args) -> None: ...
    def reset(self) -> None: ...
    def skip(self, n) -> None: ...
    def transferTo(self, out) -> None: ...

class Writer(Object, Appendable, Closeable, Flushable):
    def append(
        self, c_csq: Union[CharSequence, str], start: int = ..., end: int = ...
    ) -> Writer: ...
    def close(self) -> None: ...
    def flush(self) -> None: ...
    @staticmethod
    def nullWriter() -> Writer: ...
    def write(self, *args: Any) -> None: ...

class PrintWriter(Writer):
    def __init__(self, *args: Any) -> None: ...
    def append(
        self, c_csq: Union[CharSequence, str], start: int = ..., end: int = ...
    ) -> PrintWriter: ...
    def checkError(self) -> bool: ...
    def format(self, *args: Any) -> PrintWriter: ...
    def print(self, arg: Any) -> None: ...
    def printf(self, *args: Any) -> PrintWriter: ...
    def println(self, arg: Any) -> None: ...
    def write(self, *args: Any) -> None: ...
