



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .body_login_to_create_access_token import BodyLoginToCreateAccessToken
    from .http_validation_error import HttpValidationError
    from .meta import Meta
    from .saved_payment_method import SavedPaymentMethod
    from .token import Token
    from .token_token_type import TokenTokenType
    from .validation_error import ValidationError
    from .validation_error_loc_item import ValidationErrorLocItem
_dynamic_imports: typing.Dict[str, str] = {
    "BodyLoginToCreateAccessToken": ".body_login_to_create_access_token",
    "HttpValidationError": ".http_validation_error",
    "Meta": ".meta",
    "SavedPaymentMethod": ".saved_payment_method",
    "Token": ".token",
    "TokenTokenType": ".token_token_type",
    "ValidationError": ".validation_error",
    "ValidationErrorLocItem": ".validation_error_loc_item",
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
    "BodyLoginToCreateAccessToken",
    "HttpValidationError",
    "Meta",
    "SavedPaymentMethod",
    "Token",
    "TokenTokenType",
    "ValidationError",
    "ValidationErrorLocItem",
]
