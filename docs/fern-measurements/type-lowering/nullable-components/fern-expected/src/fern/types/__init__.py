



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .channels import Channels
    from .feedback_query import FeedbackQuery
    from .feedback_settings import FeedbackSettings
    from .response_modalities import ResponseModalities
    from .response_modalities_item import ResponseModalitiesItem
_dynamic_imports: typing.Dict[str, str] = {
    "Channels": ".channels",
    "FeedbackQuery": ".feedback_query",
    "FeedbackSettings": ".feedback_settings",
    "ResponseModalities": ".response_modalities",
    "ResponseModalitiesItem": ".response_modalities_item",
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


__all__ = ["Channels", "FeedbackQuery", "FeedbackSettings", "ResponseModalities", "ResponseModalitiesItem"]
