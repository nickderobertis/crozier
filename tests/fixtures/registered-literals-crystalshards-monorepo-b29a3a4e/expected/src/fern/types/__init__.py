



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bad_request_error_body import BadRequestErrorBody
    from .conflict_error_body import ConflictErrorBody
    from .content_too_large_error_body import ContentTooLargeErrorBody
    from .error import Error
    from .internal_server_error_body import InternalServerErrorBody
    from .pagination_meta import PaginationMeta
    from .shard_detail import ShardDetail
    from .shard_detail_dependencies_item import ShardDetailDependenciesItem
    from .shard_summary import ShardSummary
    from .shard_version import ShardVersion
    from .shard_version_detail import ShardVersionDetail
    from .shard_version_detail_dependencies_item import ShardVersionDetailDependenciesItem
    from .unauthorized_error_body import UnauthorizedErrorBody
    from .validation_error import ValidationError
_dynamic_imports: typing.Dict[str, str] = {
    "BadRequestErrorBody": ".bad_request_error_body",
    "ConflictErrorBody": ".conflict_error_body",
    "ContentTooLargeErrorBody": ".content_too_large_error_body",
    "Error": ".error",
    "InternalServerErrorBody": ".internal_server_error_body",
    "PaginationMeta": ".pagination_meta",
    "ShardDetail": ".shard_detail",
    "ShardDetailDependenciesItem": ".shard_detail_dependencies_item",
    "ShardSummary": ".shard_summary",
    "ShardVersion": ".shard_version",
    "ShardVersionDetail": ".shard_version_detail",
    "ShardVersionDetailDependenciesItem": ".shard_version_detail_dependencies_item",
    "UnauthorizedErrorBody": ".unauthorized_error_body",
    "ValidationError": ".validation_error",
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
    "BadRequestErrorBody",
    "ConflictErrorBody",
    "ContentTooLargeErrorBody",
    "Error",
    "InternalServerErrorBody",
    "PaginationMeta",
    "ShardDetail",
    "ShardDetailDependenciesItem",
    "ShardSummary",
    "ShardVersion",
    "ShardVersionDetail",
    "ShardVersionDetailDependenciesItem",
    "UnauthorizedErrorBody",
    "ValidationError",
]
