



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_users_request_filter import GetUsersRequestFilter
    from .get_users_request_order_by import GetUsersRequestOrderBy
    from .patch_users_request_company_size import PatchUsersRequestCompanySize
    from .patch_users_request_goals_item import PatchUsersRequestGoalsItem
    from .patch_users_request_industry import PatchUsersRequestIndustry
    from .patch_users_request_job_position import PatchUsersRequestJobPosition
    from .patch_users_request_location_importance import PatchUsersRequestLocationImportance
    from .patch_users_request_targeted_industry import PatchUsersRequestTargetedIndustry
    from .post_users_id_messages_request_metadata0privacy import PostUsersIdMessagesRequestMetadata0Privacy
    from .post_users_id_messages_request_metadata1privacy import PostUsersIdMessagesRequestMetadata1Privacy
    from .post_users_id_messages_request_metadata2privacy import PostUsersIdMessagesRequestMetadata2Privacy
    from .post_users_id_metadata_request_metadata0privacy import PostUsersIdMetadataRequestMetadata0Privacy
    from .post_users_id_metadata_request_metadata1privacy import PostUsersIdMetadataRequestMetadata1Privacy
    from .post_users_id_metadata_request_metadata2privacy import PostUsersIdMetadataRequestMetadata2Privacy
_dynamic_imports: typing.Dict[str, str] = {
    "GetUsersRequestFilter": ".get_users_request_filter",
    "GetUsersRequestOrderBy": ".get_users_request_order_by",
    "PatchUsersRequestCompanySize": ".patch_users_request_company_size",
    "PatchUsersRequestGoalsItem": ".patch_users_request_goals_item",
    "PatchUsersRequestIndustry": ".patch_users_request_industry",
    "PatchUsersRequestJobPosition": ".patch_users_request_job_position",
    "PatchUsersRequestLocationImportance": ".patch_users_request_location_importance",
    "PatchUsersRequestTargetedIndustry": ".patch_users_request_targeted_industry",
    "PostUsersIdMessagesRequestMetadata0Privacy": ".post_users_id_messages_request_metadata0privacy",
    "PostUsersIdMessagesRequestMetadata1Privacy": ".post_users_id_messages_request_metadata1privacy",
    "PostUsersIdMessagesRequestMetadata2Privacy": ".post_users_id_messages_request_metadata2privacy",
    "PostUsersIdMetadataRequestMetadata0Privacy": ".post_users_id_metadata_request_metadata0privacy",
    "PostUsersIdMetadataRequestMetadata1Privacy": ".post_users_id_metadata_request_metadata1privacy",
    "PostUsersIdMetadataRequestMetadata2Privacy": ".post_users_id_metadata_request_metadata2privacy",
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
