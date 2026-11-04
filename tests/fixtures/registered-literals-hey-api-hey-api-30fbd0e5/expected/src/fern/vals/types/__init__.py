



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .branches_list2response import BranchesList2Response
    from .file_content_update2request_type import FileContentUpdate2RequestType
    from .files_create2request_body import FilesCreate2RequestBody
    from .files_create2request_body_one import FilesCreate2RequestBodyOne
    from .files_create2request_body_one_type import FilesCreate2RequestBodyOneType
    from .files_create2request_body_zero import FilesCreate2RequestBodyZero
    from .files_create2request_body_zero_type import FilesCreate2RequestBodyZeroType
    from .val_environment_variable_groups_list_response import ValEnvironmentVariableGroupsListResponse
    from .val_environment_variable_groups_list_response_data_item import (
        ValEnvironmentVariableGroupsListResponseDataItem,
    )
    from .val_environment_variables_list_response import ValEnvironmentVariablesListResponse
    from .val_files_get2response import ValFilesGet2Response
    from .vals_create2request_privacy import ValsCreate2RequestPrivacy
    from .vals_list2request_privacy import ValsList2RequestPrivacy
    from .vals_list2response import ValsList2Response
_dynamic_imports: typing.Dict[str, str] = {
    "BranchesList2Response": ".branches_list2response",
    "FileContentUpdate2RequestType": ".file_content_update2request_type",
    "FilesCreate2RequestBody": ".files_create2request_body",
    "FilesCreate2RequestBodyOne": ".files_create2request_body_one",
    "FilesCreate2RequestBodyOneType": ".files_create2request_body_one_type",
    "FilesCreate2RequestBodyZero": ".files_create2request_body_zero",
    "FilesCreate2RequestBodyZeroType": ".files_create2request_body_zero_type",
    "ValEnvironmentVariableGroupsListResponse": ".val_environment_variable_groups_list_response",
    "ValEnvironmentVariableGroupsListResponseDataItem": ".val_environment_variable_groups_list_response_data_item",
    "ValEnvironmentVariablesListResponse": ".val_environment_variables_list_response",
    "ValFilesGet2Response": ".val_files_get2response",
    "ValsCreate2RequestPrivacy": ".vals_create2request_privacy",
    "ValsList2RequestPrivacy": ".vals_list2request_privacy",
    "ValsList2Response": ".vals_list2response",
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
    "BranchesList2Response",
    "FileContentUpdate2RequestType",
    "FilesCreate2RequestBody",
    "FilesCreate2RequestBodyOne",
    "FilesCreate2RequestBodyOneType",
    "FilesCreate2RequestBodyZero",
    "FilesCreate2RequestBodyZeroType",
    "ValEnvironmentVariableGroupsListResponse",
    "ValEnvironmentVariableGroupsListResponseDataItem",
    "ValEnvironmentVariablesListResponse",
    "ValFilesGet2Response",
    "ValsCreate2RequestPrivacy",
    "ValsList2RequestPrivacy",
    "ValsList2Response",
]
