from typing import Optional

from com.inductiveautomation.ignition.common.gson import Gson as Gson
from com.inductiveautomation.ignition.common.gson import JsonObject as JsonObject
from com.inductiveautomation.ignition.common.jsonschema import JsonSchema as JsonSchema
from com.inductiveautomation.ignition.common.util import LoggerEx as LoggerEx
from java.lang import Object
from java.lang import String as String
from java.util.function import Consumer

class PerspectiveModule(Object):
    LOG_PREFIX: String
    META_SCHEMA: JsonSchema
    MODULE_ID: String
    SESSION_PROPS_SCHEMA: JsonSchema
    VIEW_SCHEMA: JsonSchema
    @staticmethod
    def createPerspectiveCompatibleGson(
        customize: Optional[Consumer] = ...,
    ) -> Gson: ...
    @staticmethod
    def defaultMetaProps() -> JsonObject: ...
    @staticmethod
    def defaultSessionProps() -> JsonObject: ...
    @staticmethod
    def defaultViewProps() -> JsonObject: ...
    @staticmethod
    def getLogger(name: String) -> LoggerEx: ...
