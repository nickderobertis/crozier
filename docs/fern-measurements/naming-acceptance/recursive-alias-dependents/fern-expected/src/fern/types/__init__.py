



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .fit_summary import FitSummary
    from .inference_report import InferenceReport
    from .json_array_output import JsonArrayOutput
    from .json_object_output import JsonObjectOutput
    from .json_scalar import JsonScalar
    from .json_value_output import JsonValueOutput
_dynamic_imports: typing.Dict[str, str] = {
    "FitSummary": ".fit_summary",
    "InferenceReport": ".inference_report",
    "JsonArrayOutput": ".json_array_output",
    "JsonObjectOutput": ".json_object_output",
    "JsonScalar": ".json_scalar",
    "JsonValueOutput": ".json_value_output",
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


__all__ = ["FitSummary", "InferenceReport", "JsonArrayOutput", "JsonObjectOutput", "JsonScalar", "JsonValueOutput"]
