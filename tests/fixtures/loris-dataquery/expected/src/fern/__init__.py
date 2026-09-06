



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        AllQueries,
        BadRequestErrorBody,
        GetQueriesQueryIdCountResponse,
        PostQueriesResponse,
        Query,
        QueryCriteriaGroup,
        QueryCriteriaGroupOperator,
        QueryField,
        QueryGroupField,
        QueryGroupFieldOp,
        QueryObject,
        QueryObjectType,
        QueryResults,
        QueryRun,
        QueryRunList,
    )
    from .errors import BadRequestError, ForbiddenError, InternalServerError
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AllQueries": ".types",
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "ForbiddenError": ".errors",
    "GetQueriesQueryIdCountResponse": ".types",
    "InternalServerError": ".errors",
    "PostQueriesResponse": ".types",
    "Query": ".types",
    "QueryCriteriaGroup": ".types",
    "QueryCriteriaGroupOperator": ".types",
    "QueryField": ".types",
    "QueryGroupField": ".types",
    "QueryGroupFieldOp": ".types",
    "QueryObject": ".types",
    "QueryObjectType": ".types",
    "QueryResults": ".types",
    "QueryRun": ".types",
    "QueryRunList": ".types",
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
    "AllQueries",
    "AsyncFernApi",
    "BadRequestError",
    "BadRequestErrorBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "FernApi",
    "FernApiEnvironment",
    "ForbiddenError",
    "GetQueriesQueryIdCountResponse",
    "InternalServerError",
    "PostQueriesResponse",
    "Query",
    "QueryCriteriaGroup",
    "QueryCriteriaGroupOperator",
    "QueryField",
    "QueryGroupField",
    "QueryGroupFieldOp",
    "QueryObject",
    "QueryObjectType",
    "QueryResults",
    "QueryRun",
    "QueryRunList",
    "__version__",
]
