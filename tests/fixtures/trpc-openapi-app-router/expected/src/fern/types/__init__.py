



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .address import Address
    from .category import Category
    from .default_error_data import DefaultErrorData
    from .default_error_data_code import DefaultErrorDataCode
    from .default_error_shape import DefaultErrorShape
    from .echo_response import EchoResponse
    from .echo_response_result import EchoResponseResult
    from .greeting_response import GreetingResponse
    from .greeting_response_result import GreetingResponseResult
    from .greeting_response_result_data import GreetingResponseResultData
    from .linked_list_node import LinkedListNode
    from .no_input_response import NoInputResponse
    from .no_input_response_result import NoInputResponseResult
    from .order_item import OrderItem
    from .tree_node import TreeNode
    from .user_profile import UserProfile
_dynamic_imports: typing.Dict[str, str] = {
    "Address": ".address",
    "Category": ".category",
    "DefaultErrorData": ".default_error_data",
    "DefaultErrorDataCode": ".default_error_data_code",
    "DefaultErrorShape": ".default_error_shape",
    "EchoResponse": ".echo_response",
    "EchoResponseResult": ".echo_response_result",
    "GreetingResponse": ".greeting_response",
    "GreetingResponseResult": ".greeting_response_result",
    "GreetingResponseResultData": ".greeting_response_result_data",
    "LinkedListNode": ".linked_list_node",
    "NoInputResponse": ".no_input_response",
    "NoInputResponseResult": ".no_input_response_result",
    "OrderItem": ".order_item",
    "TreeNode": ".tree_node",
    "UserProfile": ".user_profile",
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
    "Address",
    "Category",
    "DefaultErrorData",
    "DefaultErrorDataCode",
    "DefaultErrorShape",
    "EchoResponse",
    "EchoResponseResult",
    "GreetingResponse",
    "GreetingResponseResult",
    "GreetingResponseResultData",
    "LinkedListNode",
    "NoInputResponse",
    "NoInputResponseResult",
    "OrderItem",
    "TreeNode",
    "UserProfile",
]
