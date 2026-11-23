



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .update_data_lite_input_input_options import (
        UpdateDataLiteInputInputOptions,
        UpdateDataLiteInputInputOptions_Csv,
        UpdateDataLiteInputInputOptions_Parquet,
    )
    from .update_data_lite_input_input_options_csv import UpdateDataLiteInputInputOptionsCsv
    from .update_data_lite_input_input_options_parquet import UpdateDataLiteInputInputOptionsParquet
_dynamic_imports: typing.Dict[str, str] = {
    "UpdateDataLiteInputInputOptions": ".update_data_lite_input_input_options",
    "UpdateDataLiteInputInputOptionsCsv": ".update_data_lite_input_input_options_csv",
    "UpdateDataLiteInputInputOptionsParquet": ".update_data_lite_input_input_options_parquet",
    "UpdateDataLiteInputInputOptions_Csv": ".update_data_lite_input_input_options",
    "UpdateDataLiteInputInputOptions_Parquet": ".update_data_lite_input_input_options",
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
    "UpdateDataLiteInputInputOptions",
    "UpdateDataLiteInputInputOptionsCsv",
    "UpdateDataLiteInputInputOptionsParquet",
    "UpdateDataLiteInputInputOptions_Csv",
    "UpdateDataLiteInputInputOptions_Parquet",
]
