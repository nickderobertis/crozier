



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Animal,
        Animal_Cat,
        Animal_Dog,
        Cat,
        Dog,
        Enumerations,
        EnumerationsColors,
        ProductOrder,
        ProductOrderAddress,
        RandomNumber,
        RandomNumberParams,
    )
    from .errors import InternalServerError
    from . import escape_hatches, media_types, query_parameters, request_headers, route_matching, timeout, validation
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .query_parameters import (
        GetParamsDefaultObjectQueryRequestFilter,
        GetParamsDefaultObjectQueryResponse,
        GetParamsDefaultObjectQueryResponseFilter,
        GetParamsMixedQueryRequestStatusesItem,
        GetParamsMixedQueryResponse,
        GetParamsSimpleQueryRequestOrderBy,
        GetParamsSimpleQueryResponse,
        GetParamsUnexplodedObjectQueryRequestFilter,
        GetParamsUnexplodedObjectQueryResponse,
        GetParamsUnexplodedObjectQueryResponseFilter,
    )
    from .request_headers import GetHeadersRequestResponse, GetHeadersUndeclaredResponse
    from .timeout import GetTimeoutResponse
    from .validation import GetResponsesDefaultResponse, PostValidationOptionalBodyResponse
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Animal": ".types",
    "Animal_Cat": ".types",
    "Animal_Dog": ".types",
    "AsyncFernApi": ".client",
    "Cat": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Dog": ".types",
    "Enumerations": ".types",
    "EnumerationsColors": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetHeadersRequestResponse": ".request_headers",
    "GetHeadersUndeclaredResponse": ".request_headers",
    "GetParamsDefaultObjectQueryRequestFilter": ".query_parameters",
    "GetParamsDefaultObjectQueryResponse": ".query_parameters",
    "GetParamsDefaultObjectQueryResponseFilter": ".query_parameters",
    "GetParamsMixedQueryRequestStatusesItem": ".query_parameters",
    "GetParamsMixedQueryResponse": ".query_parameters",
    "GetParamsSimpleQueryRequestOrderBy": ".query_parameters",
    "GetParamsSimpleQueryResponse": ".query_parameters",
    "GetParamsUnexplodedObjectQueryRequestFilter": ".query_parameters",
    "GetParamsUnexplodedObjectQueryResponse": ".query_parameters",
    "GetParamsUnexplodedObjectQueryResponseFilter": ".query_parameters",
    "GetResponsesDefaultResponse": ".validation",
    "GetTimeoutResponse": ".timeout",
    "InternalServerError": ".errors",
    "PostValidationOptionalBodyResponse": ".validation",
    "ProductOrder": ".types",
    "ProductOrderAddress": ".types",
    "RandomNumber": ".types",
    "RandomNumberParams": ".types",
    "__version__": ".version",
    "escape_hatches": ".escape_hatches",
    "media_types": ".media_types",
    "query_parameters": ".query_parameters",
    "request_headers": ".request_headers",
    "route_matching": ".route_matching",
    "timeout": ".timeout",
    "validation": ".validation",
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
    "Animal",
    "Animal_Cat",
    "Animal_Dog",
    "AsyncFernApi",
    "Cat",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Dog",
    "Enumerations",
    "EnumerationsColors",
    "FernApi",
    "FernApiEnvironment",
    "GetHeadersRequestResponse",
    "GetHeadersUndeclaredResponse",
    "GetParamsDefaultObjectQueryRequestFilter",
    "GetParamsDefaultObjectQueryResponse",
    "GetParamsDefaultObjectQueryResponseFilter",
    "GetParamsMixedQueryRequestStatusesItem",
    "GetParamsMixedQueryResponse",
    "GetParamsSimpleQueryRequestOrderBy",
    "GetParamsSimpleQueryResponse",
    "GetParamsUnexplodedObjectQueryRequestFilter",
    "GetParamsUnexplodedObjectQueryResponse",
    "GetParamsUnexplodedObjectQueryResponseFilter",
    "GetResponsesDefaultResponse",
    "GetTimeoutResponse",
    "InternalServerError",
    "PostValidationOptionalBodyResponse",
    "ProductOrder",
    "ProductOrderAddress",
    "RandomNumber",
    "RandomNumberParams",
    "__version__",
    "escape_hatches",
    "media_types",
    "query_parameters",
    "request_headers",
    "route_matching",
    "timeout",
    "validation",
]
