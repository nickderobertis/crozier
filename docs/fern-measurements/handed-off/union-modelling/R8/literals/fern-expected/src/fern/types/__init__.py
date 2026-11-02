



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .link_patch import LinkPatch
    from .link_patch_item import LinkPatchItem
    from .link_patch_item_one import LinkPatchItemOne
    from .link_patch_item_one_op import LinkPatchItemOneOp
    from .link_patch_item_zero import LinkPatchItemZero
    from .link_patch_item_zero_op import LinkPatchItemZeroOp
    from .link_patch_item_zero_path import LinkPatchItemZeroPath
_dynamic_imports: typing.Dict[str, str] = {
    "LinkPatch": ".link_patch",
    "LinkPatchItem": ".link_patch_item",
    "LinkPatchItemOne": ".link_patch_item_one",
    "LinkPatchItemOneOp": ".link_patch_item_one_op",
    "LinkPatchItemZero": ".link_patch_item_zero",
    "LinkPatchItemZeroOp": ".link_patch_item_zero_op",
    "LinkPatchItemZeroPath": ".link_patch_item_zero_path",
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
    "LinkPatch",
    "LinkPatchItem",
    "LinkPatchItemOne",
    "LinkPatchItemOneOp",
    "LinkPatchItemZero",
    "LinkPatchItemZeroOp",
    "LinkPatchItemZeroPath",
]
