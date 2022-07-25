from typing import Any, List, Optional

from java.lang import String
from system.bacnet.enumerated import ObjectType, PropertyIdentifier

def readRaw(
    deviceName: String,
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    propertyArrayIndex: Optional[int] = ...,
) -> List[Any]: ...
def synchronizeTime(deviceName: String) -> None: ...
def synchronizeTimeUtc(deviceName: String) -> None: ...
def writeRaw(
    deviceName: String,
    objectType: ObjectType,
    objectId: int,
    propertyId: PropertyIdentifier,
    value: Any,
    priority: int,
    propertyArrayIndex: int,
) -> None: ...
def writeWithPriority(
    deviceName: String, objectType: int, objectId: int, value: Any, priority: int
) -> None: ...

# Names in __all__ with no definition:
#   enumerated
#   enums
