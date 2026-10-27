



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_team_request import CreateTeamRequest
    from .create_team_request_channels import CreateTeamRequestChannels
    from .create_team_request_channels_channels_item import CreateTeamRequestChannelsChannelsItem
    from .create_team_request_channels_visibility import CreateTeamRequestChannelsVisibility
    from .create_team_request_group_odata_bind import CreateTeamRequestGroupOdataBind
    from .get_team_request_expand import GetTeamRequestExpand
    from .list_all_teams_response import ListAllTeamsResponse
    from .list_joined_teams_response import ListJoinedTeamsResponse
    from .update_team_request_visibility import UpdateTeamRequestVisibility
_dynamic_imports: typing.Dict[str, str] = {
    "CreateTeamRequest": ".create_team_request",
    "CreateTeamRequestChannels": ".create_team_request_channels",
    "CreateTeamRequestChannelsChannelsItem": ".create_team_request_channels_channels_item",
    "CreateTeamRequestChannelsVisibility": ".create_team_request_channels_visibility",
    "CreateTeamRequestGroupOdataBind": ".create_team_request_group_odata_bind",
    "GetTeamRequestExpand": ".get_team_request_expand",
    "ListAllTeamsResponse": ".list_all_teams_response",
    "ListJoinedTeamsResponse": ".list_joined_teams_response",
    "UpdateTeamRequestVisibility": ".update_team_request_visibility",
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
    "CreateTeamRequest",
    "CreateTeamRequestChannels",
    "CreateTeamRequestChannelsChannelsItem",
    "CreateTeamRequestChannelsVisibility",
    "CreateTeamRequestGroupOdataBind",
    "GetTeamRequestExpand",
    "ListAllTeamsResponse",
    "ListJoinedTeamsResponse",
    "UpdateTeamRequestVisibility",
]
