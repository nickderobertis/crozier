



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_v2vectordb_aliases_alter_response import PostV2VectordbAliasesAlterResponse
    from .post_v2vectordb_aliases_alter_response_data import PostV2VectordbAliasesAlterResponseData
    from .post_v2vectordb_aliases_create_response import PostV2VectordbAliasesCreateResponse
    from .post_v2vectordb_aliases_create_response_data import PostV2VectordbAliasesCreateResponseData
    from .post_v2vectordb_aliases_describe_response import PostV2VectordbAliasesDescribeResponse
    from .post_v2vectordb_aliases_describe_response_data import PostV2VectordbAliasesDescribeResponseData
    from .post_v2vectordb_aliases_drop_response import PostV2VectordbAliasesDropResponse
    from .post_v2vectordb_aliases_drop_response_data import PostV2VectordbAliasesDropResponseData
    from .post_v2vectordb_aliases_list_response import PostV2VectordbAliasesListResponse
_dynamic_imports: typing.Dict[str, str] = {
    "PostV2VectordbAliasesAlterResponse": ".post_v2vectordb_aliases_alter_response",
    "PostV2VectordbAliasesAlterResponseData": ".post_v2vectordb_aliases_alter_response_data",
    "PostV2VectordbAliasesCreateResponse": ".post_v2vectordb_aliases_create_response",
    "PostV2VectordbAliasesCreateResponseData": ".post_v2vectordb_aliases_create_response_data",
    "PostV2VectordbAliasesDescribeResponse": ".post_v2vectordb_aliases_describe_response",
    "PostV2VectordbAliasesDescribeResponseData": ".post_v2vectordb_aliases_describe_response_data",
    "PostV2VectordbAliasesDropResponse": ".post_v2vectordb_aliases_drop_response",
    "PostV2VectordbAliasesDropResponseData": ".post_v2vectordb_aliases_drop_response_data",
    "PostV2VectordbAliasesListResponse": ".post_v2vectordb_aliases_list_response",
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
    "PostV2VectordbAliasesAlterResponse",
    "PostV2VectordbAliasesAlterResponseData",
    "PostV2VectordbAliasesCreateResponse",
    "PostV2VectordbAliasesCreateResponseData",
    "PostV2VectordbAliasesDescribeResponse",
    "PostV2VectordbAliasesDescribeResponseData",
    "PostV2VectordbAliasesDropResponse",
    "PostV2VectordbAliasesDropResponseData",
    "PostV2VectordbAliasesListResponse",
]
