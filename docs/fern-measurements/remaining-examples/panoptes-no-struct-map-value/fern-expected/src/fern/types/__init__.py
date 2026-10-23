



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .block import Block
    from .block_value import BlockValue
    from .data_set import DataSet
    from .data_set_data_configuration import DataSetDataConfiguration
    from .facet_result import FacetResult
    from .range_facet import RangeFacet
    from .text_facet import TextFacet
_dynamic_imports: typing.Dict[str, str] = {
    "Block": ".block",
    "BlockValue": ".block_value",
    "DataSet": ".data_set",
    "DataSetDataConfiguration": ".data_set_data_configuration",
    "FacetResult": ".facet_result",
    "RangeFacet": ".range_facet",
    "TextFacet": ".text_facet",
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


__all__ = ["Block", "BlockValue", "DataSet", "DataSetDataConfiguration", "FacetResult", "RangeFacet", "TextFacet"]
