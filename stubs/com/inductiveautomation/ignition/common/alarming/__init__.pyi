from com.inductiveautomation.ignition.common.config import BasicPropertySet
from org.python.core import PyObject
from typing import Any, Iterable

class AlarmEvent:
    def __iter__(self) -> Iterable: ...
    def acknowledge(self, ackData: EventData) -> None: ...
    def active(self, activeData) -> None: ...
    def clear(self, clearData) -> None: ...
    def getAckData(self) -> None: ...
    def getActiveData(self) -> None: ...
    def getClearedData(self) -> None: ...
    def getDisplayPath(self) -> None: ...
    def getId(self) -> None: ...
    def getLabel(self) -> None: ...
    def getLastEventState(self) -> None: ...
    def getName(self) -> None: ...
    def getNotes(self) -> None: ...
    def getPriority(self) -> None: ...
    def getSource(self) -> None: ...
    def getState(self) -> None: ...
    def isAcked(self) -> None: ...
    def isCleared(self) -> None: ...
    def isShelved(self) -> None: ...
    def iterator(self) -> None: ...

class EventData(BasicPropertySet):
    def __init__(self, *args: Any) -> None: ...
    def getTimeStamp(self) -> long: ...

class PyAlarmEvent(AlarmEvent):
    def __iter__(self) -> Iterable: ...
    def acknowledge(self, ackData) -> None: ...
    def active(self, activeData) -> None: ...
    def clear(self, clearData) -> None: ...
    def contains(self, property) -> None: ...
    def get(self, property) -> None: ...
    def getAckData(self) -> None: ...
    def getActiveData(self) -> None: ...
    def getClearedData(self) -> None: ...
    def getDisplayPath(self) -> None: ...
    def getId(self) -> None: ...
    def getLabel(self) -> None: ...
    def getLastEventState(self) -> None: ...
    def getName(self) -> None: ...
    def getNotes(self) -> None: ...
    def getOrDefault(self, property) -> None: ...
    def getOrElse(self, property, defaultValue) -> None: ...
    def getPriority(self) -> None: ...
    def getSource(self) -> None: ...
    def getState(self) -> None: ...
    def isAcked(self) -> None: ...
    def isCleared(self) -> None: ...
    def isShelved(self) -> None: ...
    def set(self, property, value) -> None: ...
    def setGlobal(self, property, value) -> None: ...
    def sourceEvent(self) -> None: ...

class PyAlarmEventImpl(PyAlarmEvent, PyObject):
    def __init__(self, event) -> None: ...
    def contains(self, property) -> None: ...
    def get(self, property) -> None: ...
    def getOrDefault(self, property) -> None: ...
    def getOrElse(self, property, defaultValue) -> None: ...
    def set(self, property, value) -> None: ...
    def setGlobal(self, property, value) -> None: ...
    def sourceEvent(self) -> None: ...
