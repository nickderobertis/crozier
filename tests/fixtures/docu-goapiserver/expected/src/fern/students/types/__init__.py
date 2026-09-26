



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_students_id_v3request_fields_item import GetStudentsIdV3RequestFieldsItem
    from .get_students_id_v3response import GetStudentsIdV3Response
    from .get_students_v3request_fields_item import GetStudentsV3RequestFieldsItem
    from .get_students_v3response import GetStudentsV3Response
_dynamic_imports: typing.Dict[str, str] = {
    "GetStudentsIdV3RequestFieldsItem": ".get_students_id_v3request_fields_item",
    "GetStudentsIdV3Response": ".get_students_id_v3response",
    "GetStudentsV3RequestFieldsItem": ".get_students_v3request_fields_item",
    "GetStudentsV3Response": ".get_students_v3response",
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
    "GetStudentsIdV3RequestFieldsItem",
    "GetStudentsIdV3Response",
    "GetStudentsV3RequestFieldsItem",
    "GetStudentsV3Response",
]
