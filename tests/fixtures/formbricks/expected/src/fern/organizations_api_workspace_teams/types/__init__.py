



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_workspace_team_request_permission import CreateWorkspaceTeamRequestPermission
    from .create_workspace_team_response import CreateWorkspaceTeamResponse
    from .create_workspace_team_response_permission import CreateWorkspaceTeamResponsePermission
    from .delete_workspace_team_response import DeleteWorkspaceTeamResponse
    from .delete_workspace_team_response_permission import DeleteWorkspaceTeamResponsePermission
    from .get_workspace_teams_request_filter_date_field import GetWorkspaceTeamsRequestFilterDateField
    from .get_workspace_teams_request_order import GetWorkspaceTeamsRequestOrder
    from .get_workspace_teams_request_sort_by import GetWorkspaceTeamsRequestSortBy
    from .get_workspace_teams_response import GetWorkspaceTeamsResponse
    from .get_workspace_teams_response_data_item import GetWorkspaceTeamsResponseDataItem
    from .get_workspace_teams_response_data_item_permission import GetWorkspaceTeamsResponseDataItemPermission
    from .get_workspace_teams_response_meta import GetWorkspaceTeamsResponseMeta
    from .update_workspace_team_request_permission import UpdateWorkspaceTeamRequestPermission
    from .update_workspace_team_response import UpdateWorkspaceTeamResponse
    from .update_workspace_team_response_permission import UpdateWorkspaceTeamResponsePermission
_dynamic_imports: typing.Dict[str, str] = {
    "CreateWorkspaceTeamRequestPermission": ".create_workspace_team_request_permission",
    "CreateWorkspaceTeamResponse": ".create_workspace_team_response",
    "CreateWorkspaceTeamResponsePermission": ".create_workspace_team_response_permission",
    "DeleteWorkspaceTeamResponse": ".delete_workspace_team_response",
    "DeleteWorkspaceTeamResponsePermission": ".delete_workspace_team_response_permission",
    "GetWorkspaceTeamsRequestFilterDateField": ".get_workspace_teams_request_filter_date_field",
    "GetWorkspaceTeamsRequestOrder": ".get_workspace_teams_request_order",
    "GetWorkspaceTeamsRequestSortBy": ".get_workspace_teams_request_sort_by",
    "GetWorkspaceTeamsResponse": ".get_workspace_teams_response",
    "GetWorkspaceTeamsResponseDataItem": ".get_workspace_teams_response_data_item",
    "GetWorkspaceTeamsResponseDataItemPermission": ".get_workspace_teams_response_data_item_permission",
    "GetWorkspaceTeamsResponseMeta": ".get_workspace_teams_response_meta",
    "UpdateWorkspaceTeamRequestPermission": ".update_workspace_team_request_permission",
    "UpdateWorkspaceTeamResponse": ".update_workspace_team_response",
    "UpdateWorkspaceTeamResponsePermission": ".update_workspace_team_response_permission",
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
    "CreateWorkspaceTeamRequestPermission",
    "CreateWorkspaceTeamResponse",
    "CreateWorkspaceTeamResponsePermission",
    "DeleteWorkspaceTeamResponse",
    "DeleteWorkspaceTeamResponsePermission",
    "GetWorkspaceTeamsRequestFilterDateField",
    "GetWorkspaceTeamsRequestOrder",
    "GetWorkspaceTeamsRequestSortBy",
    "GetWorkspaceTeamsResponse",
    "GetWorkspaceTeamsResponseDataItem",
    "GetWorkspaceTeamsResponseDataItemPermission",
    "GetWorkspaceTeamsResponseMeta",
    "UpdateWorkspaceTeamRequestPermission",
    "UpdateWorkspaceTeamResponse",
    "UpdateWorkspaceTeamResponsePermission",
]
