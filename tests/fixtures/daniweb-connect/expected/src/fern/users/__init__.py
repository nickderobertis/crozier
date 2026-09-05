



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetUsersRequestFilter,
        GetUsersRequestOrderBy,
        PatchUsersRequestCompanySize,
        PatchUsersRequestGoalsItem,
        PatchUsersRequestIndustry,
        PatchUsersRequestJobPosition,
        PatchUsersRequestLocationImportance,
        PatchUsersRequestTargetedIndustry,
        PostUsersIdMessagesRequestMetadata0Privacy,
        PostUsersIdMessagesRequestMetadata1Privacy,
        PostUsersIdMessagesRequestMetadata2Privacy,
        PostUsersIdMetadataRequestMetadata0Privacy,
        PostUsersIdMetadataRequestMetadata1Privacy,
        PostUsersIdMetadataRequestMetadata2Privacy,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetUsersRequestFilter": ".types",
    "GetUsersRequestOrderBy": ".types",
    "PatchUsersRequestCompanySize": ".types",
    "PatchUsersRequestGoalsItem": ".types",
    "PatchUsersRequestIndustry": ".types",
    "PatchUsersRequestJobPosition": ".types",
    "PatchUsersRequestLocationImportance": ".types",
    "PatchUsersRequestTargetedIndustry": ".types",
    "PostUsersIdMessagesRequestMetadata0Privacy": ".types",
    "PostUsersIdMessagesRequestMetadata1Privacy": ".types",
    "PostUsersIdMessagesRequestMetadata2Privacy": ".types",
    "PostUsersIdMetadataRequestMetadata0Privacy": ".types",
    "PostUsersIdMetadataRequestMetadata1Privacy": ".types",
    "PostUsersIdMetadataRequestMetadata2Privacy": ".types",
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
    "GetUsersRequestFilter",
    "GetUsersRequestOrderBy",
    "PatchUsersRequestCompanySize",
    "PatchUsersRequestGoalsItem",
    "PatchUsersRequestIndustry",
    "PatchUsersRequestJobPosition",
    "PatchUsersRequestLocationImportance",
    "PatchUsersRequestTargetedIndustry",
    "PostUsersIdMessagesRequestMetadata0Privacy",
    "PostUsersIdMessagesRequestMetadata1Privacy",
    "PostUsersIdMessagesRequestMetadata2Privacy",
    "PostUsersIdMetadataRequestMetadata0Privacy",
    "PostUsersIdMetadataRequestMetadata1Privacy",
    "PostUsersIdMetadataRequestMetadata2Privacy",
]
