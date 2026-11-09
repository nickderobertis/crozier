



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        BadRequestErrorBody,
        ConflictErrorBody,
        ContentTooLargeErrorBody,
        Error,
        InternalServerErrorBody,
        PaginationMeta,
        ShardDetail,
        ShardDetailDependenciesItem,
        ShardSummary,
        ShardVersion,
        ShardVersionDetail,
        ShardVersionDetailDependenciesItem,
        UnauthorizedErrorBody,
        ValidationError,
    )
    from .errors import (
        BadRequestError,
        ConflictError,
        ContentTooLargeError,
        InternalServerError,
        NotFoundError,
        ServiceUnavailableError,
        TooManyRequestsError,
        UnauthorizedError,
        UnprocessableEntityError,
    )
    from . import downloads, health, shards, versions
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .downloads import PostApiShardsHostOwnerRepoVersionDownloadResponse
    from .environment import FernApiEnvironment
    from .health import GetApiHealthResponse, GetApiHealthResponseServices
    from .shards import (
        GetApiShardsResponse,
        PostApiShardsResponse,
        PostApiShardsResponseShard,
        PostApiShardsUploadResponse,
        PostApiShardsUploadResponseShard,
        PostApiShardsUploadResponseVersion,
    )
    from .version import __version__
    from .versions import GetApiShardsHostOwnerRepoVersionResponse, GetApiShardsHostOwnerRepoVersionsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "BadRequestErrorBody": ".types",
    "ConflictError": ".errors",
    "ConflictErrorBody": ".types",
    "ContentTooLargeError": ".errors",
    "ContentTooLargeErrorBody": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Error": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "GetApiHealthResponse": ".health",
    "GetApiHealthResponseServices": ".health",
    "GetApiShardsHostOwnerRepoVersionResponse": ".versions",
    "GetApiShardsHostOwnerRepoVersionsResponse": ".versions",
    "GetApiShardsResponse": ".shards",
    "InternalServerError": ".errors",
    "InternalServerErrorBody": ".types",
    "NotFoundError": ".errors",
    "PaginationMeta": ".types",
    "PostApiShardsHostOwnerRepoVersionDownloadResponse": ".downloads",
    "PostApiShardsResponse": ".shards",
    "PostApiShardsResponseShard": ".shards",
    "PostApiShardsUploadResponse": ".shards",
    "PostApiShardsUploadResponseShard": ".shards",
    "PostApiShardsUploadResponseVersion": ".shards",
    "ServiceUnavailableError": ".errors",
    "ShardDetail": ".types",
    "ShardDetailDependenciesItem": ".types",
    "ShardSummary": ".types",
    "ShardVersion": ".types",
    "ShardVersionDetail": ".types",
    "ShardVersionDetailDependenciesItem": ".types",
    "TooManyRequestsError": ".errors",
    "UnauthorizedError": ".errors",
    "UnauthorizedErrorBody": ".types",
    "UnprocessableEntityError": ".errors",
    "ValidationError": ".types",
    "__version__": ".version",
    "downloads": ".downloads",
    "health": ".health",
    "shards": ".shards",
    "versions": ".versions",
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
    "BadRequestErrorBody",
    "ConflictError",
    "ConflictErrorBody",
    "ContentTooLargeError",
    "ContentTooLargeErrorBody",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Error",
    "FernApi",
    "FernApiEnvironment",
    "GetApiHealthResponse",
    "GetApiHealthResponseServices",
    "GetApiShardsHostOwnerRepoVersionResponse",
    "GetApiShardsHostOwnerRepoVersionsResponse",
    "GetApiShardsResponse",
    "InternalServerError",
    "InternalServerErrorBody",
    "NotFoundError",
    "PaginationMeta",
    "PostApiShardsHostOwnerRepoVersionDownloadResponse",
    "PostApiShardsResponse",
    "PostApiShardsResponseShard",
    "PostApiShardsUploadResponse",
    "PostApiShardsUploadResponseShard",
    "PostApiShardsUploadResponseVersion",
    "ServiceUnavailableError",
    "ShardDetail",
    "ShardDetailDependenciesItem",
    "ShardSummary",
    "ShardVersion",
    "ShardVersionDetail",
    "ShardVersionDetailDependenciesItem",
    "TooManyRequestsError",
    "UnauthorizedError",
    "UnauthorizedErrorBody",
    "UnprocessableEntityError",
    "ValidationError",
    "__version__",
    "downloads",
    "health",
    "shards",
    "versions",
]
