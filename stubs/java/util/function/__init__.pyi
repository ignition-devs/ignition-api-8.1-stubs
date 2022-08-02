from typing import TypeVar

T = TypeVar("T")

class Consumer:
    def accept(self, t: T) -> None: ...
    def andThen(self, after: Consumer) -> Consumer: ...
