



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_partitions_create_response import PostV2VectordbPartitionsCreateResponse
    from .post_v2vectordb_partitions_create_response_data import PostV2VectordbPartitionsCreateResponseData
    from .post_v2vectordb_partitions_drop_response import PostV2VectordbPartitionsDropResponse
    from .post_v2vectordb_partitions_drop_response_data import PostV2VectordbPartitionsDropResponseData
    from .post_v2vectordb_partitions_get_stats_response import PostV2VectordbPartitionsGetStatsResponse
    from .post_v2vectordb_partitions_get_stats_response_data import PostV2VectordbPartitionsGetStatsResponseData
    from .post_v2vectordb_partitions_has_response import PostV2VectordbPartitionsHasResponse
    from .post_v2vectordb_partitions_has_response_data import PostV2VectordbPartitionsHasResponseData
    from .post_v2vectordb_partitions_list_response import PostV2VectordbPartitionsListResponse
    from .post_v2vectordb_partitions_load_response import PostV2VectordbPartitionsLoadResponse
    from .post_v2vectordb_partitions_load_response_data import PostV2VectordbPartitionsLoadResponseData
    from .post_v2vectordb_partitions_release_response import PostV2VectordbPartitionsReleaseResponse
    from .post_v2vectordb_partitions_release_response_data import PostV2VectordbPartitionsReleaseResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbPartitionsCreateResponse": ".post_v2vectordb_partitions_create_response",
    "PostV2VectordbPartitionsCreateResponseData": ".post_v2vectordb_partitions_create_response_data",
    "PostV2VectordbPartitionsDropResponse": ".post_v2vectordb_partitions_drop_response",
    "PostV2VectordbPartitionsDropResponseData": ".post_v2vectordb_partitions_drop_response_data",
    "PostV2VectordbPartitionsGetStatsResponse": ".post_v2vectordb_partitions_get_stats_response",
    "PostV2VectordbPartitionsGetStatsResponseData": ".post_v2vectordb_partitions_get_stats_response_data",
    "PostV2VectordbPartitionsHasResponse": ".post_v2vectordb_partitions_has_response",
    "PostV2VectordbPartitionsHasResponseData": ".post_v2vectordb_partitions_has_response_data",
    "PostV2VectordbPartitionsListResponse": ".post_v2vectordb_partitions_list_response",
    "PostV2VectordbPartitionsLoadResponse": ".post_v2vectordb_partitions_load_response",
    "PostV2VectordbPartitionsLoadResponseData": ".post_v2vectordb_partitions_load_response_data",
    "PostV2VectordbPartitionsReleaseResponse": ".post_v2vectordb_partitions_release_response",
    "PostV2VectordbPartitionsReleaseResponseData": ".post_v2vectordb_partitions_release_response_data",
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
    "PostV2VectordbPartitionsCreateResponse",
    "PostV2VectordbPartitionsCreateResponseData",
    "PostV2VectordbPartitionsDropResponse",
    "PostV2VectordbPartitionsDropResponseData",
    "PostV2VectordbPartitionsGetStatsResponse",
    "PostV2VectordbPartitionsGetStatsResponseData",
    "PostV2VectordbPartitionsHasResponse",
    "PostV2VectordbPartitionsHasResponseData",
    "PostV2VectordbPartitionsListResponse",
    "PostV2VectordbPartitionsLoadResponse",
    "PostV2VectordbPartitionsLoadResponseData",
    "PostV2VectordbPartitionsReleaseResponse",
    "PostV2VectordbPartitionsReleaseResponseData",
]
