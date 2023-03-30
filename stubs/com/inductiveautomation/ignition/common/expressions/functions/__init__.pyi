from typing import Any, Iterable

from com.inductiveautomation.ignition.common.binding import InteractionListener
from com.inductiveautomation.ignition.common.model.values import QualifiedValue
from java.lang import Class

class Function:
    def connect(self, context: Any, updateListener: InteractionListener) -> None: ...
    def copy(self) -> Function: ...
    def disconnect(self) -> None: ...
    def execute(self, args: Iterable[Any]) -> QualifiedValue: ...
    def getArgDocString(self) -> None: ...
    def getType(self) -> Class: ...
    def initArgs(self, args: Iterable[Any]) -> None: ...
    def shutdown(self) -> None: ...
    def startup(self) -> None: ...
