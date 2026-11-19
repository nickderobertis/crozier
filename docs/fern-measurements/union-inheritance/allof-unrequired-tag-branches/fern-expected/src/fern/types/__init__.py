



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cart import Cart
    from .fixed_cart import FixedCart
    from .floor_shelf import FloorShelf
    from .floor_shelf_type import FloorShelfType
    from .rolling_cart import RollingCart
    from .shelf import Shelf
    from .shelf_base import ShelfBase
    from .shelf_type import ShelfType
    from .wall_shelf import WallShelf
    from .wall_shelf_type import WallShelfType
_dynamic_imports: typing.Dict[str, str] = {
    "Cart": ".cart",
    "FixedCart": ".fixed_cart",
    "FloorShelf": ".floor_shelf",
    "FloorShelfType": ".floor_shelf_type",
    "RollingCart": ".rolling_cart",
    "Shelf": ".shelf",
    "ShelfBase": ".shelf_base",
    "ShelfType": ".shelf_type",
    "WallShelf": ".wall_shelf",
    "WallShelfType": ".wall_shelf_type",
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
    "Cart",
    "FixedCart",
    "FloorShelf",
    "FloorShelfType",
    "RollingCart",
    "Shelf",
    "ShelfBase",
    "ShelfType",
    "WallShelf",
    "WallShelfType",
]
