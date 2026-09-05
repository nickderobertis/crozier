



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .patch_groups_id_request_privacy import PatchGroupsIdRequestPrivacy
    from .post_groups_id_messages_request_metadata0privacy import PostGroupsIdMessagesRequestMetadata0Privacy
    from .post_groups_id_messages_request_metadata1privacy import PostGroupsIdMessagesRequestMetadata1Privacy
    from .post_groups_id_messages_request_metadata2privacy import PostGroupsIdMessagesRequestMetadata2Privacy
    from .post_groups_id_schedules_request_sort import PostGroupsIdSchedulesRequestSort
    from .post_groups_messages_id_metadata_request_metadata0privacy import (
        PostGroupsMessagesIdMetadataRequestMetadata0Privacy,
    )
    from .post_groups_messages_id_metadata_request_metadata1privacy import (
        PostGroupsMessagesIdMetadataRequestMetadata1Privacy,
    )
    from .post_groups_messages_id_metadata_request_metadata2privacy import (
        PostGroupsMessagesIdMetadataRequestMetadata2Privacy,
    )
    from .post_groups_request_privacy import PostGroupsRequestPrivacy
    from .post_groups_schedules_request_sort import PostGroupsSchedulesRequestSort
_dynamic_imports: typing.Dict[str, str] = {
    "PatchGroupsIdRequestPrivacy": ".patch_groups_id_request_privacy",
    "PostGroupsIdMessagesRequestMetadata0Privacy": ".post_groups_id_messages_request_metadata0privacy",
    "PostGroupsIdMessagesRequestMetadata1Privacy": ".post_groups_id_messages_request_metadata1privacy",
    "PostGroupsIdMessagesRequestMetadata2Privacy": ".post_groups_id_messages_request_metadata2privacy",
    "PostGroupsIdSchedulesRequestSort": ".post_groups_id_schedules_request_sort",
    "PostGroupsMessagesIdMetadataRequestMetadata0Privacy": ".post_groups_messages_id_metadata_request_metadata0privacy",
    "PostGroupsMessagesIdMetadataRequestMetadata1Privacy": ".post_groups_messages_id_metadata_request_metadata1privacy",
    "PostGroupsMessagesIdMetadataRequestMetadata2Privacy": ".post_groups_messages_id_metadata_request_metadata2privacy",
    "PostGroupsRequestPrivacy": ".post_groups_request_privacy",
    "PostGroupsSchedulesRequestSort": ".post_groups_schedules_request_sort",
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
    "PatchGroupsIdRequestPrivacy",
    "PostGroupsIdMessagesRequestMetadata0Privacy",
    "PostGroupsIdMessagesRequestMetadata1Privacy",
    "PostGroupsIdMessagesRequestMetadata2Privacy",
    "PostGroupsIdSchedulesRequestSort",
    "PostGroupsMessagesIdMetadataRequestMetadata0Privacy",
    "PostGroupsMessagesIdMetadataRequestMetadata1Privacy",
    "PostGroupsMessagesIdMetadataRequestMetadata2Privacy",
    "PostGroupsRequestPrivacy",
    "PostGroupsSchedulesRequestSort",
]
