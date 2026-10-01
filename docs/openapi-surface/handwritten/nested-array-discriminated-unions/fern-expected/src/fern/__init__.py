



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Animal,
        Animal_Bird,
        Animal_Fish,
        Bird,
        Cat,
        Dog,
        ExplicitGrid,
        ExplicitGridItemItem,
        ExplicitGridItemItem_Cat,
        ExplicitGridItemItem_Dog,
        Fish,
        Grids,
        InferredAnyGrid,
        InferredAnyGridItemItem,
        InferredAnyGridItemItem_Cat,
        InferredAnyGridItemItem_Dog,
        InferredGrid,
        InferredGridItemItem,
        InferredGridItemItem_Cat,
        InferredGridItemItem_Dog,
        InheritedGrid,
        Pet,
        Pet_Cat,
        Pet_Dog,
    )
    from ._default_clients import DefaultAioHttpClient, DefaultAsyncHttpxClient
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "Animal": ".types",
    "Animal_Bird": ".types",
    "Animal_Fish": ".types",
    "AsyncFernApi": ".client",
    "Bird": ".types",
    "Cat": ".types",
    "DefaultAioHttpClient": "._default_clients",
    "DefaultAsyncHttpxClient": "._default_clients",
    "Dog": ".types",
    "ExplicitGrid": ".types",
    "ExplicitGridItemItem": ".types",
    "ExplicitGridItemItem_Cat": ".types",
    "ExplicitGridItemItem_Dog": ".types",
    "FernApi": ".client",
    "Fish": ".types",
    "Grids": ".types",
    "InferredAnyGrid": ".types",
    "InferredAnyGridItemItem": ".types",
    "InferredAnyGridItemItem_Cat": ".types",
    "InferredAnyGridItemItem_Dog": ".types",
    "InferredGrid": ".types",
    "InferredGridItemItem": ".types",
    "InferredGridItemItem_Cat": ".types",
    "InferredGridItemItem_Dog": ".types",
    "InheritedGrid": ".types",
    "Pet": ".types",
    "Pet_Cat": ".types",
    "Pet_Dog": ".types",
    "__version__": ".version",
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
    "AsyncFernApi",
    "Bird",
    "Cat",
    "DefaultAioHttpClient",
    "DefaultAsyncHttpxClient",
    "Dog",
    "ExplicitGrid",
    "ExplicitGridItemItem",
    "ExplicitGridItemItem_Cat",
    "ExplicitGridItemItem_Dog",
    "FernApi",
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
    "__version__",
]
