



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .close_room_response import CloseRoomResponse
    from .collect_room_response import CollectRoomResponse
    from .finalize_room_response import FinalizeRoomResponse
    from .get_room_task_response import GetRoomTaskResponse
    from .list_room_attachments_response import ListRoomAttachmentsResponse
    from .list_room_messages_response import ListRoomMessagesResponse
    from .send_room_message_request_body import SendRoomMessageRequestBody
    from .send_room_message_response import SendRoomMessageResponse
    from .upload_room_attachment_response import UploadRoomAttachmentResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CloseRoomResponse": ".close_room_response",
    "CollectRoomResponse": ".collect_room_response",
    "FinalizeRoomResponse": ".finalize_room_response",
    "GetRoomTaskResponse": ".get_room_task_response",
    "ListRoomAttachmentsResponse": ".list_room_attachments_response",
    "ListRoomMessagesResponse": ".list_room_messages_response",
    "SendRoomMessageRequestBody": ".send_room_message_request_body",
    "SendRoomMessageResponse": ".send_room_message_response",
    "UploadRoomAttachmentResponse": ".upload_room_attachment_response",
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
    "CloseRoomResponse",
    "CollectRoomResponse",
    "FinalizeRoomResponse",
    "GetRoomTaskResponse",
    "ListRoomAttachmentsResponse",
    "ListRoomMessagesResponse",
    "SendRoomMessageRequestBody",
    "SendRoomMessageResponse",
    "UploadRoomAttachmentResponse",
]
