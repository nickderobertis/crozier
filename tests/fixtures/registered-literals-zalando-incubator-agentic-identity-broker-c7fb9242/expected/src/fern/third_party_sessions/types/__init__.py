



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_affected_agents_response import GetAffectedAgentsResponse
    from .get_affected_agents_response_data import GetAffectedAgentsResponseData
    from .get_session_details_response import GetSessionDetailsResponse
    from .get_session_details_response_data import GetSessionDetailsResponseData
    from .list_third_party_sessions_response import ListThirdPartySessionsResponse
    from .refresh_third_party_session_response import RefreshThirdPartySessionResponse
    from .terminate_session_response import TerminateSessionResponse
    from .terminate_session_response_data import TerminateSessionResponseData
_dynamic_imports: typing.Dict[str, str] = {
    "GetAffectedAgentsResponse": ".get_affected_agents_response",
    "GetAffectedAgentsResponseData": ".get_affected_agents_response_data",
    "GetSessionDetailsResponse": ".get_session_details_response",
    "GetSessionDetailsResponseData": ".get_session_details_response_data",
    "ListThirdPartySessionsResponse": ".list_third_party_sessions_response",
    "RefreshThirdPartySessionResponse": ".refresh_third_party_session_response",
    "TerminateSessionResponse": ".terminate_session_response",
    "TerminateSessionResponseData": ".terminate_session_response_data",
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
    "GetAffectedAgentsResponse",
    "GetAffectedAgentsResponseData",
    "GetSessionDetailsResponse",
    "GetSessionDetailsResponseData",
    "ListThirdPartySessionsResponse",
    "RefreshThirdPartySessionResponse",
    "TerminateSessionResponse",
    "TerminateSessionResponseData",
]
