



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        GetV1TmsPendingStarterTaskforcesResponse,
        GetV1TmsPendingStarterTaskforcesResponseMqprofiles,
        GetV1TmsPendingStopperTaskforcesResponse,
        PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse,
        PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse,
        PostV1TmsCondorRmTaskforcesTaskforceUuidResponse,
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse,
        PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse,
        PostV1TmsStatusesTaskforcesResponse,
        PostV1TmsStatusesTaskforcesResponseResultsItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "GetV1TmsPendingStarterTaskforcesResponse": ".types",
    "GetV1TmsPendingStarterTaskforcesResponseMqprofiles": ".types",
    "GetV1TmsPendingStopperTaskforcesResponse": ".types",
    "PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse": ".types",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse": ".types",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidResponse": ".types",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse": ".types",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse": ".types",
    "PostV1TmsStatusesTaskforcesResponse": ".types",
    "PostV1TmsStatusesTaskforcesResponseResultsItem": ".types",
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
    "GetV1TmsPendingStarterTaskforcesResponse",
    "GetV1TmsPendingStarterTaskforcesResponseMqprofiles",
    "GetV1TmsPendingStopperTaskforcesResponse",
    "PostV1TmsCondorCompleteTaskforcesTaskforceUuidResponse",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidFailedResponse",
    "PostV1TmsCondorRmTaskforcesTaskforceUuidResponse",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidFailedResponse",
    "PostV1TmsCondorSubmitTaskforcesTaskforceUuidResponse",
    "PostV1TmsStatusesTaskforcesResponse",
    "PostV1TmsStatusesTaskforcesResponseResultsItem",
]
