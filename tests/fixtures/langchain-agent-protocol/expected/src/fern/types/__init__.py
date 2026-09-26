



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .agent import Agent
    from .agent_capabilities import AgentCapabilities
    from .agent_schema import AgentSchema
    from .error_response import ErrorResponse
    from .item import Item
    from .list_namespace_response import ListNamespaceResponse
    from .message import Message
    from .message_content import MessageContent
    from .message_content_one_item import MessageContentOneItem
    from .message_content_one_item_one import MessageContentOneItemOne
    from .message_content_one_item_text import MessageContentOneItemText
    from .message_content_one_item_text_type import MessageContentOneItemTextType
    from .run import Run
    from .run_create import RunCreate
    from .run_create_config import RunCreateConfig
    from .run_create_if_not_exists import RunCreateIfNotExists
    from .run_create_input import RunCreateInput
    from .run_create_on_completion import RunCreateOnCompletion
    from .run_create_on_disconnect import RunCreateOnDisconnect
    from .run_status import RunStatus
    from .run_stream import RunStream
    from .run_stream_stream_mode import RunStreamStreamMode
    from .run_wait_response import RunWaitResponse
    from .search_items_response import SearchItemsResponse
    from .stream_mode import StreamMode
    from .streaming_channel import StreamingChannel
    from .streaming_channel_zero import StreamingChannelZero
    from .streaming_command_response import (
        StreamingCommandResponse,
        StreamingCommandResponse_Error,
        StreamingCommandResponse_Success,
    )
    from .streaming_error_response import StreamingErrorResponse
    from .streaming_event import StreamingEvent
    from .streaming_event_type import StreamingEventType
    from .streaming_namespace import StreamingNamespace
    from .streaming_success_response import StreamingSuccessResponse
    from .streaming_success_response_meta import StreamingSuccessResponseMeta
    from .thread import Thread
    from .thread_checkpoint import ThreadCheckpoint
    from .thread_state import ThreadState
    from .thread_status import ThreadStatus
_dynamic_imports: typing.Dict[str, str] = {
    "Agent": ".agent",
    "AgentCapabilities": ".agent_capabilities",
    "AgentSchema": ".agent_schema",
    "ErrorResponse": ".error_response",
    "Item": ".item",
    "ListNamespaceResponse": ".list_namespace_response",
    "Message": ".message",
    "MessageContent": ".message_content",
    "MessageContentOneItem": ".message_content_one_item",
    "MessageContentOneItemOne": ".message_content_one_item_one",
    "MessageContentOneItemText": ".message_content_one_item_text",
    "MessageContentOneItemTextType": ".message_content_one_item_text_type",
    "Run": ".run",
    "RunCreate": ".run_create",
    "RunCreateConfig": ".run_create_config",
    "RunCreateIfNotExists": ".run_create_if_not_exists",
    "RunCreateInput": ".run_create_input",
    "RunCreateOnCompletion": ".run_create_on_completion",
    "RunCreateOnDisconnect": ".run_create_on_disconnect",
    "RunStatus": ".run_status",
    "RunStream": ".run_stream",
    "RunStreamStreamMode": ".run_stream_stream_mode",
    "RunWaitResponse": ".run_wait_response",
    "SearchItemsResponse": ".search_items_response",
    "StreamMode": ".stream_mode",
    "StreamingChannel": ".streaming_channel",
    "StreamingChannelZero": ".streaming_channel_zero",
    "StreamingCommandResponse": ".streaming_command_response",
    "StreamingCommandResponse_Error": ".streaming_command_response",
    "StreamingCommandResponse_Success": ".streaming_command_response",
    "StreamingErrorResponse": ".streaming_error_response",
    "StreamingEvent": ".streaming_event",
    "StreamingEventType": ".streaming_event_type",
    "StreamingNamespace": ".streaming_namespace",
    "StreamingSuccessResponse": ".streaming_success_response",
    "StreamingSuccessResponseMeta": ".streaming_success_response_meta",
    "Thread": ".thread",
    "ThreadCheckpoint": ".thread_checkpoint",
    "ThreadState": ".thread_state",
    "ThreadStatus": ".thread_status",
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
    "Agent",
    "AgentCapabilities",
    "AgentSchema",
    "ErrorResponse",
    "Item",
    "ListNamespaceResponse",
    "Message",
    "MessageContent",
    "MessageContentOneItem",
    "MessageContentOneItemOne",
    "MessageContentOneItemText",
    "MessageContentOneItemTextType",
    "Run",
    "RunCreate",
    "RunCreateConfig",
    "RunCreateIfNotExists",
    "RunCreateInput",
    "RunCreateOnCompletion",
    "RunCreateOnDisconnect",
    "RunStatus",
    "RunStream",
    "RunStreamStreamMode",
    "RunWaitResponse",
    "SearchItemsResponse",
    "StreamMode",
    "StreamingChannel",
    "StreamingChannelZero",
    "StreamingCommandResponse",
    "StreamingCommandResponse_Error",
    "StreamingCommandResponse_Success",
    "StreamingErrorResponse",
    "StreamingEvent",
    "StreamingEventType",
    "StreamingNamespace",
    "StreamingSuccessResponse",
    "StreamingSuccessResponseMeta",
    "Thread",
    "ThreadCheckpoint",
    "ThreadState",
    "ThreadStatus",
]
