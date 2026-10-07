



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .api_response import ApiResponse
    from .category import Category
    from .oauth_scope import OauthScope
    from .order import Order
    from .order_status import OrderStatus
    from .pet import Pet
    from .pet_status import PetStatus
    from .tag import Tag
    from .user import User
_dynamic_imports: typing.Dict[str, str] = {
    "ApiResponse": ".api_response",
    "Category": ".category",
    "OauthScope": ".oauth_scope",
    "Order": ".order",
    "OrderStatus": ".order_status",
    "Pet": ".pet",
    "PetStatus": ".pet_status",
    "Tag": ".tag",
    "User": ".user",
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


__all__ = ["ApiResponse", "Category", "OauthScope", "Order", "OrderStatus", "Pet", "PetStatus", "Tag", "User"]
