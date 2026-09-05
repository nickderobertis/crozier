



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Batch,
        BatchCondition,
        BatchConditionVarEmpty,
        BatchConditionVarMinSize,
        BatchConditionVarNotEmpty,
        BatchConditionZero,
        BatchEntry,
        BatchEntryForEach,
        BatchEntryForEachForEach,
        BatchEntryQuery,
        HealthResponse,
        NamedQuery,
        OperationTree,
        QueryError,
        QueryParameterType,
        QueryParameterTypeArray,
        QueryParameterTypeZero,
        QueryParameterTypes,
        QueryParameterValue,
        QueryParameters,
        QueryRequest,
        QueryRequest_Read,
        QueryRequest_Write,
        QueryResponse,
        ReadBatchQuery,
        ReadQueryRequest,
        WriteBatchQuery,
        WriteQueryRequest,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ContentTooLargeError,
        ForbiddenError,
        InternalServerError,
        PaymentRequiredError,
        RequestTimeoutError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
    )
    from . import health, queries
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Batch": ".types",
    "BatchCondition": ".types",
    "BatchConditionVarEmpty": ".types",
    "BatchConditionVarMinSize": ".types",
    "BatchConditionVarNotEmpty": ".types",
    "BatchConditionZero": ".types",
    "BatchEntry": ".types",
    "BatchEntryForEach": ".types",
    "BatchEntryForEachForEach": ".types",
    "BatchEntryQuery": ".types",
    "ConflictError": ".errors",
    "ContentTooLargeError": ".errors",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "HealthResponse": ".types",
    "InternalServerError": ".errors",
    "NamedQuery": ".types",
    "OperationTree": ".types",
    "PaymentRequiredError": ".errors",
    "QueryError": ".types",
    "QueryParameterType": ".types",
    "QueryParameterTypeArray": ".types",
    "QueryParameterTypeZero": ".types",
    "QueryParameterTypes": ".types",
    "QueryParameterValue": ".types",
    "QueryParameters": ".types",
    "QueryRequest": ".types",
    "QueryRequest_Read": ".types",
    "QueryRequest_Write": ".types",
    "QueryResponse": ".types",
    "ReadBatchQuery": ".types",
    "ReadQueryRequest": ".types",
    "RequestTimeoutError": ".errors",
    "ServiceUnavailableError": ".errors",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "WriteBatchQuery": ".types",
    "WriteQueryRequest": ".types",
    "__version__": ".version",
    "health": ".health",
    "queries": ".queries",
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
    "Batch",
    "BatchCondition",
    "BatchConditionVarEmpty",
    "BatchConditionVarMinSize",
    "BatchConditionVarNotEmpty",
    "BatchConditionZero",
    "BatchEntry",
    "BatchEntryForEach",
    "BatchEntryForEachForEach",
    "BatchEntryQuery",
    "ConflictError",
    "ContentTooLargeError",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "HealthResponse",
    "InternalServerError",
    "NamedQuery",
    "OperationTree",
    "PaymentRequiredError",
    "QueryError",
    "QueryParameterType",
    "QueryParameterTypeArray",
    "QueryParameterTypeZero",
    "QueryParameterTypes",
    "QueryParameterValue",
    "QueryParameters",
    "QueryRequest",
    "QueryRequest_Read",
    "QueryRequest_Write",
    "QueryResponse",
    "ReadBatchQuery",
    "ReadQueryRequest",
    "RequestTimeoutError",
    "ServiceUnavailableError",
    "TooManyRequestsError",
    "UnauthorizedError",
    "WriteBatchQuery",
    "WriteQueryRequest",
    "__version__",
    "health",
    "queries",
]
