



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .create_dpp_request_representation import CreateDppRequestRepresentation
    from .read_dpp_by_id_request_representation import ReadDppByIdRequestRepresentation
    from .read_dpp_by_product_id_request_representation import ReadDppByProductIdRequestRepresentation
    from .read_dpp_version_by_id_and_date_request_representation import ReadDppVersionByIdAndDateRequestRepresentation
    from .update_dpp_by_id_request_representation import UpdateDppByIdRequestRepresentation
_dynamic_imports: typing.Dict[str, str] = {
    "CreateDppRequestRepresentation": ".create_dpp_request_representation",
    "ReadDppByIdRequestRepresentation": ".read_dpp_by_id_request_representation",
    "ReadDppByProductIdRequestRepresentation": ".read_dpp_by_product_id_request_representation",
    "ReadDppVersionByIdAndDateRequestRepresentation": ".read_dpp_version_by_id_and_date_request_representation",
    "UpdateDppByIdRequestRepresentation": ".update_dpp_by_id_request_representation",
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
    "CreateDppRequestRepresentation",
    "ReadDppByIdRequestRepresentation",
    "ReadDppByProductIdRequestRepresentation",
    "ReadDppVersionByIdAndDateRequestRepresentation",
    "UpdateDppByIdRequestRepresentation",
]
