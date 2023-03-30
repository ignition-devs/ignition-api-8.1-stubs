from copy import PyStringMap as PyStringMap  # noqa: F401
from typing import Any, Iterable, Iterator, List, Mapping, Optional, Tuple, Union

import java.util
from dev.thecesrom.helper.types import AnyStr
from enum import Enum
from java.io import PrintWriter
from java.lang import Class, Object, RuntimeException, StringBuilder
from org.python.expose import TypeBuilder

class PyObject(Object):
    gcMonitorGlobal: bool
    TYPE: PyType
    def __init__(self, objtype: Optional[PyType] = ...) -> None: ...
    def __abs__(self) -> PyObject: ...
    def __add__(self, other: PyObject) -> PyObject: ...
    def __and__(self, other: PyObject) -> PyObject: ...
    def __call__(self, *args: Any, **kwargs: Any) -> PyObject: ...
    def __coerce__(self, pyo: PyObject) -> PyObject: ...
    def __coerce_ex__(self, o: PyObject) -> Object: ...
    def __complex__(self) -> complex: ...
    def __contains__(self, o: PyObject) -> bool: ...
    def __delete__(self, obj: PyObject) -> None: ...
    def __delitem__(self, key: PyObject) -> None: ...
    def __delslice__(
        self, start: PyObject, stop: PyObject, step: Optional[PyObject] = ...
    ) -> None: ...
    def __dir__(self) -> PyObject: ...
    def __div__(self, other: PyObject) -> PyObject: ...
    def __ensure_finalizer__(self) -> None: ...
    def __findattr__(self, name: str) -> PyObject: ...
    def __findattr_ex__(self, name: str) -> PyObject: ...
    def __finditem__(self, key: str) -> PyObject: ...
    def __float__(self) -> float: ...
    def __floordiv__(self, other: PyObject) -> PyObject: ...
    def __get__(self, obj: PyObject, type: PyObject) -> PyObject: ...
    def __getattr__(self, name: str) -> PyObject: ...
    def __getitem__(self, key: Union[int, PyObject]) -> PyObject: ...
    def __getnewargs__(self) -> Tuple[Any, ...]: ...
    def __getslice__(
        self, start: PyObject, stop: PyObject, step: Optional[PyObject] = ...
    ) -> None: ...
    def __hex__(self) -> str: ...
    def __iadd__(self, other: PyObject) -> PyObject: ...
    def __iand__(self, other: PyObject) -> PyObject: ...
    def __idiv__(self, other: PyObject) -> PyObject: ...
    def __idivmod__(self, other: PyObject) -> PyObject: ...
    def __ifloordiv__(self, other: PyObject) -> PyObject: ...
    def __ilshift__(self, other: PyObject) -> PyObject: ...
    def __imod__(self, other: PyObject) -> PyObject: ...
    def __imul__(self, other: PyObject) -> PyObject: ...
    def __index__(self) -> PyObject: ...
    def __int__(self) -> PyObject: ...
    def __invert__(self) -> PyObject: ...
    def __ior__(self, other: PyObject) -> PyObject: ...
    def __ipow__(
        self, other: PyObject, dummy: Optional[PyObject] = ...
    ) -> PyObject: ...
    def __irshift__(self, other: PyObject) -> PyObject: ...
    def __isub__(self, other: PyObject) -> PyObject: ...
    def __iter__(self) -> Iterator[Any]: ...
    def __iternext__(self) -> PyObject: ...
    def __itruediv__(self, other: PyObject) -> PyObject: ...
    def __ixor__(self, other: PyObject) -> PyObject: ...
    def __le__(self, other: PyObject) -> PyObject: ...
    def __long__(self) -> PyObject: ...
    def __lshift__(self, other: PyObject) -> PyObject: ...
    def __mod__(self, other: PyObject) -> PyObject: ...
    def __mul__(self, other: PyObject) -> PyObject: ...
    def __neg__(self) -> PyObject: ...
    def __nonzero__(self) -> PyObject: ...
    def __not__(self) -> PyObject: ...
    def __oct__(self) -> PyObject: ...
    def __or__(self, other: PyObject) -> PyObject: ...
    def __pos__(self) -> PyObject: ...
    def __pow__(self, o2: PyObject, o3: Optional[PyObject] = ...) -> PyObject: ...
    def __radd__(self, other: PyObject) -> PyObject: ...
    def __rand__(self, other: PyObject) -> PyObject: ...
    def __rdiv__(self, other: PyObject) -> PyObject: ...
    def __rdivmod__(self, other: PyObject) -> PyObject: ...
    def __rfloordiv__(self, other: PyObject) -> PyObject: ...
    def __rlshift__(self, other: PyObject) -> PyObject: ...
    def __rmod__(self, other: PyObject) -> PyObject: ...
    def __rmul__(self, other: PyObject) -> PyObject: ...
    def __ror__(self, other: PyObject) -> PyObject: ...
    def __rpow__(self, other: PyObject) -> PyObject: ...
    def __rrshift__(self, other: PyObject) -> PyObject: ...
    def __rshift__(self, other: PyObject) -> PyObject: ...
    def __rsub__(self, other: PyObject) -> PyObject: ...
    def __rtruediv__(self, other: PyObject) -> PyObject: ...
    def __rxor__(self, other: PyObject) -> PyObject: ...
    def __set__(self, obj: PyObject, value: PyObject) -> None: ...
    def __setitem__(self, key: Union[int, PyObject, str], value: PyObject) -> None: ...
    def __setslice__(self, *args: Any) -> None: ...
    def __sub__(self, other: PyObject) -> PyObject: ...
    def __tojava__(self, c: Class) -> Object: ...
    def __truediv__(self, other: PyObject) -> PyObject: ...
    def __trunc__(self) -> PyObject: ...
    def __unicode__(self) -> unicode: ...
    def __xor__(self, other: PyObject) -> PyObject: ...
    def asDouble(self) -> float: ...
    def asIndex(self, err: Optional[PyObject] = ...) -> int: ...
    def asInt(self, index: Optional[int] = ...) -> int: ...
    def asIterable(self) -> Iterable[PyObject]: ...
    def asLong(self, index: Optional[int] = ...) -> long: ...
    def asName(self, arg: Union[int, PyObject]) -> AnyStr: ...
    def asString(self, index: Optional[int] = ...) -> AnyStr: ...
    def asStringOrNull(self, index: Optional[int] = ...) -> AnyStr: ...
    def bit_length(self) -> int: ...
    def conjugate(self) -> PyObject: ...
    def delDict(self) -> None: ...
    def delType(self) -> None: ...
    def dispatch__init__(self, *args: Any, **kwargs: Any) -> None: ...
    def fastGetClass(self) -> PyObject: ...
    def fastGetDict(self) -> PyObject: ...
    def getDict(self) -> PyObject: ...
    def getType(self) -> PyType: ...
    def implementsDescrDelete(self) -> bool: ...
    def implementsDescrGet(self) -> bool: ...
    def implementsDescrSet(self) -> bool: ...
    def invoke(self, *args: Any, **kwargs: Any) -> PyObject: ...
    def isCallable(self) -> bool: ...
    def isDataDescr(self) -> bool: ...
    def isIndex(self) -> bool: ...
    def isInteger(self) -> bool: ...
    def isMappingType(self) -> bool: ...
    def isNumberType(self) -> bool: ...
    def isSequenceType(self) -> bool: ...
    def noAttributeError(self, name: AnyStr) -> None: ...
    @staticmethod
    def object___subclasshook__(type: PyType, subclass: PyObject) -> PyObject: ...
    def readonlyAttributeError(self, name: AnyStr) -> None: ...
    def setDict(self, newDict: PyObject) -> None: ...
    def setType(self, type: PyType) -> None: ...

class CodeFlag(Enum):
    CO_FUTURE_ABSOLUTE_IMPORT: int
    CO_FUTURE_DIVISION: int
    CO_FUTURE_PRINT_FUNCTION: int
    CO_FUTURE_UNICODE_LITERALS: int
    CO_FUTURE_WITH_STATEMENT: int
    CO_GENERATOR: int
    CO_GENERATOR_ALLOWED: int
    CO_NESTED: int
    CO_NEWLOCALS: int
    CO_OPTIMIZED: int
    CO_VARARGS: int
    CO_VARKEYWORDS: int
    flag: int
    def isFlagBitSetIn(self, flags: int) -> bool: ...
    @staticmethod
    def valueOf(name: AnyStr) -> CodeFlag: ...
    @staticmethod
    def values() -> List[CodeFlag]: ...

class CompilerFlags(Object):
    dont_imply_dedent: bool
    encoding: AnyStr
    only_ast: bool
    PyCF_DONT_IMPLY_DEDENT: int
    PyCF_ONLY_AST: int
    PyCF_SOURCE_IS_UTF8: int
    source_is_utf8: bool
    def __init__(self, co_flags: Optional[int] = ...) -> None: ...
    def combine(self, flags: Union[CompilerFlags, int]) -> CompilerFlags: ...
    @staticmethod
    def getCompilerFlags(
        flags: Union[CompilerFlags, int], frame: PyFrame
    ) -> CompilerFlags: ...
    def isFlagSet(self, flag: CodeFlag) -> bool: ...
    def toBits(self) -> int: ...

class PyCode(PyObject):
    co_name: AnyStr
    def call(self, *args: Any) -> None: ...

class PyBaseCode(PyCode):
    co_argcount: int
    co_cellvars: List[AnyStr]
    co_filename: AnyStr
    co_firstlineno: int
    co_flags: CompilerFlags
    co_freevars: List[AnyStr]
    co_nlocals: int
    co_varnames: List[AnyStr]
    jy_npurecell: int
    varargs: bool
    varkwargs: bool
    def getCompilerFlags(self) -> CompilerFlags: ...
    def hasFreevars(self) -> bool: ...

class PyBuiltinCallable(PyObject):
    def bind(self, o: PyObject) -> PyBuiltinCallable: ...
    def fastGetName(self) -> PyObject: ...
    def getDoc(self) -> AnyStr: ...
    def getModule(self) -> PyObject: ...
    def getSelf(self) -> PyObject: ...
    def makeCall(self) -> PyObject: ...
    def setInfo(self, info: PyBuiltinCallable.Info) -> None: ...

    class Info:
        def getMaxargs(self) -> int: ...
        def getMinargs(self) -> int: ...
        def getName(self) -> AnyStr: ...
        def unexpectedCall(self, nargs: int, keywords: bool) -> PyException: ...

class PyBuiltinMethod(PyBuiltinCallable):
    def bind(self, o: PyObject) -> PyBuiltinCallable: ...
    def makeDescriptor(self, t: PyType) -> PyMethodDescr: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...

class PyCell(PyObject):
    ob_ref: PyObject
    def __init__(self) -> None: ...
    def getCellContents(self) -> PyObject: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...

class PyDescriptor(PyObject, PyBuiltinCallable.Info):
    def __init__(self, t: PyType, func: PyBuiltinCallable) -> None: ...
    def getDoc(self) -> AnyStr: ...
    def getMaxargs(self) -> int: ...
    def getMinargs(self) -> int: ...
    def getName(self) -> AnyStr: ...
    def getObjClass(self) -> PyObject: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...
    def unexpectedCall(self, nargs: int, keywords: bool) -> PyException: ...

class PyException(RuntimeException):
    traceback: Optional[PyTraceback]
    type: Optional[PyObject]
    value: Optional[Union[PyObject, AnyStr]]
    def __init__(
        self,
        type_: Optional[PyObject] = ...,
        value: Optional[Union[PyObject, AnyStr]] = ...,
        traceback: Optional[PyTraceback] = ...,
    ) -> None: ...
    @staticmethod
    def doRaise(
        type_: PyObject, value: PyObject, traceback: PyObject
    ) -> PyException: ...
    def exceptionClassName(self, obj: PyObject) -> AnyStr: ...
    def isExceptionClass(self, obj: PyObject) -> bool: ...
    def match(self, exc: PyObject) -> bool: ...
    def normalize(self) -> None: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def super__printStackTrace(self, w: PrintWriter) -> None: ...
    def tracebackHere(self, here: PyFrame, isFinally: Optional[bool] = ...) -> None: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...

class PyFrame(PyObject):
    f_back: PyFrame
    f_builtins: PyObject
    f_code: PyBaseCode
    f_env: List[PyCell]
    f_exits: List[PyObject]
    f_fastlocals: List[PyObject]
    f_globals: PyObject
    f_lasti: int
    f_lineno: int
    f_locals: PyObject
    f_ncells: int
    f_nfreevars: int
    f_savedlocals: List[Object]
    tracefunc: TraceFunction
    def __init__(self, *args: Any) -> None: ...
    def checkGeneratorInput(self) -> Object: ...
    def delglobal(self, index: AnyStr) -> None: ...
    def dellocal(self, index: Union[int, AnyStr]) -> None: ...
    def delTrace(self) -> None: ...
    def getclosure(self, index: int) -> PyObject: ...
    def getderef(self, index: int) -> PyObject: ...
    def getf_locals(self) -> PyObject: ...
    def getGeneratorInput(self) -> Object: ...
    def getglobal(self, index: AnyStr) -> PyObject: ...
    def getLine(self) -> int: ...
    def getlocal(self, index: int) -> PyObject: ...
    def getLocals(self) -> PyObject: ...
    def getname(self, index: AnyStr) -> PyObject: ...
    def getTrace(self) -> PyObject: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def setderef(self, index: int, value: PyObject) -> None: ...
    def setglobal(self, index: AnyStr, value: PyObject) -> None: ...
    def setline(self, line: int) -> None: ...
    def setlocal(self, index: Union[int, AnyStr], value: PyObject) -> None: ...
    def setTrace(self, trace: PyObject) -> None: ...
    def to_cell(self, parm_index: int, env_index: int) -> None: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...

class PyFunction(PyObject):
    def __init__(self, *args: Any) -> None: ...

class PyInteger(PyObject):
    def __init__(self, *args: Any) -> None: ...

class PyMethodDescr(PyDescriptor):
    def __init__(self, t: PyType, func: PyBuiltinCallable) -> None: ...

class PyNewWrapper(PyBuiltinMethod):
    for_type: PyType
    def __init__(self, *args: Any) -> None: ...
    def getWrappedType(self) -> PyType: ...
    def new_impl(
        self, init: bool, subtype: PyType, *args: Any, **kwargs: Any
    ) -> PyObject: ...
    def setWrappedType(self, type_: PyType) -> None: ...

class PySequence(PyObject): ...

class PySequenceList(PySequence):
    def add(self, *args: Any) -> Optional[bool]: ...
    def addAll(self, *args: Any) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, o: Object) -> bool: ...
    def containsAll(self, c: java.util.Collection) -> bool: ...
    def get(self, index: int) -> Object: ...
    def getArray(self) -> List[PyObject]: ...
    def indexOf(self, o: Object) -> int: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator: ...
    def lastIndexOf(self, o: Object) -> int: ...
    def listIterator(self, index: Optional[int] = ...) -> java.util.ListIterator: ...
    def pyadd(self, *args: Any) -> Optional[bool]: ...
    def pyget(self, index: int) -> PyObject: ...
    def pyset(self, index: int, element: PyObject) -> None: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def remove(self, *args: Any) -> Union[bool, None, Object]: ...
    def removeAll(self, c: java.util.Collection) -> bool: ...
    def retainAll(self, c: java.util.Collection) -> bool: ...
    def set(self, index: int, element: Object) -> Object: ...
    def size(self) -> int: ...
    def subList(self, fromIndex: int, toIndex: int) -> List[PyObject]: ...
    def toArray(self, a: Optional[List[Object]] = ...) -> List[Object]: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...

class PyList(PySequenceList):
    def __init__(self, *args: Any) -> None: ...
    def add(self, *args: Any) -> Optional[bool]: ...
    def addAll(self, *args: Any) -> bool: ...
    def append(self, o: PyObject) -> None: ...
    def clear(self) -> None: ...
    def contains(self, o: Object) -> bool: ...
    def containsAll(self, c: java.util.Collection) -> bool: ...
    def count(self, o: PyObject) -> int: ...
    def extend(self, o: PyObject) -> None: ...
    @staticmethod
    def fromList(list_: List[PyObject]) -> PyList: ...
    def get(self, index: int) -> Object: ...
    def getArray(self) -> List[PyObject]: ...
    def index(self, o: PyObject, *args: int) -> int: ...
    def indexOf(self, o: Object) -> int: ...
    def insert(self, o: PyObject) -> None: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator: ...
    def lastIndexOf(self, o: Object) -> int: ...
    def listIterator(self, index: Optional[int] = ...) -> java.util.ListIterator: ...
    def pyadd(self, *args: Any) -> Optional[bool]: ...
    def pyget(self, index: int) -> PyObject: ...
    def pyset(self, index: int, element: PyObject) -> None: ...
    def remove(self, *args: Any) -> Union[bool, None, Object]: ...
    def removeAll(self, c: java.util.Collection) -> bool: ...
    def retainAll(self, c: java.util.Collection) -> bool: ...
    def reverse(self) -> None: ...
    def set(self, index: int, element: Object) -> Object: ...
    def size(self) -> int: ...
    def sort(self, *args: PyObject) -> None: ...
    def subList(self, fromIndex: int, toIndex: int) -> List[PyObject]: ...
    def toArray(self, a: Optional[List[Object]] = ...) -> List[Object]: ...

class PyModule(PyObject): ...

class PyString(PyObject):
    def __init__(self, *args: Any) -> None: ...

class PySystemState(PyObject):
    def argv(self) -> PyList: ...
    @staticmethod
    def builtin_module_names() -> PyTuple: ...
    def builtins(self) -> PyObject: ...
    @staticmethod
    def byteorder() -> PyString: ...
    @staticmethod
    def copyright() -> PyObject: ...
    def dont_write_bytecode(self) -> bool: ...
    @staticmethod
    def exec_prefix() -> PyObject: ...
    def executable(self) -> PyObject: ...
    @staticmethod
    def flags() -> Class: ...
    @staticmethod
    def float_info() -> PyObject: ...
    @staticmethod
    def float_repr_style() -> PyString: ...
    @staticmethod
    def hexversion() -> int: ...
    def last_traceback(self) -> PyObject: ...
    def last_type(self) -> PyObject: ...
    def last_value(self) -> PyObject: ...
    @staticmethod
    def long_info() -> PyObject: ...
    @staticmethod
    def maxint() -> int: ...
    @staticmethod
    def maxsize() -> int: ...
    @staticmethod
    def maxunicode() -> int: ...
    def meta_path(self) -> PyList: ...
    @staticmethod
    def minint() -> int: ...
    def modules(self) -> PyObject: ...
    def modules_reloading(self) -> Mapping[AnyStr, PyModule]: ...
    def path(self) -> PyList: ...
    def path_hooks(self) -> PyList: ...
    def path_importer_cache(self) -> PyObject: ...
    def platform(self) -> PyObject: ...
    @staticmethod
    def prefix() -> PyObject: ...
    def ps1(self) -> PyObject: ...
    def ps2(self) -> PyObject: ...
    @staticmethod
    def py3kwarning() -> bool: ...
    @staticmethod
    def registry() -> java.util.Properties: ...
    def stderr(self) -> PyObject: ...
    def stdin(self) -> PyObject: ...
    def stdout(self) -> PyObject: ...
    @staticmethod
    def subversion() -> PyTuple: ...
    @staticmethod
    def version() -> PyString: ...
    @staticmethod
    def version_info() -> PyVersionInfo: ...
    def warnoptions(self) -> PyList: ...

class PyTraceback(PyObject):
    tb_frame: PyFrame
    tb_lineno: int
    tb_next: PyObject
    def __init__(self, next: PyTraceback, frame: PyFrame) -> None: ...
    def dumpStack(self, buf: Optional[StringBuilder] = ...) -> Optional[AnyStr]: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...

class PyTuple(PySequenceList):
    def __init__(self, *args: Any) -> None: ...
    def add(self, *args: Any) -> Optional[bool]: ...
    def addAll(self, *args: Any) -> bool: ...
    def clear(self) -> None: ...
    def contains(self, o: Object) -> bool: ...
    def containsAll(self, c: java.util.Collection) -> bool: ...
    def count(self, value: PyObject) -> int: ...
    @staticmethod
    def fromIterable(iterable: PyObject) -> PyTuple: ...
    def get(self, index: int) -> Object: ...
    def getArray(self) -> List[PyObject]: ...
    def index(self, value: PyObject, *args: int) -> int: ...
    def indexOf(self, o: Object) -> int: ...
    def isEmpty(self) -> bool: ...
    def iterator(self) -> java.util.Iterator: ...
    def lastIndexOf(self, o: Object) -> int: ...
    def listIterator(self, index: Optional[int] = ...) -> java.util.ListIterator: ...
    def pyadd(self, *args: Any) -> Optional[bool]: ...
    def pyget(self, index: int) -> PyObject: ...
    def pyset(self, index: int, element: PyObject) -> None: ...
    def remove(self, *args: Any) -> Union[bool, None, Object]: ...
    def removeAll(self, c: java.util.Collection) -> bool: ...
    def retainAll(self, c: java.util.Collection) -> bool: ...
    def set(self, index: int, element: Object) -> Object: ...
    def size(self) -> int: ...
    def subList(self, fromIndex: int, toIndex: int) -> List[PyObject]: ...
    def toArray(self, a: Optional[List[Object]] = ...) -> List[Object]: ...
    def tuple___iter__(self) -> PyObject: ...

class PyType(PyObject):
    @staticmethod
    def addBuilder(c: Class, builder: TypeBuilder) -> None: ...
    def addMethod(self, meth: PyBuiltinMethod) -> None: ...
    def compatibleForAssignment(self, other: PyType, attribute: AnyStr) -> None: ...
    def delBases(self) -> None: ...
    def delModule(self) -> None: ...
    @staticmethod
    def ensureBootstrapped() -> bool: ...
    @staticmethod
    def ensureDoc(arg: PyObject) -> None: ...
    @staticmethod
    def ensureModule(arg: PyObject) -> None: ...
    def fastGetName(self) -> AnyStr: ...
    @staticmethod
    def fromClass(c: Class, hardRef: bool = ...) -> PyType: ...
    def getAbstractMethods(self) -> PyObject: ...
    def getBase(self) -> PyObject: ...
    def getBases(self) -> PyObject: ...
    def getDoc(self) -> PyObject: ...
    def getFlags(self) -> long: ...
    def getModule(self) -> PyObject: ...
    def getMro(self) -> Tuple[Any, ...]: ...
    def getName(self) -> AnyStr: ...
    def getNumSlots(self) -> int: ...
    def getProxyType(self) -> Class: ...
    def getStatic(self) -> PyObject: ...
    def instDict(self) -> PyObject: ...
    def isSubType(self, supertype: PyType) -> bool: ...
    def lookup_where(self, name: AnyStr, where: List[PyObject]) -> PyObject: ...
    def lookup(self, name: AnyStr) -> PyObject: ...
    def needsFinalizer(self) -> bool: ...
    @staticmethod
    def newType(
        new_: PyNewWrapper,
        metatype: PyType,
        name: AnyStr,
        bases: Tuple[Any, ...],
        dict_: PyObject,
    ) -> PyObject: ...
    def pyDelName(self) -> None: ...
    def pyGetName(self) -> PyObject: ...
    def pySetName(self, name: PyObject) -> None: ...
    def refersDirectlyTo(self, ob: PyObject) -> bool: ...
    def removeMethod(self, meth: PyBuiltinMethod) -> None: ...
    def setAbstractMethods(self, value: PyObject) -> None: ...
    def setBases(self, newBasesTuple: PyObject) -> None: ...
    def setName(self, name: AnyStr) -> None: ...
    def super_lookup(self, ref: PyType, name: AnyStr) -> PyObject: ...
    def traverse(self, visit: Visitproc, arg: Object) -> int: ...
    def type___eq__(self, other: PyObject) -> PyObject: ...
    def type___ge__(self, other: PyObject) -> PyObject: ...
    def type___gt__(self, other: PyObject) -> PyObject: ...
    def type___instancecheck__(self, inst: PyObject) -> bool: ...
    def type___le__(self, other: PyObject) -> PyObject: ...
    def type___lt__(self, other: PyObject) -> PyObject: ...
    def type___ne__(self, other: PyObject) -> PyObject: ...
    def type___subclasscheck__(self, inst: PyObject) -> bool: ...
    def type___subclasses__(self) -> PyObject: ...

class TraceFunction(Object):
    def traceCall(self, frame: PyFrame) -> TraceFunction: ...
    def traceException(self, frame: PyFrame, exc: PyException) -> TraceFunction: ...
    def traceLine(self, frame: PyFrame, line: int) -> TraceFunction: ...
    def traceReturn(self, frame: PyFrame, ret: PyObject) -> TraceFunction: ...

class PyVersionInfo(PyTuple): ...

class Visitproc:
    def visit(self, obj: PyObject, arg: Object) -> int: ...
