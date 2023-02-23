from typing import Any, List, Optional

from dev.thecesrom.helper.types import AnyStr
from system.bacnet.enumerated import ObjectType, PropertyIdentifier

def readRaw(
    deviceName: AnyStr,
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    propertyArrayIndex: Optional[int] = ...,
) -> List[Any]: ...
def synchronizeTime(deviceName: AnyStr) -> None: ...
def synchronizeTimeUtc(deviceName: AnyStr) -> None: ...
def writeRaw(
    deviceName: AnyStr,
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    value: Any,
    priority: int,
    propertyArrayIndex: int,
) -> None: ...
def writeWithPriority(
    deviceName: AnyStr, objectType: int, objectId: int, value: Any, priority: int
) -> None: ...

# Names in __all__ with no definition:
#   enumerated
#   enums
