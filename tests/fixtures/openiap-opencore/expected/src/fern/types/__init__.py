



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .ace import Ace
    from .ace_rights import AceRights
    from .collection import Collection
    from .collection_type import CollectionType
    from .create_collection_options_timeseries import CreateCollectionOptionsTimeseries
    from .i_record_of_any import IRecordOfAny
    from .i_string_to_string_dictionary import IStringToStringDictionary
    from .open_rpa_workflow_creation_params import OpenRpaWorkflowCreationParams
    from .pick_user_name_or_email_or_username_or_newpassword import PickUserNameOrEmailOrUsernameOrNewpassword
    from .pick_workflow_name_or_background_or_serializable_or_filename_or_projectandname_or_xaml import (
        PickWorkflowNameOrBackgroundOrSerializableOrFilenameOrProjectandnameOrXaml,
    )
    from .query_params_sort import QueryParamsSort
    from .user import User
    from .user_creation_params import UserCreationParams
    from .workflow import Workflow
    from .workflow_parameter import WorkflowParameter
    from .workflow_parameter_direction import WorkflowParameterDirection
_dynamic_imports: typing.Dict[str, str] = {
    "Ace": ".ace",
    "AceRights": ".ace_rights",
    "Collection": ".collection",
    "CollectionType": ".collection_type",
    "CreateCollectionOptionsTimeseries": ".create_collection_options_timeseries",
    "IRecordOfAny": ".i_record_of_any",
    "IStringToStringDictionary": ".i_string_to_string_dictionary",
    "OpenRpaWorkflowCreationParams": ".open_rpa_workflow_creation_params",
    "PickUserNameOrEmailOrUsernameOrNewpassword": ".pick_user_name_or_email_or_username_or_newpassword",
    "PickWorkflowNameOrBackgroundOrSerializableOrFilenameOrProjectandnameOrXaml": ".pick_workflow_name_or_background_or_serializable_or_filename_or_projectandname_or_xaml",
    "QueryParamsSort": ".query_params_sort",
    "User": ".user",
    "UserCreationParams": ".user_creation_params",
    "Workflow": ".workflow",
    "WorkflowParameter": ".workflow_parameter",
    "WorkflowParameterDirection": ".workflow_parameter_direction",
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
    "Ace",
    "AceRights",
    "Collection",
    "CollectionType",
    "CreateCollectionOptionsTimeseries",
    "IRecordOfAny",
    "IStringToStringDictionary",
    "OpenRpaWorkflowCreationParams",
    "PickUserNameOrEmailOrUsernameOrNewpassword",
    "PickWorkflowNameOrBackgroundOrSerializableOrFilenameOrProjectandnameOrXaml",
    "QueryParamsSort",
    "User",
    "UserCreationParams",
    "Workflow",
    "WorkflowParameter",
    "WorkflowParameterDirection",
]
