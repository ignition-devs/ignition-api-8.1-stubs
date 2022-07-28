from typing import List, Optional, Union

from java.lang import String

NUL: int
PULSE_ON: int
PULSE_OFF: int
LATCH_ON: int
LATCH_OFF: int
CLOSE: int
TRIP: int

def directOperateAnalog(
    deviceName: String,
    index: int,
    value: Union[float, int],
    variation: Optional[int] = ...,
) -> int: ...
def directOperateBinary(
    deviceName: String,
    indexes: List[int],
    opType: int,
    tcCode: Optional[int] = ...,
    count: Optional[int] = ...,
    onTime: Optional[int] = ...,
    offTime: Optional[int] = ...,
) -> int: ...
def freezeAnalogs(deviceName: String, indexes: List[int]) -> None: ...
def freezeAnalogsAtTime(
    deviceName: String, absoluteTime: int, intervalTime: int, indexes: List[int]
) -> None: ...
def freezeCounters(deviceName: String, indexes: List[int]) -> None: ...
def freezeCountersAtTime(
    deviceName: String, absoluteTime: int, intervalTime: int, indexes: List[int]
) -> None: ...
def selectOperateAnalog(
    deviceName: String,
    index: int,
    value: Union[float, int],
    variation: Optional[int] = ...,
) -> int: ...
def selectOperateBinary(
    deviceName: String,
    indexes: List[int],
    opType: int,
    tcCode: Optional[int] = ...,
    count: Optional[int] = ...,
    onTime: Optional[int] = ...,
    offTime: Optional[int] = ...,
) -> int: ...
