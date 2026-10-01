



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .cat import Cat
    from .dog import Dog
    from .get_variants_response import GetVariantsResponse
    from .get_variants_response_five import GetVariantsResponseFive
    from .get_variants_response_four_item import GetVariantsResponseFourItem
    from .get_variants_response_one import GetVariantsResponseOne
    from .get_variants_response_seven_item import (
        GetVariantsResponseSevenItem,
        GetVariantsResponseSevenItem_Cat,
        GetVariantsResponseSevenItem_Dog,
    )
    from .get_variants_response_three_item import GetVariantsResponseThreeItem
    from .get_variants_response_two_item import GetVariantsResponseTwoItem
    from .get_variants_response_zero import GetVariantsResponseZero
    from .target import Target
_dynamic_imports: typing.Dict[str, str] = {
    "Cat": ".cat",
    "Dog": ".dog",
    "GetVariantsResponse": ".get_variants_response",
    "GetVariantsResponseFive": ".get_variants_response_five",
    "GetVariantsResponseFourItem": ".get_variants_response_four_item",
    "GetVariantsResponseOne": ".get_variants_response_one",
    "GetVariantsResponseSevenItem": ".get_variants_response_seven_item",
    "GetVariantsResponseSevenItem_Cat": ".get_variants_response_seven_item",
    "GetVariantsResponseSevenItem_Dog": ".get_variants_response_seven_item",
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
    "Cat",
    "Dog",
    "GetVariantsResponse",
    "GetVariantsResponseFive",
    "GetVariantsResponseFourItem",
    "GetVariantsResponseOne",
    "GetVariantsResponseSevenItem",
    "GetVariantsResponseSevenItem_Cat",
    "GetVariantsResponseSevenItem_Dog",
    "GetVariantsResponseThreeItem",
    "GetVariantsResponseTwoItem",
    "GetVariantsResponseZero",
    "Target",
]
