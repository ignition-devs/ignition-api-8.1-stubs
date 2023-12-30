from typing import Iterable

from com.palantir.ptoss.cinch.core import DefaultBindableModel
from dev.coatl.helper.types import AnyStr
from java.lang import Enum

class ScheduleModel(DefaultBindableModel):
    def __init__(self) -> None: ...
    def deselectDayOfWeek(self, day: ScheduleModel.DayOfWeek) -> None: ...
    def getEveryHour(self) -> AnyStr: ...
    def getHour(self) -> AnyStr: ...
    def getMinute(self) -> AnyStr: ...
    def getSelectedDays(self) -> AnyStr: ...
    def isAlldays(self) -> bool: ...
    def isDaySelected(self, day: ScheduleModel.DayOfWeek) -> bool: ...
    def isEveryHourEnabled(self) -> bool: ...
    def isEveryMinuteEnabled(self) -> bool: ...
    def isHourEnabled(self) -> bool: ...
    def isMinuteEnabled(self) -> bool: ...
    def selectDayOfWeek(self, day: ScheduleModel.DayOfWeek) -> None: ...
    def setAllDays(self, allDays: bool) -> None: ...
    def setEveryHour(self, everyHour: AnyStr) -> None: ...
    def setHour(self, hour: AnyStr) -> None: ...
    def setHourEnabled(self, hourEnabled: bool) -> None: ...
    def setMinute(self, minute: AnyStr) -> None: ...
    def setMinuteEnabled(self, minuteEnabled: bool) -> None: ...
    def setSelectedDays(self, selectedDays: AnyStr) -> None: ...
    def toCronString(self) -> AnyStr: ...

    class DayOfWeek(Enum):
        @staticmethod
        def values() -> Iterable[ScheduleModel.DayOfWeek]: ...
