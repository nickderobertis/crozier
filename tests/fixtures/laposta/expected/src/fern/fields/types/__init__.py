



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .veld_toevoegen_request_datatype import VeldToevoegenRequestDatatype
    from .veld_toevoegen_request_datatype_display import VeldToevoegenRequestDatatypeDisplay
    from .veld_wijzigen_request_datatype import VeldWijzigenRequestDatatype
    from .veld_wijzigen_request_datatype_display import VeldWijzigenRequestDatatypeDisplay
_dynamic_imports: typing.Dict[str, str] = {
    "VeldToevoegenRequestDatatype": ".veld_toevoegen_request_datatype",
    "VeldToevoegenRequestDatatypeDisplay": ".veld_toevoegen_request_datatype_display",
    "VeldWijzigenRequestDatatype": ".veld_wijzigen_request_datatype",
    "VeldWijzigenRequestDatatypeDisplay": ".veld_wijzigen_request_datatype_display",
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
    "VeldToevoegenRequestDatatype",
    "VeldToevoegenRequestDatatypeDisplay",
    "VeldWijzigenRequestDatatype",
    "VeldWijzigenRequestDatatypeDisplay",
]
