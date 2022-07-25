from typing import Any, Dict, List, Tuple

from java.lang import String

def addConnection(
    name: String,
    description: String,
    discoveryUrl: String,
    endpointUrl: String,
    securityPolicy: String,
    securityMode: String,
    settings: Dict[String, Any],
) -> None: ...
def callMethod(
    connectionName: String, objectId: String, methodId: String, inputs: List[String]
) -> Tuple[Any, Any, Any]: ...
def removeConnection(name: String) -> bool: ...
