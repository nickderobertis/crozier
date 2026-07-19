



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .scheduled_messages_delete_scheduled_message_request_body import (
        ScheduledMessagesDeleteScheduledMessageRequestBody,
    )
    from .scheduled_messages_delete_scheduled_message_response import ScheduledMessagesDeleteScheduledMessageResponse
    from .scheduled_messages_list_scheduled_messages_response import ScheduledMessagesListScheduledMessagesResponse
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItem,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessage,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_include_return_message_types_item import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageIncludeReturnMessageTypesItem,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItem,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContent,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem,
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem_Image,
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem_Text,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImage,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image_source import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSource,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image_source_type import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSourceType,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_text import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemText,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_role import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_type import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemType,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule,
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_OneTime,
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_Recurring,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule_one_time import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemScheduleOneTime,
    )
    from .scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule_recurring import (
        ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemScheduleRecurring,
    )
    from .scheduled_messages_retrieve_scheduled_message_response import (
        ScheduledMessagesRetrieveScheduledMessageResponse,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessage,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_include_return_message_types_item import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageIncludeReturnMessageTypesItem,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItem,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContent,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem,
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Image,
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Text,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImage,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSource,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source_type import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_text import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemText,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_role import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemRole,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_message_messages_item_type import (
        ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemType,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_schedule import (
        ScheduledMessagesRetrieveScheduledMessageResponseSchedule,
        ScheduledMessagesRetrieveScheduledMessageResponseSchedule_OneTime,
        ScheduledMessagesRetrieveScheduledMessageResponseSchedule_Recurring,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_schedule_one_time import (
        ScheduledMessagesRetrieveScheduledMessageResponseScheduleOneTime,
    )
    from .scheduled_messages_retrieve_scheduled_message_response_schedule_recurring import (
        ScheduledMessagesRetrieveScheduledMessageResponseScheduleRecurring,
    )
    from .scheduled_messages_schedule_agent_message_request_include_return_message_types_item import (
        ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItem,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_content import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContent,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem,
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Image,
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImage,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source_type import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSourceType,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_text import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemText,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_role import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole,
    )
    from .scheduled_messages_schedule_agent_message_request_messages_item_type import (
        ScheduledMessagesScheduleAgentMessageRequestMessagesItemType,
    )
    from .scheduled_messages_schedule_agent_message_request_schedule import (
        ScheduledMessagesScheduleAgentMessageRequestSchedule,
        ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime,
        ScheduledMessagesScheduleAgentMessageRequestSchedule_Recurring,
    )
    from .scheduled_messages_schedule_agent_message_request_schedule_one_time import (
        ScheduledMessagesScheduleAgentMessageRequestScheduleOneTime,
    )
    from .scheduled_messages_schedule_agent_message_request_schedule_recurring import (
        ScheduledMessagesScheduleAgentMessageRequestScheduleRecurring,
    )
    from .scheduled_messages_schedule_agent_message_response import ScheduledMessagesScheduleAgentMessageResponse
_dynamic_imports: typing.Dict[str, str] = {
    "ScheduledMessagesDeleteScheduledMessageRequestBody": ".scheduled_messages_delete_scheduled_message_request_body",
    "ScheduledMessagesDeleteScheduledMessageResponse": ".scheduled_messages_delete_scheduled_message_response",
    "ScheduledMessagesListScheduledMessagesResponse": ".scheduled_messages_list_scheduled_messages_response",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItem": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessage": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageIncludeReturnMessageTypesItem": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_include_return_message_types_item",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItem": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContent": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImage": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSource": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image_source",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSourceType": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_image_source_type",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemText": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item_text",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem_Image": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem_Text": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_content_zero_item",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_role",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemType": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_message_messages_item_type",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemScheduleOneTime": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule_one_time",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemScheduleRecurring": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule_recurring",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_OneTime": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_Recurring": ".scheduled_messages_list_scheduled_messages_response_scheduled_messages_item_schedule",
    "ScheduledMessagesRetrieveScheduledMessageResponse": ".scheduled_messages_retrieve_scheduled_message_response",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessage": ".scheduled_messages_retrieve_scheduled_message_response_message",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageIncludeReturnMessageTypesItem": ".scheduled_messages_retrieve_scheduled_message_response_message_include_return_message_types_item",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItem": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContent": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImage": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSource": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_image_source_type",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemText": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item_text",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Image": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Text": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_content_zero_item",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemRole": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_role",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemType": ".scheduled_messages_retrieve_scheduled_message_response_message_messages_item_type",
    "ScheduledMessagesRetrieveScheduledMessageResponseSchedule": ".scheduled_messages_retrieve_scheduled_message_response_schedule",
    "ScheduledMessagesRetrieveScheduledMessageResponseScheduleOneTime": ".scheduled_messages_retrieve_scheduled_message_response_schedule_one_time",
    "ScheduledMessagesRetrieveScheduledMessageResponseScheduleRecurring": ".scheduled_messages_retrieve_scheduled_message_response_schedule_recurring",
    "ScheduledMessagesRetrieveScheduledMessageResponseSchedule_OneTime": ".scheduled_messages_retrieve_scheduled_message_response_schedule",
    "ScheduledMessagesRetrieveScheduledMessageResponseSchedule_Recurring": ".scheduled_messages_retrieve_scheduled_message_response_schedule",
    "ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem": ".scheduled_messages_schedule_agent_message_request_include_return_message_types_item",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItem": ".scheduled_messages_schedule_agent_message_request_messages_item",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContent": ".scheduled_messages_schedule_agent_message_request_messages_item_content",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImage": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSourceType": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_image_source_type",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemText": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item_text",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Image": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text": ".scheduled_messages_schedule_agent_message_request_messages_item_content_zero_item",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole": ".scheduled_messages_schedule_agent_message_request_messages_item_role",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemType": ".scheduled_messages_schedule_agent_message_request_messages_item_type",
    "ScheduledMessagesScheduleAgentMessageRequestSchedule": ".scheduled_messages_schedule_agent_message_request_schedule",
    "ScheduledMessagesScheduleAgentMessageRequestScheduleOneTime": ".scheduled_messages_schedule_agent_message_request_schedule_one_time",
    "ScheduledMessagesScheduleAgentMessageRequestScheduleRecurring": ".scheduled_messages_schedule_agent_message_request_schedule_recurring",
    "ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime": ".scheduled_messages_schedule_agent_message_request_schedule",
    "ScheduledMessagesScheduleAgentMessageRequestSchedule_Recurring": ".scheduled_messages_schedule_agent_message_request_schedule",
    "ScheduledMessagesScheduleAgentMessageResponse": ".scheduled_messages_schedule_agent_message_response",
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
    "ScheduledMessagesDeleteScheduledMessageRequestBody",
    "ScheduledMessagesDeleteScheduledMessageResponse",
    "ScheduledMessagesListScheduledMessagesResponse",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItem",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessage",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageIncludeReturnMessageTypesItem",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItem",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContent",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImage",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSource",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemImageSourceType",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItemText",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem_Image",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemContentZeroItem_Text",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemRole",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemMessageMessagesItemType",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemScheduleOneTime",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemScheduleRecurring",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_OneTime",
    "ScheduledMessagesListScheduledMessagesResponseScheduledMessagesItemSchedule_Recurring",
    "ScheduledMessagesRetrieveScheduledMessageResponse",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessage",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageIncludeReturnMessageTypesItem",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItem",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContent",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImage",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSource",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemImageSourceType",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItemText",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Image",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemContentZeroItem_Text",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemRole",
    "ScheduledMessagesRetrieveScheduledMessageResponseMessageMessagesItemType",
    "ScheduledMessagesRetrieveScheduledMessageResponseSchedule",
    "ScheduledMessagesRetrieveScheduledMessageResponseScheduleOneTime",
    "ScheduledMessagesRetrieveScheduledMessageResponseScheduleRecurring",
    "ScheduledMessagesRetrieveScheduledMessageResponseSchedule_OneTime",
    "ScheduledMessagesRetrieveScheduledMessageResponseSchedule_Recurring",
    "ScheduledMessagesScheduleAgentMessageRequestIncludeReturnMessageTypesItem",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItem",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContent",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImage",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSource",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemImageSourceType",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItemText",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Image",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemContentZeroItem_Text",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemRole",
    "ScheduledMessagesScheduleAgentMessageRequestMessagesItemType",
    "ScheduledMessagesScheduleAgentMessageRequestSchedule",
    "ScheduledMessagesScheduleAgentMessageRequestScheduleOneTime",
    "ScheduledMessagesScheduleAgentMessageRequestScheduleRecurring",
    "ScheduledMessagesScheduleAgentMessageRequestSchedule_OneTime",
    "ScheduledMessagesScheduleAgentMessageRequestSchedule_Recurring",
    "ScheduledMessagesScheduleAgentMessageResponse",
]
