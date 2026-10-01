



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_variants_response import GetVariantsResponse
    from .get_variants_response_four import GetVariantsResponseFour
    from .get_variants_response_one_item import GetVariantsResponseOneItem
    from .get_variants_response_three_item import GetVariantsResponseThreeItem
    from .get_variants_response_two_item import GetVariantsResponseTwoItem
    from .get_variants_response_zero import GetVariantsResponseZero
    from .target import Target
_dynamic_imports: typing.Dict[str, str] = {
    "GetVariantsResponse": ".get_variants_response",
    "GetVariantsResponseFour": ".get_variants_response_four",
    "GetVariantsResponseOneItem": ".get_variants_response_one_item",
    "GetVariantsResponseThreeItem": ".get_variants_response_three_item",
    "GetVariantsResponseTwoItem": ".get_variants_response_two_item",
    "GetVariantsResponseZero": ".get_variants_response_zero",
    "Target": ".target",
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
    "GetVariantsResponse",
    "GetVariantsResponseFour",
    "GetVariantsResponseOneItem",
    "GetVariantsResponseThreeItem",
    "GetVariantsResponseTwoItem",
    "GetVariantsResponseZero",
    "Target",
]
