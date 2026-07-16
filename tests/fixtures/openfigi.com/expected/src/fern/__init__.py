



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BulkMappingJob,
        BulkMappingJobResult,
        FigiResult,
        GetMappingValuesKeyRequestKey,
        GetMappingValuesKeyResponse,
        MappingJob,
        MappingJobIdType,
        MappingJobIdValue,
        MappingJobOptionType,
        MappingJobResult,
        MappingJobResultFigiList,
        MappingJobResultFigiNotFound,
        MappingJobStateCode,
        NullableDateInterval,
        NullableNumberInterval,
    )
    from .errors import (
        BadRequestError,
        ContentTooLargeError,
        InternalServerError,
        NotAcceptableError,
        UnauthorizedError,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BulkMappingJob": ".types",
    "BulkMappingJobResult": ".types",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "FigiResult": ".types",
    "GetMappingValuesKeyRequestKey": ".types",
    "GetMappingValuesKeyResponse": ".types",
    "InternalServerError": ".errors",
    "MappingJob": ".types",
    "MappingJobIdType": ".types",
    "MappingJobIdValue": ".types",
    "MappingJobOptionType": ".types",
    "MappingJobResult": ".types",
    "MappingJobResultFigiList": ".types",
    "MappingJobResultFigiNotFound": ".types",
    "MappingJobStateCode": ".types",
    "NotAcceptableError": ".errors",
    "NullableDateInterval": ".types",
    "NullableNumberInterval": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "AsyncFernApi",
    "BadRequestError",
    "BulkMappingJob",
    "BulkMappingJobResult",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "FigiResult",
    "GetMappingValuesKeyRequestKey",
    "GetMappingValuesKeyResponse",
    "InternalServerError",
    "MappingJob",
    "MappingJobIdType",
    "MappingJobIdValue",
    "MappingJobOptionType",
    "MappingJobResult",
    "MappingJobResultFigiList",
    "MappingJobResultFigiNotFound",
    "MappingJobStateCode",
    "NotAcceptableError",
    "NullableDateInterval",
    "NullableNumberInterval",
    "UnauthorizedError",
    "__version__",
]
