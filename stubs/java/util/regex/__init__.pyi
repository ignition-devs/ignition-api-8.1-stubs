from typing import Any, List, Optional, Union

from java.lang import CharSequence as CharSequence
from java.lang import Object as Object
from java.lang import String as String
from java.lang import StringBuffer as StringBuffer
from java.lang import StringBuilder as StringBuilder
from java.util.function import Function as Function
from java.util.function import Predicate as Predicate

class MatchResult:
    def end(self, group: Optional[int] = ...) -> int: ...
    def group(self, group: Optional[int] = ...) -> String: ...
    def groupCount(self) -> int: ...
    def start(self, group: Optional[int] = ...) -> int: ...

class Matcher(Object, MatchResult):
    def appendReplacement(
        self, sb: Union[StringBuffer, StringBuilder], replacement: String
    ) -> Matcher: ...
    def appendTail(
        self, sb: Union[StringBuffer, StringBuilder]
    ) -> Union[StringBuffer, StringBuilder]: ...
    def end(self, group: Optional[int] = ...) -> int: ...
    def find(self, start: Optional[int] = ...) -> bool: ...
    def group(self, group: Optional[Union[int, String]] = ...) -> String: ...
    def groupCount(self) -> int: ...
    def hasAnchoringBounds(self) -> bool: ...
    def hasTransparentBounds(self) -> bool: ...
    def hitEnd(self) -> bool: ...
    def lookingAt(self) -> bool: ...
    def matches(self) -> bool: ...
    def pattern(self) -> Pattern: ...
    @staticmethod
    def quoteReplacement(s: String) -> String: ...
    def region(self, start: int, end: int) -> Matcher: ...
    def regionEnd(self) -> int: ...
    def regionStart(self) -> int: ...
    def replaceAll(self, arg: Union[Function, String]) -> String: ...
    def replaceFirst(self, arg: Union[Function, String]) -> String: ...
    def requireEnd(self) -> bool: ...
    def reset(self, input: Optional[CharSequence] = ...) -> Matcher: ...
    def results(self) -> Any: ...
    def start(self, group: Optional[int] = ...) -> int: ...
    def toMatchResult(self) -> MatchResult: ...
    def useAnchoringBounds(self, b: bool) -> Matcher: ...
    def usePattern(self, newPattern: Pattern) -> Matcher: ...
    def useTransparentBounds(self, b: bool) -> Matcher: ...

class Pattern(Object):
    CANON_EQ: int
    CASE_INSENSITIVE: int
    COMMENTS: int
    DOTALL: int
    LITERAL: int
    MULTILINE: int
    UNICODE_CASE: int
    UNICODE_CHARACTER_CLASS: int
    UNIX_LINES: int
    def asMatchPredicate(self) -> Predicate: ...
    def asPredicate(self) -> Predicate: ...
    @staticmethod
    def compile(regex: String, flags: Optional[int] = ...) -> Pattern: ...
    def flags(self) -> int: ...
    def matcher(self, input: CharSequence) -> Matcher: ...
    @staticmethod
    def matches(regex: String, input: CharSequence) -> bool: ...
    def pattern(self) -> String: ...
    @staticmethod
    def quote(s: String) -> String: ...
    def split(
        self, input: CharSequence, limit: Optional[int] = ...
    ) -> List[String]: ...
    def splitAsStream(self, input: CharSequence) -> Any: ...