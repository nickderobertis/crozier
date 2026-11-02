



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .set_chart_layers_request_layers_item import SetChartLayersRequestLayersItem
    from .set_chart_layers_request_layers_item_match import SetChartLayersRequestLayersItemMatch
    from .set_chart_layers_response import SetChartLayersResponse
    from .upload_chart_response import UploadChartResponse
_dynamic_imports: typing.Dict[str, str] = {
    "SetChartLayersRequestLayersItem": ".set_chart_layers_request_layers_item",
    "SetChartLayersRequestLayersItemMatch": ".set_chart_layers_request_layers_item_match",
    "SetChartLayersResponse": ".set_chart_layers_response",
    "UploadChartResponse": ".upload_chart_response",
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
    "SetChartLayersRequestLayersItem",
    "SetChartLayersRequestLayersItemMatch",
    "SetChartLayersResponse",
    "UploadChartResponse",
]
