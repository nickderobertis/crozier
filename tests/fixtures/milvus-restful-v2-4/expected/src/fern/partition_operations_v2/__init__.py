



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostV2VectordbPartitionsCreateResponse,
        PostV2VectordbPartitionsCreateResponseData,
        PostV2VectordbPartitionsDropResponse,
        PostV2VectordbPartitionsDropResponseData,
        PostV2VectordbPartitionsGetStatsResponse,
        PostV2VectordbPartitionsGetStatsResponseData,
        PostV2VectordbPartitionsHasResponse,
        PostV2VectordbPartitionsHasResponseData,
        PostV2VectordbPartitionsListResponse,
        PostV2VectordbPartitionsLoadResponse,
        PostV2VectordbPartitionsLoadResponseData,
        PostV2VectordbPartitionsReleaseResponse,
        PostV2VectordbPartitionsReleaseResponseData,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbPartitionsCreateResponse": ".types",
    "PostV2VectordbPartitionsCreateResponseData": ".types",
    "PostV2VectordbPartitionsDropResponse": ".types",
    "PostV2VectordbPartitionsDropResponseData": ".types",
    "PostV2VectordbPartitionsGetStatsResponse": ".types",
    "PostV2VectordbPartitionsGetStatsResponseData": ".types",
    "PostV2VectordbPartitionsHasResponse": ".types",
    "PostV2VectordbPartitionsHasResponseData": ".types",
    "PostV2VectordbPartitionsListResponse": ".types",
    "PostV2VectordbPartitionsLoadResponse": ".types",
    "PostV2VectordbPartitionsLoadResponseData": ".types",
    "PostV2VectordbPartitionsReleaseResponse": ".types",
    "PostV2VectordbPartitionsReleaseResponseData": ".types",
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
