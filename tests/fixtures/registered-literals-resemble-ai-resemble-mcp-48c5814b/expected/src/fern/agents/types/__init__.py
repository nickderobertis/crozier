



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_agent_request_asr import CreateAgentRequestAsr
    from .create_agent_request_asr_user_input_audio_format import CreateAgentRequestAsrUserInputAudioFormat
    from .create_agent_request_dynamic_variables_value import CreateAgentRequestDynamicVariablesValue
    from .create_agent_request_llm import CreateAgentRequestLlm
    from .create_agent_request_search_mode import CreateAgentRequestSearchMode
    from .create_agent_request_turn import CreateAgentRequestTurn
    from .create_agent_request_turn_mode import CreateAgentRequestTurnMode
    from .create_agent_response import CreateAgentResponse
    from .delete_agent_response import DeleteAgentResponse
    from .dispatch_agent_response import DispatchAgentResponse
    from .get_agent_capabilities_response import GetAgentCapabilitiesResponse
    from .get_agent_capabilities_response_asr_capabilities_item import GetAgentCapabilitiesResponseAsrCapabilitiesItem
    from .get_agent_capabilities_response_llm_capabilities_item import GetAgentCapabilitiesResponseLlmCapabilitiesItem
    from .get_agent_response import GetAgentResponse
    from .get_system_tools_response import GetSystemToolsResponse
    from .list_agents_response import ListAgentsResponse
    from .update_agent_request_search_mode import UpdateAgentRequestSearchMode
    from .update_agent_response import UpdateAgentResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateAgentRequestAsr": ".create_agent_request_asr",
    "CreateAgentRequestAsrUserInputAudioFormat": ".create_agent_request_asr_user_input_audio_format",
    "CreateAgentRequestDynamicVariablesValue": ".create_agent_request_dynamic_variables_value",
    "CreateAgentRequestLlm": ".create_agent_request_llm",
    "CreateAgentRequestSearchMode": ".create_agent_request_search_mode",
    "CreateAgentRequestTurn": ".create_agent_request_turn",
    "CreateAgentRequestTurnMode": ".create_agent_request_turn_mode",
    "CreateAgentResponse": ".create_agent_response",
    "DeleteAgentResponse": ".delete_agent_response",
    "DispatchAgentResponse": ".dispatch_agent_response",
    "GetAgentCapabilitiesResponse": ".get_agent_capabilities_response",
    "GetAgentCapabilitiesResponseAsrCapabilitiesItem": ".get_agent_capabilities_response_asr_capabilities_item",
    "GetAgentCapabilitiesResponseLlmCapabilitiesItem": ".get_agent_capabilities_response_llm_capabilities_item",
    "GetAgentResponse": ".get_agent_response",
    "GetSystemToolsResponse": ".get_system_tools_response",
    "ListAgentsResponse": ".list_agents_response",
    "UpdateAgentRequestSearchMode": ".update_agent_request_search_mode",
    "UpdateAgentResponse": ".update_agent_response",
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
    "CreateAgentRequestAsr",
    "CreateAgentRequestAsrUserInputAudioFormat",
    "CreateAgentRequestDynamicVariablesValue",
    "CreateAgentRequestLlm",
    "CreateAgentRequestSearchMode",
    "CreateAgentRequestTurn",
    "CreateAgentRequestTurnMode",
    "CreateAgentResponse",
    "DeleteAgentResponse",
    "DispatchAgentResponse",
    "GetAgentCapabilitiesResponse",
    "GetAgentCapabilitiesResponseAsrCapabilitiesItem",
    "GetAgentCapabilitiesResponseLlmCapabilitiesItem",
    "GetAgentResponse",
    "GetSystemToolsResponse",
    "ListAgentsResponse",
    "UpdateAgentRequestSearchMode",
    "UpdateAgentResponse",
]
