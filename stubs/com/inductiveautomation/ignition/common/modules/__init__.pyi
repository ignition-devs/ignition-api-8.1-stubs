from typing import List, Mapping, Optional

from com.inductiveautomation.ignition.common.licensing import LicenseState
from com.inductiveautomation.ignition.common.model import Version
from com.inductiveautomation.ignition.common.util import Platform
from dev.coatl.helper.types import AnyStr
from java.lang import Object

class ModuleInfo(Object):
    def getCrc(self) -> long: ...
    def getDependencies(
        self, scope: Optional[int] = ...
    ) -> List[ModuleInfo.ModuleDependency]: ...
    def getDescription(self) -> AnyStr: ...
    def getDocumentationRoot(self) -> AnyStr: ...
    def getExports(self) -> List[ModuleInfo.JarInfo]: ...
    def getHooks(self) -> Mapping[int, AnyStr]: ...
    def getId(self) -> AnyStr: ...
    def getInstallPath(self) -> AnyStr: ...
    def getJars(self) -> List[ModuleInfo.JarInfo]: ...
    def getLibsRequired(self) -> List[ModuleInfo.LibraryInfo]: ...
    def getLicenseFile(self) -> AnyStr: ...
    def getLicenseState(self) -> LicenseState: ...
    def getName(self) -> AnyStr: ...
    def getRequiredFrameworkVersion(self) -> int: ...
    def getRequiredIgnitionVersion(self) -> Version: ...
    def getVendorContactInfo(self) -> AnyStr: ...
    def getVendorId(self) -> int: ...
    def getVendorName(self) -> AnyStr: ...
    def getVersion(self) -> Version: ...
    def isFree(self) -> bool: ...
    def isMakerEditionCompatible(self) -> bool: ...
    def isSelfSigned(self) -> bool: ...
    def isTrialMode(self) -> bool: ...
    @staticmethod
    def newBuilder() -> ModuleInfo.Builder: ...
    def setCrc(self, crc: long) -> None: ...
    def setFree(self) -> None: ...
    def setInstallPath(self, installPath: AnyStr) -> None: ...
    def setLicenseState(self, newState: LicenseState) -> None: ...
    def setMakerEditionCompatible(self) -> None: ...
    def setSelfSigned(self) -> None: ...
    def setVendorInfo(
        self, vendorId: int, vendorName: AnyStr, vendorContactInfo: AnyStr
    ) -> None: ...
    @staticmethod
    def setDependencyOrder(
        list_: List[ModuleInfo], scope: int, reverse: bool
    ) -> List[ModuleInfo]: ...
    def toXML(self) -> AnyStr: ...

    class Builder(Object):
        def __init__(self) -> None: ...
        def addDependency(
            self, dependency: ModuleInfo.ModuleDependency
        ) -> ModuleInfo.Builder: ...
        def build(self) -> ModuleInfo: ...
        def setDependencies(
            self, dependencies: List[ModuleInfo.ModuleDependency]
        ) -> ModuleInfo.Builder: ...
        def setDescription(self, description: AnyStr) -> ModuleInfo.Builder: ...
        def setExports(
            self, exports: List[ModuleInfo.JarInfo]
        ) -> ModuleInfo.Builder: ...
        def setHooks(self, hooks: Mapping[int, AnyStr]) -> ModuleInfo.Builder: ...
        def setId(self, id_: AnyStr) -> ModuleInfo.Builder: ...
        def setJars(self, jars: List[ModuleInfo.JarInfo]) -> ModuleInfo.Builder: ...
        def setLicenseFile(self, licenseFilename: AnyStr) -> ModuleInfo.Builder: ...
        def setName(self, name: AnyStr) -> ModuleInfo.Builder: ...
        def setRequire(
            self, require: List[ModuleInfo.LibraryInfo]
        ) -> ModuleInfo.Builder: ...
        def setRequiredFrameworkVersion(
            self, requiredFrameworkVersion: int
        ) -> ModuleInfo.Builder: ...
        def setRequiredIgnitionVersion(
            self, requiredIgnitionVersion: Version
        ) -> ModuleInfo.Builder: ...
        def setSelfSigned(self, selfSigned: bool) -> ModuleInfo.Builder: ...
        def setVendor(
            self, id_: int, name: AnyStr, contactInfo: AnyStr
        ) -> ModuleInfo.Builder: ...
        def setVersion(self, version: Version) -> ModuleInfo.Builder: ...

    class JarInfo(Object):
        def __init__(
            self,
            scope: int,
            path: AnyStr,
            requiredOs: AnyStr = ...,
            requiredArch: AnyStr = ...,
        ) -> None: ...
        def getPath(self) -> AnyStr: ...
        def getRequiredArch(self) -> AnyStr: ...
        def getRequiredOS(self) -> AnyStr: ...
        def getScope(self) -> int: ...
        def isNativeLib(self) -> bool: ...
        def isRequiredArchitecture(self, arch: Platform.Architecture) -> bool: ...
        def isRequiredOS(self, os: Platform.OperatingSystem) -> bool: ...

    class LibraryInfo(Object):
        def getName(self) -> AnyStr: ...
        def getScope(self) -> int: ...
        def setName(self, name: AnyStr) -> None: ...
        def setScope(self, scope: int) -> None: ...

    class ModuleDependency(Object):
        def getModuleId(self) -> AnyStr: ...
        def getScope(self) -> int: ...
        def getVersion(self) -> Version: ...
