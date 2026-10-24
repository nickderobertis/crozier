



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .agent_check_request import AgentCheckRequest
    from .agent_check_response import AgentCheckResponse
    from .agent_check_response_next_actions_item import AgentCheckResponseNextActionsItem
    from .agent_check_response_role import AgentCheckResponseRole
    from .agent_close_request import AgentCloseRequest
    from .agent_close_response import AgentCloseResponse
    from .agent_close_response_role import AgentCloseResponseRole
    from .agent_collect_request import AgentCollectRequest
    from .agent_collect_response import AgentCollectResponse
    from .agent_collect_response_role import AgentCollectResponseRole
    from .agent_final_request import AgentFinalRequest
    from .agent_final_response import AgentFinalResponse
    from .agent_final_response_next_actions_item import AgentFinalResponseNextActionsItem
    from .agent_final_response_role import AgentFinalResponseRole
    from .agent_finish_request import AgentFinishRequest
    from .agent_finish_response import AgentFinishResponse
    from .agent_finish_response_next_actions_item import AgentFinishResponseNextActionsItem
    from .agent_finish_response_role import AgentFinishResponseRole
    from .agent_join_request import AgentJoinRequest
    from .agent_join_response import AgentJoinResponse
    from .agent_say_request import AgentSayRequest
    from .agent_say_response import AgentSayResponse
    from .agent_say_response_next_actions_item import AgentSayResponseNextActionsItem
    from .agent_say_response_role import AgentSayResponseRole
    from .created_room import CreatedRoom
    from .error import Error
    from .room_attachment import RoomAttachment
    from .room_final import RoomFinal
    from .room_message import RoomMessage
    from .room_message_role import RoomMessageRole
    from .room_status import RoomStatus
    from .room_status_status import RoomStatusStatus
    from .sha256 import Sha256
_dynamic_imports: typing.Dict[str, str] = {
    "AgentCheckRequest": ".agent_check_request",
    "AgentCheckResponse": ".agent_check_response",
    "AgentCheckResponseNextActionsItem": ".agent_check_response_next_actions_item",
    "AgentCheckResponseRole": ".agent_check_response_role",
    "AgentCloseRequest": ".agent_close_request",
    "AgentCloseResponse": ".agent_close_response",
    "AgentCloseResponseRole": ".agent_close_response_role",
    "AgentCollectRequest": ".agent_collect_request",
    "AgentCollectResponse": ".agent_collect_response",
    "AgentCollectResponseRole": ".agent_collect_response_role",
    "AgentFinalRequest": ".agent_final_request",
    "AgentFinalResponse": ".agent_final_response",
    "AgentFinalResponseNextActionsItem": ".agent_final_response_next_actions_item",
    "AgentFinalResponseRole": ".agent_final_response_role",
    "AgentFinishRequest": ".agent_finish_request",
    "AgentFinishResponse": ".agent_finish_response",
    "AgentFinishResponseNextActionsItem": ".agent_finish_response_next_actions_item",
    "AgentFinishResponseRole": ".agent_finish_response_role",
    "AgentJoinRequest": ".agent_join_request",
    "AgentJoinResponse": ".agent_join_response",
    "AgentSayRequest": ".agent_say_request",
    "AgentSayResponse": ".agent_say_response",
    "AgentSayResponseNextActionsItem": ".agent_say_response_next_actions_item",
    "AgentSayResponseRole": ".agent_say_response_role",
    "CreatedRoom": ".created_room",
    "Error": ".error",
    "RoomAttachment": ".room_attachment",
    "RoomFinal": ".room_final",
    "RoomMessage": ".room_message",
    "RoomMessageRole": ".room_message_role",
    "RoomStatus": ".room_status",
    "RoomStatusStatus": ".room_status_status",
    "Sha256": ".sha256",
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
    "AgentCheckRequest",
    "AgentCheckResponse",
    "AgentCheckResponseNextActionsItem",
    "AgentCheckResponseRole",
    "AgentCloseRequest",
    "AgentCloseResponse",
    "AgentCloseResponseRole",
    "AgentCollectRequest",
    "AgentCollectResponse",
    "AgentCollectResponseRole",
    "AgentFinalRequest",
    "AgentFinalResponse",
    "AgentFinalResponseNextActionsItem",
    "AgentFinalResponseRole",
    "AgentFinishRequest",
    "AgentFinishResponse",
    "AgentFinishResponseNextActionsItem",
    "AgentFinishResponseRole",
    "AgentJoinRequest",
    "AgentJoinResponse",
    "AgentSayRequest",
    "AgentSayResponse",
    "AgentSayResponseNextActionsItem",
    "AgentSayResponseRole",
    "CreatedRoom",
    "Error",
    "RoomAttachment",
    "RoomFinal",
    "RoomMessage",
    "RoomMessageRole",
    "RoomStatus",
    "RoomStatusStatus",
    "Sha256",
]
