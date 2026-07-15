



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .session_settings import SessionSettings
    from .session_settings_allow_actions_item import SessionSettingsAllowActionsItem
    from .session_theme import SessionTheme
_dynamic_imports: typing.Dict[str, str] = {
    "SessionSettings": ".session_settings",
    "SessionSettingsAllowActionsItem": ".session_settings_allow_actions_item",
    "SessionTheme": ".session_theme",
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


__all__ = ["SessionSettings", "SessionSettingsAllowActionsItem", "SessionTheme"]
