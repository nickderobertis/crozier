



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_api_shards_response import GetApiShardsResponse
    from .post_api_shards_response import PostApiShardsResponse
    from .post_api_shards_response_shard import PostApiShardsResponseShard
    from .post_api_shards_upload_response import PostApiShardsUploadResponse
    from .post_api_shards_upload_response_shard import PostApiShardsUploadResponseShard
    from .post_api_shards_upload_response_version import PostApiShardsUploadResponseVersion
_dynamic_imports: typing.Dict[str, str] = {
    "GetApiShardsResponse": ".get_api_shards_response",
    "PostApiShardsResponse": ".post_api_shards_response",
    "PostApiShardsResponseShard": ".post_api_shards_response_shard",
    "PostApiShardsUploadResponse": ".post_api_shards_upload_response",
    "PostApiShardsUploadResponseShard": ".post_api_shards_upload_response_shard",
    "PostApiShardsUploadResponseVersion": ".post_api_shards_upload_response_version",
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
    "GetApiShardsResponse",
    "PostApiShardsResponse",
    "PostApiShardsResponseShard",
    "PostApiShardsUploadResponse",
    "PostApiShardsUploadResponseShard",
    "PostApiShardsUploadResponseVersion",
]
