



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_team_response import CreateTeamResponse
    from .delete_team_response import DeleteTeamResponse
    from .get_team_response import GetTeamResponse
    from .get_teams_request_filter_date_field import GetTeamsRequestFilterDateField
    from .get_teams_request_order import GetTeamsRequestOrder
    from .get_teams_request_sort_by import GetTeamsRequestSortBy
    from .get_teams_response import GetTeamsResponse
    from .get_teams_response_data_item import GetTeamsResponseDataItem
    from .get_teams_response_meta import GetTeamsResponseMeta
    from .update_team_response import UpdateTeamResponse
_dynamic_imports: typing.Dict[str, str] = {
    "CreateTeamResponse": ".create_team_response",
    "DeleteTeamResponse": ".delete_team_response",
    "GetTeamResponse": ".get_team_response",
    "GetTeamsRequestFilterDateField": ".get_teams_request_filter_date_field",
    "GetTeamsRequestOrder": ".get_teams_request_order",
    "GetTeamsRequestSortBy": ".get_teams_request_sort_by",
    "GetTeamsResponse": ".get_teams_response",
    "GetTeamsResponseDataItem": ".get_teams_response_data_item",
    "GetTeamsResponseMeta": ".get_teams_response_meta",
    "UpdateTeamResponse": ".update_team_response",
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
    "CreateTeamResponse",
    "DeleteTeamResponse",
    "GetTeamResponse",
    "GetTeamsRequestFilterDateField",
    "GetTeamsRequestOrder",
    "GetTeamsRequestSortBy",
    "GetTeamsResponse",
    "GetTeamsResponseDataItem",
    "GetTeamsResponseMeta",
    "UpdateTeamResponse",
]
