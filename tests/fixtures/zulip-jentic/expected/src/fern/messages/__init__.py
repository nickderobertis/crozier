



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CheckMessagesMatchNarrowResponse,
        CheckMessagesMatchNarrowResponseMessagesValue,
        CheckThumbnailStatusResponse,
        GetFileTemporaryUrlResponse,
        GetMessageHistoryResponse,
        GetMessageHistoryResponseMessageHistoryItem,
        GetMessageResponse,
        GetMessageResponseMessage,
        GetMessageResponseMessageDisplayRecipient,
        GetMessageResponseMessageDisplayRecipientOneItem,
        GetMessageResponseMessageEditHistoryItem,
        GetMessageResponseMessageSubmessagesItem,
        GetMessageResponseMessageTopicLinksItem,
        GetMessagesResponse,
        GetMessagesResponseMessagesItem,
        GetMessagesResponseMessagesItemDisplayRecipient,
        GetMessagesResponseMessagesItemDisplayRecipientOneItem,
        GetMessagesResponseMessagesItemEditHistoryItem,
        GetMessagesResponseMessagesItemSubmessagesItem,
        GetMessagesResponseMessagesItemTopicLinksItem,
        GetReadReceiptsResponse,
        MarkAllAsReadResponse,
        RenderMessageResponse,
        SendMessageRequestTo,
        SendMessageRequestType,
        SendMessageResponse,
        UpdateMessageFlagsForNarrowRequestNarrowItem,
        UpdateMessageFlagsForNarrowRequestNarrowItemNegated,
        UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand,
        UpdateMessageFlagsForNarrowRequestOp,
        UpdateMessageFlagsForNarrowResponse,
        UpdateMessageFlagsRequestOp,
        UpdateMessageFlagsResponse,
        UpdateMessageRequestPropagateMode,
        UpdateMessageResponse,
        UploadFileResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CheckMessagesMatchNarrowResponse": ".types",
    "CheckMessagesMatchNarrowResponseMessagesValue": ".types",
    "CheckThumbnailStatusResponse": ".types",
    "GetFileTemporaryUrlResponse": ".types",
    "GetMessageHistoryResponse": ".types",
    "GetMessageHistoryResponseMessageHistoryItem": ".types",
    "GetMessageResponse": ".types",
    "GetMessageResponseMessage": ".types",
    "GetMessageResponseMessageDisplayRecipient": ".types",
    "GetMessageResponseMessageDisplayRecipientOneItem": ".types",
    "GetMessageResponseMessageEditHistoryItem": ".types",
    "GetMessageResponseMessageSubmessagesItem": ".types",
    "GetMessageResponseMessageTopicLinksItem": ".types",
    "GetMessagesResponse": ".types",
    "GetMessagesResponseMessagesItem": ".types",
    "GetMessagesResponseMessagesItemDisplayRecipient": ".types",
    "GetMessagesResponseMessagesItemDisplayRecipientOneItem": ".types",
    "GetMessagesResponseMessagesItemEditHistoryItem": ".types",
    "GetMessagesResponseMessagesItemSubmessagesItem": ".types",
    "GetMessagesResponseMessagesItemTopicLinksItem": ".types",
    "GetReadReceiptsResponse": ".types",
    "MarkAllAsReadResponse": ".types",
    "RenderMessageResponse": ".types",
    "SendMessageRequestTo": ".types",
    "SendMessageRequestType": ".types",
    "SendMessageResponse": ".types",
    "UpdateMessageFlagsForNarrowRequestNarrowItem": ".types",
    "UpdateMessageFlagsForNarrowRequestNarrowItemNegated": ".types",
    "UpdateMessageFlagsForNarrowRequestNarrowItemNegatedOperand": ".types",
    "UpdateMessageFlagsForNarrowRequestOp": ".types",
    "UpdateMessageFlagsForNarrowResponse": ".types",
    "UpdateMessageFlagsRequestOp": ".types",
    "UpdateMessageFlagsResponse": ".types",
    "UpdateMessageRequestPropagateMode": ".types",
    "UpdateMessageResponse": ".types",
    "UploadFileResponse": ".types",
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
