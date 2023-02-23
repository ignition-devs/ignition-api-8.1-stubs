from typing import List

from com.inductiveautomation.ignition.common.functional import FragileRunnable
from dev.thecesrom.helper.types import AnyStr
from java.lang import Object
from java.util import Locale
from java.util.function import Consumer

class MessageInterface:
    def addMessageReceiver(self, protocol, rcv) -> None: ...
    def sendCall(self, protocol, scope, msg) -> None: ...
    def sendMessage(self, protocol, scope, msg) -> None: ...

class MessageReceiver:
    def receiveCall(self, msg) -> None: ...

class UIResponse(Object):
    errors: List[AnyStr]
    infos: List[AnyStr]
    locale: Locale
    warns: List[AnyStr]
    def __init__(self, locale: Locale) -> None: ...
    def attempt(self, method: FragileRunnable) -> None: ...
    def error(self, message: AnyStr, *args: Object) -> None: ...
    def getErrors(self) -> List[AnyStr]: ...
    def getInfos(self) -> List[AnyStr]: ...
    def getLocale(self) -> Locale: ...
    def getWarns(self) -> List[AnyStr]: ...
    def info(self, message: AnyStr, *args: Object) -> None: ...
    def warn(self, message: AnyStr, *args: Object) -> None: ...
    @staticmethod
    def wrap(locale: Locale, fx: Consumer) -> UIResponse: ...
