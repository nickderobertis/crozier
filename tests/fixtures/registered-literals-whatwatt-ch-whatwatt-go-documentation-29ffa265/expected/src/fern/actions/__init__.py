



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        CallActionResponse,
        GetActionStatusResponseItem,
        GetActionsResponse,
        GetActionsResponseActionsItem,
        GetActionsResponseActionsItemRequestsItem,
        GetActionsResponseActionsItemRequestsItemHttp,
        GetActionsResponseActionsItemRequestsItemHttpMethod,
        GetActionsResponseActionsItemRequestsItemModbus,
        GetActionsResponseActionsItemRequestsItemModbusType,
        GetActionsResponseConstValue,
        SetActionsRequestActionsItem,
        SetActionsRequestActionsItemRequestsItem,
        SetActionsRequestActionsItemRequestsItemHttp,
        SetActionsRequestActionsItemRequestsItemHttpMethod,
        SetActionsRequestActionsItemRequestsItemModbus,
        SetActionsRequestActionsItemRequestsItemModbusType,
        SetActionsRequestConstValue,
        SetActionsResponse,
        SetActionsResponseActionsItem,
        SetActionsResponseActionsItemRequestsItem,
        SetActionsResponseActionsItemRequestsItemHttp,
        SetActionsResponseActionsItemRequestsItemHttpMethod,
        SetActionsResponseActionsItemRequestsItemModbus,
        SetActionsResponseActionsItemRequestsItemModbusType,
        SetActionsResponseConstValue,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "CallActionResponse": ".types",
    "GetActionStatusResponseItem": ".types",
    "GetActionsResponse": ".types",
    "GetActionsResponseActionsItem": ".types",
    "GetActionsResponseActionsItemRequestsItem": ".types",
    "GetActionsResponseActionsItemRequestsItemHttp": ".types",
    "GetActionsResponseActionsItemRequestsItemHttpMethod": ".types",
    "GetActionsResponseActionsItemRequestsItemModbus": ".types",
    "GetActionsResponseActionsItemRequestsItemModbusType": ".types",
    "GetActionsResponseConstValue": ".types",
    "SetActionsRequestActionsItem": ".types",
    "SetActionsRequestActionsItemRequestsItem": ".types",
    "SetActionsRequestActionsItemRequestsItemHttp": ".types",
    "SetActionsRequestActionsItemRequestsItemHttpMethod": ".types",
    "SetActionsRequestActionsItemRequestsItemModbus": ".types",
    "SetActionsRequestActionsItemRequestsItemModbusType": ".types",
    "SetActionsRequestConstValue": ".types",
    "SetActionsResponse": ".types",
    "SetActionsResponseActionsItem": ".types",
    "SetActionsResponseActionsItemRequestsItem": ".types",
    "SetActionsResponseActionsItemRequestsItemHttp": ".types",
    "SetActionsResponseActionsItemRequestsItemHttpMethod": ".types",
    "SetActionsResponseActionsItemRequestsItemModbus": ".types",
    "SetActionsResponseActionsItemRequestsItemModbusType": ".types",
    "SetActionsResponseConstValue": ".types",
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
    "CallActionResponse",
    "GetActionStatusResponseItem",
    "GetActionsResponse",
    "GetActionsResponseActionsItem",
    "GetActionsResponseActionsItemRequestsItem",
    "GetActionsResponseActionsItemRequestsItemHttp",
    "GetActionsResponseActionsItemRequestsItemHttpMethod",
    "GetActionsResponseActionsItemRequestsItemModbus",
    "GetActionsResponseActionsItemRequestsItemModbusType",
    "GetActionsResponseConstValue",
    "SetActionsRequestActionsItem",
    "SetActionsRequestActionsItemRequestsItem",
    "SetActionsRequestActionsItemRequestsItemHttp",
    "SetActionsRequestActionsItemRequestsItemHttpMethod",
    "SetActionsRequestActionsItemRequestsItemModbus",
    "SetActionsRequestActionsItemRequestsItemModbusType",
    "SetActionsRequestConstValue",
    "SetActionsResponse",
    "SetActionsResponseActionsItem",
    "SetActionsResponseActionsItemRequestsItem",
    "SetActionsResponseActionsItemRequestsItemHttp",
    "SetActionsResponseActionsItemRequestsItemHttpMethod",
    "SetActionsResponseActionsItemRequestsItemModbus",
    "SetActionsResponseActionsItemRequestsItemModbusType",
    "SetActionsResponseConstValue",
]
