



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        V2GroundCreateJobResponse,
        V2GroundCreateJobResponseStatus,
        V2GroundGetJobResponse,
        V2GroundGetJobResponseError,
        V2GroundGetJobResponseResult,
        V2GroundGetJobResponseStatus,
        V2GroundListJobsResponse,
        V2GroundListJobsResponseJobsItem,
        V2GroundListJobsResponseJobsItemStatus,
        V2GroundRunSyncResponse,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "V2GroundCreateJobResponse": ".types",
    "V2GroundCreateJobResponseStatus": ".types",
    "V2GroundGetJobResponse": ".types",
    "V2GroundGetJobResponseError": ".types",
    "V2GroundGetJobResponseResult": ".types",
    "V2GroundGetJobResponseStatus": ".types",
    "V2GroundListJobsResponse": ".types",
    "V2GroundListJobsResponseJobsItem": ".types",
    "V2GroundListJobsResponseJobsItemStatus": ".types",
    "V2GroundRunSyncResponse": ".types",
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
    "V2GroundCreateJobResponse",
    "V2GroundCreateJobResponseStatus",
    "V2GroundGetJobResponse",
    "V2GroundGetJobResponseError",
    "V2GroundGetJobResponseResult",
    "V2GroundGetJobResponseStatus",
    "V2GroundListJobsResponse",
    "V2GroundListJobsResponseJobsItem",
    "V2GroundListJobsResponseJobsItemStatus",
    "V2GroundRunSyncResponse",
]
