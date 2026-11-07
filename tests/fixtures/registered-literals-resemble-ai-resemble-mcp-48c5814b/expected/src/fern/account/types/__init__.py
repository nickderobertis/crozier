



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_account_response import GetAccountResponse
    from .get_billing_usage_response import GetBillingUsageResponse
    from .get_team_response import GetTeamResponse
    from .get_team_response_item import GetTeamResponseItem
    from .get_teams_response import GetTeamsResponse
_dynamic_imports: typing.Dict[str, str] = {
    "GetAccountResponse": ".get_account_response",
    "GetBillingUsageResponse": ".get_billing_usage_response",
    "GetTeamResponse": ".get_team_response",
    "GetTeamResponseItem": ".get_team_response_item",
    "GetTeamsResponse": ".get_teams_response",
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
    "GetAccountResponse",
    "GetBillingUsageResponse",
    "GetTeamResponse",
    "GetTeamResponseItem",
    "GetTeamsResponse",
]
