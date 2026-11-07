



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .call_action_response import CallActionResponse
    from .get_action_status_response_item import GetActionStatusResponseItem
    from .get_actions_response import GetActionsResponse
    from .get_actions_response_actions_item import GetActionsResponseActionsItem
    from .get_actions_response_actions_item_requests_item import GetActionsResponseActionsItemRequestsItem
    from .get_actions_response_actions_item_requests_item_http import GetActionsResponseActionsItemRequestsItemHttp
    from .get_actions_response_actions_item_requests_item_http_method import (
        GetActionsResponseActionsItemRequestsItemHttpMethod,
    )
    from .get_actions_response_actions_item_requests_item_modbus import GetActionsResponseActionsItemRequestsItemModbus
    from .get_actions_response_actions_item_requests_item_modbus_type import (
        GetActionsResponseActionsItemRequestsItemModbusType,
    )
    from .get_actions_response_const_value import GetActionsResponseConstValue
    from .set_actions_request_actions_item import SetActionsRequestActionsItem
    from .set_actions_request_actions_item_requests_item import SetActionsRequestActionsItemRequestsItem
    from .set_actions_request_actions_item_requests_item_http import SetActionsRequestActionsItemRequestsItemHttp
    from .set_actions_request_actions_item_requests_item_http_method import (
        SetActionsRequestActionsItemRequestsItemHttpMethod,
    )
    from .set_actions_request_actions_item_requests_item_modbus import SetActionsRequestActionsItemRequestsItemModbus
    from .set_actions_request_actions_item_requests_item_modbus_type import (
        SetActionsRequestActionsItemRequestsItemModbusType,
    )
    from .set_actions_request_const_value import SetActionsRequestConstValue
    from .set_actions_response import SetActionsResponse
    from .set_actions_response_actions_item import SetActionsResponseActionsItem
    from .set_actions_response_actions_item_requests_item import SetActionsResponseActionsItemRequestsItem
    from .set_actions_response_actions_item_requests_item_http import SetActionsResponseActionsItemRequestsItemHttp
    from .set_actions_response_actions_item_requests_item_http_method import (
        SetActionsResponseActionsItemRequestsItemHttpMethod,
    )
    from .set_actions_response_actions_item_requests_item_modbus import SetActionsResponseActionsItemRequestsItemModbus
    from .set_actions_response_actions_item_requests_item_modbus_type import (
        SetActionsResponseActionsItemRequestsItemModbusType,
    )
    from .set_actions_response_const_value import SetActionsResponseConstValue
_dynamic_imports: typing.Dict[str, str] = {
    "CallActionResponse": ".call_action_response",
    "GetActionStatusResponseItem": ".get_action_status_response_item",
    "GetActionsResponse": ".get_actions_response",
    "GetActionsResponseActionsItem": ".get_actions_response_actions_item",
    "GetActionsResponseActionsItemRequestsItem": ".get_actions_response_actions_item_requests_item",
    "GetActionsResponseActionsItemRequestsItemHttp": ".get_actions_response_actions_item_requests_item_http",
    "GetActionsResponseActionsItemRequestsItemHttpMethod": ".get_actions_response_actions_item_requests_item_http_method",
    "GetActionsResponseActionsItemRequestsItemModbus": ".get_actions_response_actions_item_requests_item_modbus",
    "GetActionsResponseActionsItemRequestsItemModbusType": ".get_actions_response_actions_item_requests_item_modbus_type",
    "GetActionsResponseConstValue": ".get_actions_response_const_value",
    "SetActionsRequestActionsItem": ".set_actions_request_actions_item",
    "SetActionsRequestActionsItemRequestsItem": ".set_actions_request_actions_item_requests_item",
    "SetActionsRequestActionsItemRequestsItemHttp": ".set_actions_request_actions_item_requests_item_http",
    "SetActionsRequestActionsItemRequestsItemHttpMethod": ".set_actions_request_actions_item_requests_item_http_method",
    "SetActionsRequestActionsItemRequestsItemModbus": ".set_actions_request_actions_item_requests_item_modbus",
    "SetActionsRequestActionsItemRequestsItemModbusType": ".set_actions_request_actions_item_requests_item_modbus_type",
    "SetActionsRequestConstValue": ".set_actions_request_const_value",
    "SetActionsResponse": ".set_actions_response",
    "SetActionsResponseActionsItem": ".set_actions_response_actions_item",
    "SetActionsResponseActionsItemRequestsItem": ".set_actions_response_actions_item_requests_item",
    "SetActionsResponseActionsItemRequestsItemHttp": ".set_actions_response_actions_item_requests_item_http",
    "SetActionsResponseActionsItemRequestsItemHttpMethod": ".set_actions_response_actions_item_requests_item_http_method",
    "SetActionsResponseActionsItemRequestsItemModbus": ".set_actions_response_actions_item_requests_item_modbus",
    "SetActionsResponseActionsItemRequestsItemModbusType": ".set_actions_response_actions_item_requests_item_modbus_type",
    "SetActionsResponseConstValue": ".set_actions_response_const_value",
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
