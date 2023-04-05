from typing import Optional

from com.inductiveautomation.vision.api.client.components.model import (
    AbstractVisionPanel,
)
from dev.thecesrom.helper.types import AnyStr

class BasicContainer(AbstractVisionPanel):
    def __init__(self, name: Optional[AnyStr] = ...) -> None: ...
