from typing import Any, Callable, Dict, List, Optional

from com.inductiveautomation.ignition.common.script.builtin.http import JythonHttpClient
from java.lang import String

def getExternalIpAddress() -> String: ...
def getHostName() -> String: ...
def getIpAddress() -> String: ...
def getRemoteServers(runningOnly: Optional[bool] = ...) -> List[String]: ...
def httpClient(
    timeout: int = ...,
    bypass_cert_validation: bool = ...,
    username: Optional[String] = ...,
    password: Optional[String] = ...,
    proxy: Optional[String] = ...,
    cookie_policy: String = ...,
    redirect_policy: String = ...,
    version: String = ...,
    customizer: Optional[Callable[..., Any]] = ...,
) -> JythonHttpClient: ...
def httpDelete(
    url: String,
    contentType: Optional[String] = ...,
    connectTimeout: int = ...,
    readTimeout: int = ...,
    username: Optional[String] = ...,
    password: Optional[String] = ...,
    headerValues: Optional[Dict[String, String]] = ...,
    bypassCertValidation: bool = ...,
) -> String: ...
def httpGet(
    url: String,
    connectTimeout: int = ...,
    readTimeout: int = ...,
    username: Optional[String] = ...,
    password: Optional[String] = ...,
    headerValues: Optional[Dict[String, String]] = ...,
    bypassCertValidation: Optional[bool] = ...,
    useCaches: bool = ...,
    throwOnError: bool = ...,
) -> String: ...
def httpPost(url: String, *args: Any, **kwargs: Any) -> String: ...
def httpPut(url: String, *args: Any, **kwargs: Any) -> String: ...
def openURL(url: String, useApplet: Optional[bool] = ...) -> None: ...
def sendEmail(
    smtp: Optional[String] = ...,
    fromAddr: String = ...,
    subject: Optional[String] = ...,
    body: Optional[String] = ...,
    html: bool = ...,
    to: Optional[List[String]] = ...,
    attachmentNames: Optional[List[object]] = ...,
    attachmentData: Optional[List[object]] = ...,
    timeout: int = ...,
    username: Optional[String] = ...,
    password: Optional[String] = ...,
    priority: String = ...,
    smtpProfile: Optional[String] = ...,
    cc: Optional[List[String]] = ...,
    bcc: Optional[List[String]] = ...,
    retries: int = ...,
    replyTo: Optional[List[String]] = ...,
) -> None: ...
