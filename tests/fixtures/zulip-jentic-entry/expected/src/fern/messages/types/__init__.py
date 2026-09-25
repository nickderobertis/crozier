



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .check_messages_match_narrow_response import CheckMessagesMatchNarrowResponse
    from .check_messages_match_narrow_response_messages_value import CheckMessagesMatchNarrowResponseMessagesValue
    from .check_thumbnail_status_response import CheckThumbnailStatusResponse
    from .get_file_temporary_url_response import GetFileTemporaryUrlResponse
    from .get_message_history_response import GetMessageHistoryResponse
    from .get_message_history_response_message_history_item import GetMessageHistoryResponseMessageHistoryItem
    from .get_message_response import GetMessageResponse
    from .get_message_response_message import GetMessageResponseMessage
    from .get_message_response_message_display_recipient import GetMessageResponseMessageDisplayRecipient
    from .get_message_response_message_display_recipient_one_item import (
        GetMessageResponseMessageDisplayRecipientOneItem,
    )
    from .get_message_response_message_edit_history_item import GetMessageResponseMessageEditHistoryItem
    from .get_message_response_message_submessages_item import GetMessageResponseMessageSubmessagesItem
    from .get_message_response_message_topic_links_item import GetMessageResponseMessageTopicLinksItem
    from .get_messages_response import GetMessagesResponse
    from .get_messages_response_messages_item import GetMessagesResponseMessagesItem
    from .get_messages_response_messages_item_display_recipient import GetMessagesResponseMessagesItemDisplayRecipient
    from .get_messages_response_messages_item_display_recipient_one_item import (
        GetMessagesResponseMessagesItemDisplayRecipientOneItem,
    )
    from .get_messages_response_messages_item_edit_history_item import GetMessagesResponseMessagesItemEditHistoryItem
    from .get_messages_response_messages_item_submessages_item import GetMessagesResponseMessagesItemSubmessagesItem
    from .get_messages_response_messages_item_topic_links_item import GetMessagesResponseMessagesItemTopicLinksItem
    from .get_read_receipts_response import GetReadReceiptsResponse
    from .mark_all_as_read_response import MarkAllAsReadResponse
    from .render_message_response import RenderMessageResponse
    from .send_message_request_to import SendMessageRequestTo
    from .send_message_request_type import SendMessageRequestType
    from .send_message_response import SendMessageResponse
    from .update_message_flags_for_narrow_request_narrow_item import UpdateMessageFlagsForNarrowRequestNarrowItem
    from .update_message_flags_for_narrow_request_narrow_item_negated import (
        UpdateMessageFlagsForNarrowRequestNarrowItemNegated,
    )
    from .update_message_flags_for_narrow_request_narrow_item_negated_operand import (
        UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand,
    )
    from .update_message_flags_for_narrow_request_op import UpdateMessageFlagsForNarrowRequestOp
    from .update_message_flags_for_narrow_response import UpdateMessageFlagsForNarrowResponse
    from .update_message_flags_request_op import UpdateMessageFlagsRequestOp
    from .update_message_flags_response import UpdateMessageFlagsResponse
    from .update_message_request_propagate_mode import UpdateMessageRequestPropagateMode
    from .update_message_response import UpdateMessageResponse
    from .upload_file_response import UploadFileResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CheckMessagesMatchNarrowResponse": ".check_messages_match_narrow_response",
    "CheckMessagesMatchNarrowResponseMessagesValue": ".check_messages_match_narrow_response_messages_value",
    "CheckThumbnailStatusResponse": ".check_thumbnail_status_response",
    "GetFileTemporaryUrlResponse": ".get_file_temporary_url_response",
    "GetMessageHistoryResponse": ".get_message_history_response",
    "GetMessageHistoryResponseMessageHistoryItem": ".get_message_history_response_message_history_item",
    "GetMessageResponse": ".get_message_response",
    "GetMessageResponseMessage": ".get_message_response_message",
    "GetMessageResponseMessageDisplayRecipient": ".get_message_response_message_display_recipient",
    "GetMessageResponseMessageDisplayRecipientOneItem": ".get_message_response_message_display_recipient_one_item",
    "GetMessageResponseMessageEditHistoryItem": ".get_message_response_message_edit_history_item",
    "GetMessageResponseMessageSubmessagesItem": ".get_message_response_message_submessages_item",
    "GetMessageResponseMessageTopicLinksItem": ".get_message_response_message_topic_links_item",
    "GetMessagesResponse": ".get_messages_response",
    "GetMessagesResponseMessagesItem": ".get_messages_response_messages_item",
    "GetMessagesResponseMessagesItemDisplayRecipient": ".get_messages_response_messages_item_display_recipient",
    "GetMessagesResponseMessagesItemDisplayRecipientOneItem": ".get_messages_response_messages_item_display_recipient_one_item",
    "GetMessagesResponseMessagesItemEditHistoryItem": ".get_messages_response_messages_item_edit_history_item",
    "GetMessagesResponseMessagesItemSubmessagesItem": ".get_messages_response_messages_item_submessages_item",
    "GetMessagesResponseMessagesItemTopicLinksItem": ".get_messages_response_messages_item_topic_links_item",
    "GetReadReceiptsResponse": ".get_read_receipts_response",
    "MarkAllAsReadResponse": ".mark_all_as_read_response",
    "RenderMessageResponse": ".render_message_response",
    "SendMessageRequestTo": ".send_message_request_to",
    "SendMessageRequestType": ".send_message_request_type",
    "SendMessageResponse": ".send_message_response",
    "UpdateMessageFlagsForNarrowRequestNarrowItem": ".update_message_flags_for_narrow_request_narrow_item",
    "UpdateMessageFlagsForNarrowRequestNarrowItemNegated": ".update_message_flags_for_narrow_request_narrow_item_negated",
    "UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand": ".update_message_flags_for_narrow_request_narrow_item_negated_operand",
    "UpdateMessageFlagsForNarrowRequestOp": ".update_message_flags_for_narrow_request_op",
    "UpdateMessageFlagsForNarrowResponse": ".update_message_flags_for_narrow_response",
    "UpdateMessageFlagsRequestOp": ".update_message_flags_request_op",
    "UpdateMessageFlagsResponse": ".update_message_flags_response",
    "UpdateMessageRequestPropagateMode": ".update_message_request_propagate_mode",
    "UpdateMessageResponse": ".update_message_response",
    "UploadFileResponse": ".upload_file_response",
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
    "CheckMessagesMatchNarrowResponse",
    "CheckMessagesMatchNarrowResponseMessagesValue",
    "CheckThumbnailStatusResponse",
    "GetFileTemporaryUrlResponse",
    "GetMessageHistoryResponse",
    "GetMessageHistoryResponseMessageHistoryItem",
    "GetMessageResponse",
    "GetMessageResponseMessage",
    "GetMessageResponseMessageDisplayRecipient",
    "GetMessageResponseMessageDisplayRecipientOneItem",
    "GetMessageResponseMessageEditHistoryItem",
    "GetMessageResponseMessageSubmessagesItem",
    "GetMessageResponseMessageTopicLinksItem",
    "GetMessagesResponse",
    "GetMessagesResponseMessagesItem",
    "GetMessagesResponseMessagesItemDisplayRecipient",
    "GetMessagesResponseMessagesItemDisplayRecipientOneItem",
    "GetMessagesResponseMessagesItemEditHistoryItem",
    "GetMessagesResponseMessagesItemSubmessagesItem",
    "GetMessagesResponseMessagesItemTopicLinksItem",
    "GetReadReceiptsResponse",
    "MarkAllAsReadResponse",
    "RenderMessageResponse",
    "SendMessageRequestTo",
    "SendMessageRequestType",
    "SendMessageResponse",
    "UpdateMessageFlagsForNarrowRequestNarrowItem",
    "UpdateMessageFlagsForNarrowRequestNarrowItemNegated",
    "UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand",
    "UpdateMessageFlagsForNarrowRequestOp",
    "UpdateMessageFlagsForNarrowResponse",
    "UpdateMessageFlagsRequestOp",
    "UpdateMessageFlagsResponse",
    "UpdateMessageRequestPropagateMode",
    "UpdateMessageResponse",
    "UploadFileResponse",
]
