



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .add_composable_to_cart_request_data import AddComposableToCartRequestData
    from .add_composable_to_cart_request_data_attributes import AddComposableToCartRequestDataAttributes
    from .add_composable_to_cart_request_data_attributes_components_item import (
        AddComposableToCartRequestDataAttributesComponentsItem,
    )
    from .add_composable_to_cart_request_data_attributes_composable import (
        AddComposableToCartRequestDataAttributesComposable,
    )
    from .forgot_password_request_data import ForgotPasswordRequestData
    from .forgot_password_request_data_attributes import ForgotPasswordRequestDataAttributes
    from .new_password_request_data import NewPasswordRequestData
    from .new_password_request_data_attributes import NewPasswordRequestDataAttributes
    from .register_request_data import RegisterRequestData
    from .register_request_data_attributes import RegisterRequestDataAttributes
    from .register_without_password_request_data import RegisterWithoutPasswordRequestData
    from .register_without_password_request_data_attributes import RegisterWithoutPasswordRequestDataAttributes
_dynamic_imports: typing.Dict[str, str] = {
    "AddComposableToCartRequestData": ".add_composable_to_cart_request_data",
    "AddComposableToCartRequestDataAttributes": ".add_composable_to_cart_request_data_attributes",
    "AddComposableToCartRequestDataAttributesComponentsItem": ".add_composable_to_cart_request_data_attributes_components_item",
    "AddComposableToCartRequestDataAttributesComposable": ".add_composable_to_cart_request_data_attributes_composable",
    "ForgotPasswordRequestData": ".forgot_password_request_data",
    "ForgotPasswordRequestDataAttributes": ".forgot_password_request_data_attributes",
    "NewPasswordRequestData": ".new_password_request_data",
    "NewPasswordRequestDataAttributes": ".new_password_request_data_attributes",
    "RegisterRequestData": ".register_request_data",
    "RegisterRequestDataAttributes": ".register_request_data_attributes",
    "RegisterWithoutPasswordRequestData": ".register_without_password_request_data",
    "RegisterWithoutPasswordRequestDataAttributes": ".register_without_password_request_data_attributes",
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
    "AddComposableToCartRequestData",
    "AddComposableToCartRequestDataAttributes",
    "AddComposableToCartRequestDataAttributesComponentsItem",
    "AddComposableToCartRequestDataAttributesComposable",
    "ForgotPasswordRequestData",
    "ForgotPasswordRequestDataAttributes",
    "NewPasswordRequestData",
    "NewPasswordRequestDataAttributes",
    "RegisterRequestData",
    "RegisterRequestDataAttributes",
    "RegisterWithoutPasswordRequestData",
    "RegisterWithoutPasswordRequestDataAttributes",
]
