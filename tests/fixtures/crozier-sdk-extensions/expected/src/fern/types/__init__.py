



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .page_info import PageInfo
    from .price_unit import PriceUnit
    from .watch_request import WatchRequest
    from .widget import Widget
    from .widget_event import WidgetEvent
    from .widget_page import WidgetPage
_dynamic_imports: typing.Dict[str, str] = {
    "PageInfo": ".page_info",
    "PriceUnit": ".price_unit",
    "WatchRequest": ".watch_request",
    "Widget": ".widget",
    "WidgetEvent": ".widget_event",
    "WidgetPage": ".widget_page",
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


__all__ = ["PageInfo", "PriceUnit", "WatchRequest", "Widget", "WidgetEvent", "WidgetPage"]
