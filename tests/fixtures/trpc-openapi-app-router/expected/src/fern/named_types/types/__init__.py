



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .named_types_deep_nested_response import NamedTypesDeepNestedResponse
    from .named_types_deep_nested_response_result import NamedTypesDeepNestedResponseResult
    from .named_types_deep_nested_response_result_data import NamedTypesDeepNestedResponseResultData
    from .named_types_deep_nested_response_result_data_data import NamedTypesDeepNestedResponseResultDataData
    from .named_types_deep_nested_response_result_data_data_nested import (
        NamedTypesDeepNestedResponseResultDataDataNested,
    )
    from .named_types_order_items_response import NamedTypesOrderItemsResponse
    from .named_types_order_items_response_result import NamedTypesOrderItemsResponseResult
    from .named_types_order_items_response_result_data import NamedTypesOrderItemsResponseResultData
    from .named_types_profile_and_address_response import NamedTypesProfileAndAddressResponse
    from .named_types_profile_and_address_response_result import NamedTypesProfileAndAddressResponseResult
    from .named_types_profile_and_address_response_result_data import NamedTypesProfileAndAddressResponseResultData
    from .named_types_with_address_response import NamedTypesWithAddressResponse
    from .named_types_with_address_response_result import NamedTypesWithAddressResponseResult
    from .named_types_with_address_response_result_data import NamedTypesWithAddressResponseResultData
    from .named_types_with_profile_response import NamedTypesWithProfileResponse
    from .named_types_with_profile_response_result import NamedTypesWithProfileResponseResult
    from .named_types_with_profile_response_result_data import NamedTypesWithProfileResponseResultData
_dynamic_imports: typing.Dict[str, str] = {
    "NamedTypesDeepNestedResponse": ".named_types_deep_nested_response",
    "NamedTypesDeepNestedResponseResult": ".named_types_deep_nested_response_result",
    "NamedTypesDeepNestedResponseResultData": ".named_types_deep_nested_response_result_data",
    "NamedTypesDeepNestedResponseResultDataData": ".named_types_deep_nested_response_result_data_data",
    "NamedTypesDeepNestedResponseResultDataDataNested": ".named_types_deep_nested_response_result_data_data_nested",
    "NamedTypesOrderItemsResponse": ".named_types_order_items_response",
    "NamedTypesOrderItemsResponseResult": ".named_types_order_items_response_result",
    "NamedTypesOrderItemsResponseResultData": ".named_types_order_items_response_result_data",
    "NamedTypesProfileAndAddressResponse": ".named_types_profile_and_address_response",
    "NamedTypesProfileAndAddressResponseResult": ".named_types_profile_and_address_response_result",
    "NamedTypesProfileAndAddressResponseResultData": ".named_types_profile_and_address_response_result_data",
    "NamedTypesWithAddressResponse": ".named_types_with_address_response",
    "NamedTypesWithAddressResponseResult": ".named_types_with_address_response_result",
    "NamedTypesWithAddressResponseResultData": ".named_types_with_address_response_result_data",
    "NamedTypesWithProfileResponse": ".named_types_with_profile_response",
    "NamedTypesWithProfileResponseResult": ".named_types_with_profile_response_result",
    "NamedTypesWithProfileResponseResultData": ".named_types_with_profile_response_result_data",
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
    "NamedTypesDeepNestedResponse",
    "NamedTypesDeepNestedResponseResult",
    "NamedTypesDeepNestedResponseResultData",
    "NamedTypesDeepNestedResponseResultDataData",
    "NamedTypesDeepNestedResponseResultDataDataNested",
    "NamedTypesOrderItemsResponse",
    "NamedTypesOrderItemsResponseResult",
    "NamedTypesOrderItemsResponseResultData",
    "NamedTypesProfileAndAddressResponse",
    "NamedTypesProfileAndAddressResponseResult",
    "NamedTypesProfileAndAddressResponseResultData",
    "NamedTypesWithAddressResponse",
    "NamedTypesWithAddressResponseResult",
    "NamedTypesWithAddressResponseResultData",
    "NamedTypesWithProfileResponse",
    "NamedTypesWithProfileResponseResult",
    "NamedTypesWithProfileResponseResultData",
]
