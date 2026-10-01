



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .animal import Animal, Animal_Bird, Animal_Fish
    from .bird import Bird
    from .cat import Cat
    from .dog import Dog
    from .explicit_grid import ExplicitGrid
    from .explicit_grid_item_item import ExplicitGridItemItem, ExplicitGridItemItem_Cat, ExplicitGridItemItem_Dog
    from .fish import Fish
    from .grids import Grids
    from .inferred_any_grid import InferredAnyGrid
    from .inferred_any_grid_item_item import (
        InferredAnyGridItemItem,
        InferredAnyGridItemItem_Cat,
        InferredAnyGridItemItem_Dog,
    )
    from .inferred_grid import InferredGrid
    from .inferred_grid_item_item import InferredGridItemItem, InferredGridItemItem_Cat, InferredGridItemItem_Dog
    from .inherited_grid import InheritedGrid
    from .pet import Pet, Pet_Cat, Pet_Dog
_dynamic_imports: typing.Dict[str, str] = {
    "Animal": ".animal",
    "Animal_Bird": ".animal",
    "Animal_Fish": ".animal",
    "Bird": ".bird",
    "Cat": ".cat",
    "Dog": ".dog",
    "ExplicitGrid": ".explicit_grid",
    "ExplicitGridItemItem": ".explicit_grid_item_item",
    "ExplicitGridItemItem_Cat": ".explicit_grid_item_item",
    "ExplicitGridItemItem_Dog": ".explicit_grid_item_item",
    "Fish": ".fish",
    "Grids": ".grids",
    "InferredAnyGrid": ".inferred_any_grid",
    "InferredAnyGridItemItem": ".inferred_any_grid_item_item",
    "InferredAnyGridItemItem_Cat": ".inferred_any_grid_item_item",
    "InferredAnyGridItemItem_Dog": ".inferred_any_grid_item_item",
    "InferredGrid": ".inferred_grid",
    "InferredGridItemItem": ".inferred_grid_item_item",
    "InferredGridItemItem_Cat": ".inferred_grid_item_item",
    "InferredGridItemItem_Dog": ".inferred_grid_item_item",
    "InheritedGrid": ".inherited_grid",
    "Pet": ".pet",
    "Pet_Cat": ".pet",
    "Pet_Dog": ".pet",
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
    "Animal_Bird",
    "Animal_Fish",
    "Bird",
    "Cat",
    "Dog",
    "ExplicitGrid",
    "ExplicitGridItemItem",
    "ExplicitGridItemItem_Cat",
    "ExplicitGridItemItem_Dog",
    "Fish",
    "Grids",
    "InferredAnyGrid",
    "InferredAnyGridItemItem",
    "InferredAnyGridItemItem_Cat",
    "InferredAnyGridItemItem_Dog",
    "InferredGrid",
    "InferredGridItemItem",
    "InferredGridItemItem_Cat",
    "InferredGridItemItem_Dog",
    "InheritedGrid",
    "Pet",
    "Pet_Cat",
    "Pet_Dog",
]
