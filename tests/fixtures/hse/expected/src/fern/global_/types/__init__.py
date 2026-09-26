



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .kmc_vmstat_get_response_item import KmcVmstatGetResponseItem
    from .param_get_response import ParamGetResponse
    from .param_set_request_body import ParamSetRequestBody
    from .params_get_response import ParamsGetResponse
    from .workqueues_get_response_item import WorkqueuesGetResponseItem
    from .workqueues_get_response_item_state import WorkqueuesGetResponseItemState
_dynamic_imports: typing.Dict[str, str] = {
    "KmcVmstatGetResponseItem": ".kmc_vmstat_get_response_item",
    "ParamGetResponse": ".param_get_response",
    "ParamSetRequestBody": ".param_set_request_body",
    "ParamsGetResponse": ".params_get_response",
    "WorkqueuesGetResponseItem": ".workqueues_get_response_item",
    "WorkqueuesGetResponseItemState": ".workqueues_get_response_item_state",
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
    "KmcVmstatGetResponseItem",
    "ParamGetResponse",
    "ParamSetRequestBody",
    "ParamsGetResponse",
    "WorkqueuesGetResponseItem",
    "WorkqueuesGetResponseItemState",
]
