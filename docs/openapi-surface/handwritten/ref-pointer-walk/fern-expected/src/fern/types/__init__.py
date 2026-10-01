



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .choice import Choice
    from .choice_code import ChoiceCode
    from .composite import Composite
    from .either import Either
    from .either_flag import EitherFlag
    from .holder import Holder
    from .named import Named
    from .tag_list import TagList
    from .tag_list_item import TagListItem
    from .tag_list_item_tag import TagListItemTag
_dynamic_imports: typing.Dict[str, str] = {
    "Choice": ".choice",
    "ChoiceCode": ".choice_code",
    "Composite": ".composite",
    "Either": ".either",
    "EitherFlag": ".either_flag",
    "Holder": ".holder",
    "Named": ".named",
    "TagList": ".tag_list",
    "TagListItem": ".tag_list_item",
    "TagListItemTag": ".tag_list_item_tag",
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
    "Choice",
    "ChoiceCode",
    "Composite",
    "Either",
    "EitherFlag",
    "Holder",
    "Named",
    "TagList",
    "TagListItem",
    "TagListItemTag",
]
