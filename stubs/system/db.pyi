from typing import Any, List, Optional

from com.inductiveautomation.ignition.common import BasicDataset
from com.inductiveautomation.ignition.common.script.builtin import (
    DatasetUtilities,
    SProcCall,
)
from java.lang import String
from java.util import Date
from javax.swing import JComponent

BIT: int
REAL: int
LONGVARCHAR: int
LONGVARBINARY: int
TINYINT: int
DOUBLE: int
DATE: int
NULL: int
SMALLINT: int
NUMERIC: int
TIME: int
ROWID: int
INTEGER: int
DECIMAL: int
TIMESTAMP: int
CLOB: int
BIGINT: int
CHAR: int
BINARY: int
NCLOB: int
FLOAT: int
VARCHAR: int
VARBINARY: int
BLOB: int
NCHAR: int
NVARCHAR: int
LONGNVARCHAR: int
BOOLEAN: int
ORACLE_CURSOR: int
DISTINCT: int
STRUCT: int
REF: int
JAVA_OBJECT: int
SQLXML: int
ARRAY: int
DATALINK: int
OTHER: int
READ_COMMITTED: int
READ_UNCOMMITTED: int
REPEATABLE_READ: int
SERIALIZABLE: int

def addDatasource(
    jdbcDriver: String,
    name: String,
    description: String = ...,
    connectUrl: Optional[String] = ...,
    username: Optional[String] = ...,
    password: Optional[String] = ...,
    props: Optional[String] = ...,
    validationQuery: Optional[String] = ...,
    maxConnections: int = ...,
) -> None: ...
def beginNamedQueryTransaction(*args: Any) -> String: ...
def beginTransaction(
    database: Optional[String] = ...,
    isolationLevel: Optional[int] = ...,
    timeout: Optional[int] = ...,
) -> String: ...
def clearAllNamedQueryCaches(project: Optional[String] = ...) -> None: ...
def clearNamedQueryCache(*args: String) -> None: ...
def closeTransaction(tx: String) -> None: ...
def commitTransaction(tx: String) -> None: ...
def createSProcCall(
    procedureName: String,
    database: String = ...,
    tx: Optional[String] = ...,
    skipAudit: bool = ...,
) -> SProcCall: ...
def dateFormat(date: Date, formatPattern: String) -> String: ...
def execSProcCall(callContext: SProcCall) -> None: ...
def getConnectionInfo(name: Optional[String] = ...) -> BasicDataset: ...
def getConnections() -> BasicDataset: ...
def refresh(component: JComponent, propertyName: String) -> bool: ...
def removeDatasource(name: String) -> None: ...
def rollbackTransaction(tx: String) -> None: ...
def runNamedQuery(*args: Any) -> Any: ...
def runPrepQuery(
    query: String, args: List[Any], database: String = ..., tx: Optional[String] = ...
) -> DatasetUtilities.PyDataSet: ...
def runPrepUpdate(
    query: String,
    args: List[Any],
    database: String = ...,
    tx: Optional[String] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def runQuery(
    query: String, database: String = ..., tx: Optional[String] = ...
) -> DatasetUtilities.PyDataSet: ...
def runSFNamedQuery(*args: Any) -> bool: ...
def runSFPrepUpdate(
    query: String, args: List[Any], datasources: List[String]
) -> bool: ...
def runSFUpdateQuery(query: String, datasources: List[String]) -> bool: ...
def runScalarPrepQuery(
    query: String, args: List[Any], database: String = ..., tx: Optional[String] = ...
) -> Any: ...
def runScalarQuery(
    query: String, database: Optional[String] = ..., tx: Optional[String] = ...
) -> Any: ...
def runUpdateQuery(
    query: String,
    database: String = ...,
    tx: Optional[String] = ...,
    getKey: bool = ...,
    skipAudit: bool = ...,
) -> int: ...
def setDatasourceConnectURL(name: String, connectUrl: String) -> None: ...
def setDatasourceEnabled(name: String, enabled: bool) -> None: ...
def setDatasourceMaxConnections(name: String, maxConnections: int) -> None: ...
