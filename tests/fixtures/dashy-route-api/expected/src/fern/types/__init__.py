



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .app_config import AppConfig
    from .app_config_icon_size import AppConfigIconSize
    from .app_config_layout import AppConfigLayout
    from .app_config_starting_view import AppConfigStartingView
    from .config import Config
    from .error import Error
    from .file_list import FileList
    from .item import Item
    from .item_fields import ItemFields
    from .item_fields_target import ItemFieldsTarget
    from .item_result import ItemResult
    from .key_value import KeyValue
    from .page import Page
    from .page_info import PageInfo
    from .section import Section
    from .section_fields import SectionFields
    from .section_result import SectionResult
    from .write_result import WriteResult
_dynamic_imports: typing.Dict[str, str] = {
    "AppConfig": ".app_config",
    "AppConfigIconSize": ".app_config_icon_size",
    "AppConfigLayout": ".app_config_layout",
    "AppConfigStartingView": ".app_config_starting_view",
    "Config": ".config",
    "Error": ".error",
    "FileList": ".file_list",
    "Item": ".item",
    "ItemFields": ".item_fields",
    "ItemFieldsTarget": ".item_fields_target",
    "ItemResult": ".item_result",
    "KeyValue": ".key_value",
    "Page": ".page",
    "PageInfo": ".page_info",
    "Section": ".section",
    "SectionFields": ".section_fields",
    "SectionResult": ".section_result",
    "WriteResult": ".write_result",
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
    "AppConfig",
    "AppConfigIconSize",
    "AppConfigLayout",
    "AppConfigStartingView",
    "Config",
    "Error",
    "FileList",
    "Item",
    "ItemFields",
    "ItemFieldsTarget",
    "ItemResult",
    "KeyValue",
    "Page",
    "PageInfo",
    "Section",
    "SectionFields",
    "SectionResult",
    "WriteResult",
]
