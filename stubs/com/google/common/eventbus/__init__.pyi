from typing import Any

from dev.thecesrom.helper.types import AnyStr as AnyStr
from java.lang import Object

class EventBus(Object):
    def __init__(self, *args: Any) -> None: ...
    def identifier(self) -> AnyStr: ...
    def post(self, event: Object) -> None: ...
    def register(self, obj: Object) -> None: ...
    def unregister(self, obj: Object) -> None: ...
