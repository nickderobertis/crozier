



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import AndNode, LeafNode, Node, Node_And, Node_Leaf, TreeNode
    from . import pred, tree
    from .client import AsyncFernApi, FernApi
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AndNode": ".types",
    "AsyncFernApi": ".client",
    "FernApi": ".client",
    "LeafNode": ".types",
    "Node": ".types",
    "Node_And": ".types",
    "Node_Leaf": ".types",
    "TreeNode": ".types",
    "__version__": ".version",
    "pred": ".pred",
    "tree": ".tree",
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
    "AndNode",
    "AsyncFernApi",
    "FernApi",
    "LeafNode",
    "Node",
    "Node_And",
    "Node_Leaf",
    "TreeNode",
    "__version__",
    "pred",
    "tree",
]
