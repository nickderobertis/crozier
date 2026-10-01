



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .account import Account
    from .account_category import AccountCategory
    from .accounts_webhook import AccountsWebhook
    from .categorised_account import CategorisedAccount
    from .drawing import Drawing
    from .shape import Shape
    from .shape_radius import ShapeRadius
    from .shape_side import ShapeSide
_dynamic_imports: typing.Dict[str, str] = {
    "Account": ".account",
    "AccountCategory": ".account_category",
    "AccountsWebhook": ".accounts_webhook",
    "CategorisedAccount": ".categorised_account",
    "Drawing": ".drawing",
    "Shape": ".shape",
    "ShapeRadius": ".shape_radius",
    "ShapeSide": ".shape_side",
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
    "Account",
    "AccountCategory",
    "AccountsWebhook",
    "CategorisedAccount",
    "Drawing",
    "Shape",
    "ShapeRadius",
    "ShapeSide",
]
