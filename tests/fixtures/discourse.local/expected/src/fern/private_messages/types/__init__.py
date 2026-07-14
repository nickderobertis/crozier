



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_user_sent_private_messages_response import GetUserSentPrivateMessagesResponse
    from .get_user_sent_private_messages_response_topic_list import GetUserSentPrivateMessagesResponseTopicList
    from .get_user_sent_private_messages_response_topic_list_topics_item import (
        GetUserSentPrivateMessagesResponseTopicListTopicsItem,
    )
    from .get_user_sent_private_messages_response_topic_list_topics_item_posters_item import (
        GetUserSentPrivateMessagesResponseTopicListTopicsItemPostersItem,
    )
    from .get_user_sent_private_messages_response_users_item import GetUserSentPrivateMessagesResponseUsersItem
    from .list_user_private_messages_response import ListUserPrivateMessagesResponse
    from .list_user_private_messages_response_topic_list import ListUserPrivateMessagesResponseTopicList
    from .list_user_private_messages_response_topic_list_topics_item import (
        ListUserPrivateMessagesResponseTopicListTopicsItem,
    )
    from .list_user_private_messages_response_topic_list_topics_item_participants_item import (
        ListUserPrivateMessagesResponseTopicListTopicsItemParticipantsItem,
    )
    from .list_user_private_messages_response_topic_list_topics_item_posters_item import (
        ListUserPrivateMessagesResponseTopicListTopicsItemPostersItem,
    )
    from .list_user_private_messages_response_users_item import ListUserPrivateMessagesResponseUsersItem
_dynamic_imports: typing.Dict[str, str] = {
    "GetUserSentPrivateMessagesResponse": ".get_user_sent_private_messages_response",
    "GetUserSentPrivateMessagesResponseTopicList": ".get_user_sent_private_messages_response_topic_list",
    "GetUserSentPrivateMessagesResponseTopicListTopicsItem": ".get_user_sent_private_messages_response_topic_list_topics_item",
    "GetUserSentPrivateMessagesResponseTopicListTopicsItemPostersItem": ".get_user_sent_private_messages_response_topic_list_topics_item_posters_item",
    "GetUserSentPrivateMessagesResponseUsersItem": ".get_user_sent_private_messages_response_users_item",
    "ListUserPrivateMessagesResponse": ".list_user_private_messages_response",
    "ListUserPrivateMessagesResponseTopicList": ".list_user_private_messages_response_topic_list",
    "ListUserPrivateMessagesResponseTopicListTopicsItem": ".list_user_private_messages_response_topic_list_topics_item",
    "ListUserPrivateMessagesResponseTopicListTopicsItemParticipantsItem": ".list_user_private_messages_response_topic_list_topics_item_participants_item",
    "ListUserPrivateMessagesResponseTopicListTopicsItemPostersItem": ".list_user_private_messages_response_topic_list_topics_item_posters_item",
    "ListUserPrivateMessagesResponseUsersItem": ".list_user_private_messages_response_users_item",
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
    "GetUserSentPrivateMessagesResponse",
    "GetUserSentPrivateMessagesResponseTopicList",
    "GetUserSentPrivateMessagesResponseTopicListTopicsItem",
    "GetUserSentPrivateMessagesResponseTopicListTopicsItemPostersItem",
    "GetUserSentPrivateMessagesResponseUsersItem",
    "ListUserPrivateMessagesResponse",
    "ListUserPrivateMessagesResponseTopicList",
    "ListUserPrivateMessagesResponseTopicListTopicsItem",
    "ListUserPrivateMessagesResponseTopicListTopicsItemParticipantsItem",
    "ListUserPrivateMessagesResponseTopicListTopicsItemPostersItem",
    "ListUserPrivateMessagesResponseUsersItem",
]
