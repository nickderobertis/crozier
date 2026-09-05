



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_conversations_statuses_request_filter import GetConversationsStatusesRequestFilter
    from .post_conversations_id_messages_request_metadata0privacy import (
        PostConversationsIdMessagesRequestMetadata0Privacy,
    )
    from .post_conversations_id_messages_request_metadata1privacy import (
        PostConversationsIdMessagesRequestMetadata1Privacy,
    )
    from .post_conversations_id_messages_request_metadata2privacy import (
        PostConversationsIdMessagesRequestMetadata2Privacy,
    )
    from .post_conversations_id_schedules_request_sort import PostConversationsIdSchedulesRequestSort
    from .post_conversations_schedules_request_sort import PostConversationsSchedulesRequestSort
_dynamic_imports: typing.Dict[str, str] = {
    "GetConversationsStatusesRequestFilter": ".get_conversations_statuses_request_filter",
    "PostConversationsIdMessagesRequestMetadata0Privacy": ".post_conversations_id_messages_request_metadata0privacy",
    "PostConversationsIdMessagesRequestMetadata1Privacy": ".post_conversations_id_messages_request_metadata1privacy",
    "PostConversationsIdMessagesRequestMetadata2Privacy": ".post_conversations_id_messages_request_metadata2privacy",
    "PostConversationsIdSchedulesRequestSort": ".post_conversations_id_schedules_request_sort",
    "PostConversationsSchedulesRequestSort": ".post_conversations_schedules_request_sort",
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
    "GetConversationsStatusesRequestFilter",
    "PostConversationsIdMessagesRequestMetadata0Privacy",
    "PostConversationsIdMessagesRequestMetadata1Privacy",
    "PostConversationsIdMessagesRequestMetadata2Privacy",
    "PostConversationsIdSchedulesRequestSort",
    "PostConversationsSchedulesRequestSort",
]
