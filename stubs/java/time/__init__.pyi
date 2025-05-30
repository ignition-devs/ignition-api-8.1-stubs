from typing import Any, Dict, List, Optional, Set, Union

from dev.coatl.helper.types import AnyStr
from java.lang import CharSequence, Comparable, Enum, Object
from java.time.chrono import ChronoLocalDateTime, ChronoZonedDateTime
from java.time.format import DateTimeFormatter, TextStyle
from java.time.temporal import (
    Temporal,
    TemporalAccessor,
    TemporalAdjuster,
    TemporalUnit,
)
from java.util import Locale

class Clock(Object):
    @staticmethod
    def offset(baseClock: Instant, offsetDuration: ZoneId) -> Clock: ...
    @staticmethod
    def systemDefaultZone() -> Clock: ...
    @staticmethod
    def systemUTC() -> Clock: ...
    @staticmethod
    def tick(baseClock: Clock, tickDuration: Duration) -> Clock: ...
    @staticmethod
    def tickMillis(zone: ZoneId) -> Clock: ...
    @staticmethod
    def tickMinutes(zone: ZoneId) -> Clock: ...
    @staticmethod
    def tickSeconds(zone: ZoneId) -> Clock: ...

class DayOfWeek(Enum, TemporalAccessor, TemporalAdjuster):
    FRIDAY: DayOfWeek
    MONDAY: DayOfWeek
    SATURDAY: DayOfWeek
    SUNDAY: DayOfWeek
    THURSDAY: DayOfWeek
    TUESDAY: DayOfWeek
    WEDNESDAY: DayOfWeek
    def getValue(self) -> int: ...
    def minus(self, days: long) -> DayOfWeek: ...
    @staticmethod
    def of(dayOfWeek: int) -> DayOfWeek: ...
    def plus(self, days: long) -> DayOfWeek: ...
    @staticmethod
    def values() -> List[DayOfWeek]: ...

class Duration(Object):
    ZERO: Duration
    def toDays(self) -> long: ...
    def toDaysPart(self) -> long: ...
    def toHours(self) -> long: ...
    def toHoursPart(self) -> int: ...
    def toMillis(self) -> long: ...
    def toMillisPart(self) -> int: ...
    def toMinutes(self) -> long: ...
    def toMinutesPart(self) -> int: ...
    def toNanos(self) -> long: ...
    def toNanosPart(self) -> int: ...
    def toSeconds(self) -> long: ...
    def toSecondsPart(self) -> int: ...

class Instant(Object):
    EPOCH: Instant
    MAX: Instant
    MIN: Instant
    @staticmethod
    def now(clock: Optional[Clock] = ...) -> Instant: ...
    @staticmethod
    def ofEpochMilli(epochMilli: long) -> Instant: ...
    @staticmethod
    def ofEpochSecond(
        epochSecond: long, nanoAdjustment: Optional[long] = ...
    ) -> Instant: ...
    @staticmethod
    def parse(text: CharSequence) -> Instant: ...

class LocalDate(Object, Temporal, TemporalAdjuster, Comparable):
    EPOCH: LocalDate
    MAX: LocalDate
    MIN: LocalDate
    def compareTo(self, o: Any) -> int: ...
    def until(self, endExclusive: Temporal, unit: TemporalUnit) -> long: ...
    def atStartOfDay(self, zone: ZoneId) -> LocalDateTime: ...
    def atTime(self, *args: Any) -> Union[LocalDateTime, OffsetDateTime]: ...
    @staticmethod
    def now(clock: Optional[Clock] = ...) -> LocalDate: ...
    @staticmethod
    def of(year: int, month: int, dayOfMonth: int) -> LocalDate: ...
    @staticmethod
    def parse(text: CharSequence) -> LocalDate: ...

class LocalDateTime(Object, ChronoLocalDateTime):
    MAX: LocalDateTime
    MIN: LocalDateTime
    def atOffset(self, offset: ZoneOffset) -> OffsetDateTime: ...
    def atZone(self, zone: ZoneId) -> ZonedDateTime: ...
    def toLocalDate(self) -> LocalDate: ...
    def toLocalTime(self) -> LocalTime: ...
    def until(self, endExclusive: Temporal, unit: TemporalUnit) -> long: ...
    def adjustInto(self, temporal: Temporal) -> Temporal: ...
    def compareTo(self, o: Any) -> int: ...

class LocalTime(Object, Temporal, TemporalAdjuster, Comparable):
    MAX: LocalTime
    MIDNIGHT: LocalTime
    MIN: LocalTime
    NOON: LocalTime
    def adjustInto(self, temporal: Temporal) -> Temporal: ...
    def atDate(self, date: LocalDate) -> LocalDateTime: ...
    def compareTo(self, o: Any) -> int: ...
    @staticmethod
    def now(clock: Optional[Clock] = ...) -> LocalTime: ...
    @staticmethod
    def of(
        hour: int, minute: int, second: Optional[int] = ..., nano: Optional[int] = ...
    ) -> LocalTime: ...
    @staticmethod
    def parse(text: CharSequence) -> LocalTime: ...
    def until(self, endExclusive: Temporal, unit: TemporalUnit) -> long: ...

class Month(Enum, TemporalAccessor, TemporalAdjuster):
    JANUARY: Month
    FEBRUARY: Month
    MARCH: Month
    APRIL: Month
    MAY: Month
    JUNE: Month
    JULY: Month
    AUGUST: Month
    SEPTEMBER: Month
    OCTOBER: Month
    NOVEMBER: Month
    DECEMBER: Month
    def adjustInto(self, temporal: Temporal) -> Temporal: ...
    def firstDayOfYear(self, leapYear: bool) -> int: ...
    def firstMonthOfQuarter(self) -> Month: ...
    def getDisplayName(self, style: TextStyle, locale: Locale) -> AnyStr: ...
    def getValue(self) -> int: ...
    def length(self, leapYear: bool) -> int: ...
    def maxLength(self) -> int: ...
    def minLength(self) -> int: ...
    def minus(self, months: long) -> Month: ...
    @staticmethod
    def of(month: int) -> Month: ...
    def plus(self, months: long) -> Month: ...
    @staticmethod
    def values() -> List[Month]: ...

class OffsetDateTime(Object, Temporal, TemporalAdjuster, Comparable):
    MAX: OffsetDateTime
    MIN: OffsetDateTime
    def adjustInto(self, temporal: Temporal) -> Temporal: ...
    def atZoneSameInstant(self, zone: ZoneId) -> ZonedDateTime: ...
    def compareTo(self, o: Any) -> int: ...
    def toLocalDateTime(self) -> LocalDateTime: ...
    def until(self, endExclusive: Temporal, unit: TemporalUnit) -> long: ...

class ZoneId(Object):
    SHORT_IDS: Dict[AnyStr, AnyStr]
    @staticmethod
    def getAvailableZoneIds() -> Set[AnyStr]: ...
    @staticmethod
    def of(
        zoneId: AnyStr, aliasMap: Optional[Dict[AnyStr, AnyStr]] = ...
    ) -> ZoneId: ...
    @staticmethod
    def ofOffset(prefix: AnyStr, offset: ZoneOffset) -> ZoneId: ...
    @staticmethod
    def systemDefault() -> ZoneId: ...

class ZoneOffset(Object):
    MAX: ZoneOffset
    MIN: ZoneOffset
    UTC: ZoneOffset
    @staticmethod
    def of(offsetId: AnyStr) -> ZoneOffset: ...
    @staticmethod
    def ofHours(hours: int) -> ZoneOffset: ...
    @staticmethod
    def ofHoursMinutes(hours: int, minutes: int) -> ZoneOffset: ...
    @staticmethod
    def ofHoursMinutesSeconds(hours: int, minutes: int, seconds: int) -> ZoneOffset: ...
    @staticmethod
    def ofTotalSeconds(totalSeconds: int) -> ZoneOffset: ...

class ZonedDateTime(Object, ChronoZonedDateTime):
    def toLocalDateTime(self) -> LocalDateTime: ...
    def withEarlierOffsetAtOverlap(self) -> ZonedDateTime: ...
    def withLaterOffsetAtOverlap(self) -> ZonedDateTime: ...
    def withZoneSameInstant(self, zone: ZoneId) -> ZonedDateTime: ...
    def withZoneSameLocal(self, zone: ZoneId) -> ZonedDateTime: ...
    def until(self, endExclusive: Temporal, unit: TemporalUnit) -> long: ...
    def compareTo(self, o: Any) -> int: ...
    def getDayOfMonth(self) -> int: ...
    def getDayOfWeek(self) -> DayOfWeek: ...
    def getDayOfYear(self) -> int: ...
    def getHour(self) -> int: ...
    def getMinute(self) -> int: ...
    def getMonth(self) -> Month: ...
    def getMonthValue(self) -> int: ...
    def getNano(self) -> int: ...
    def getOffset(self) -> ZoneOffset: ...
    def getSecond(self) -> int: ...
    def getYear(self) -> int: ...
    def getZone(self) -> ZoneId: ...
    def minusDays(self, days: int) -> ZonedDateTime: ...
    def minusHours(self, hours: int) -> ZonedDateTime: ...
    def minusMinutes(self, minutes: int) -> ZonedDateTime: ...
    def minusMonths(self, months: int) -> ZonedDateTime: ...
    def minusNanos(self, nanos: int) -> ZonedDateTime: ...
    def minusSeconds(self, seconds: int) -> ZonedDateTime: ...
    def minusWeeks(self, weeks: int) -> ZonedDateTime: ...
    def minusYears(self, years: int) -> ZonedDateTime: ...
    @staticmethod
    def now(arg: Optional[Union[Clock, ZoneId]] = ...) -> ZonedDateTime: ...
    @staticmethod
    def of(*args: Any) -> ZonedDateTime: ...
    @staticmethod
    def ofInstant(*args: Any) -> ZonedDateTime: ...
    @staticmethod
    def ofLocal(
        localDateTime: LocalDateTime, zone: ZoneId, preferredOffset: ZoneOffset
    ) -> ZonedDateTime: ...
    @staticmethod
    def ofStrict(
        localDateTime: LocalDateTime, offset: ZoneOffset, zone: ZoneId
    ) -> ZonedDateTime: ...
    @staticmethod
    def parse(
        text: CharSequence, formatter: Optional[DateTimeFormatter] = ...
    ) -> ZonedDateTime: ...
