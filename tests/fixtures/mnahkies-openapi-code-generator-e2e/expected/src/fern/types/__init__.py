



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .animal import Animal, Animal_Cat, Animal_Dog
    from .cat import Cat
    from .dog import Dog
    from .enumerations import Enumerations
    from .enumerations_colors import EnumerationsColors
    from .product_order import ProductOrder
    from .product_order_address import ProductOrderAddress
    from .random_number import RandomNumber
    from .random_number_params import RandomNumberParams
_dynamic_imports: typing.Dict[str, str] = {
    "Animal": ".animal",
    "Animal_Cat": ".animal",
    "Animal_Dog": ".animal",
    "Cat": ".cat",
    "Dog": ".dog",
    "Enumerations": ".enumerations",
    "EnumerationsColors": ".enumerations_colors",
    "ProductOrder": ".product_order",
    "ProductOrderAddress": ".product_order_address",
    "RandomNumber": ".random_number",
    "RandomNumberParams": ".random_number_params",
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
    "Animal",
    "Animal_Cat",
    "Animal_Dog",
    "Cat",
    "Dog",
    "Enumerations",
    "EnumerationsColors",
    "ProductOrder",
    "ProductOrderAddress",
    "RandomNumber",
    "RandomNumberParams",
]
