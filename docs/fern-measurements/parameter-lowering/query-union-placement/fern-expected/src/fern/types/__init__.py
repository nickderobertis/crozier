



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .get_row_request_picker import GetRowRequestPicker
    from .get_row_request_picker_one import GetRowRequestPickerOne
    from .get_row_request_picker_zero import GetRowRequestPickerZero
    from .list_weighed_harvests_request_grade import ListWeighedHarvestsRequestGrade
    from .list_weighed_harvests_request_unit import ListWeighedHarvestsRequestUnit
    from .list_weighed_harvests_request_unit_one import ListWeighedHarvestsRequestUnitOne
    from .list_weighed_harvests_request_unit_zero import ListWeighedHarvestsRequestUnitZero
_dynamic_imports: typing.Dict[str, str] = {
    "GetRowRequestPicker": ".get_row_request_picker",
    "GetRowRequestPickerOne": ".get_row_request_picker_one",
    "GetRowRequestPickerZero": ".get_row_request_picker_zero",
    "ListWeighedHarvestsRequestGrade": ".list_weighed_harvests_request_grade",
    "ListWeighedHarvestsRequestUnit": ".list_weighed_harvests_request_unit",
    "ListWeighedHarvestsRequestUnitOne": ".list_weighed_harvests_request_unit_one",
    "ListWeighedHarvestsRequestUnitZero": ".list_weighed_harvests_request_unit_zero",
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
    "GetRowRequestPicker",
    "GetRowRequestPickerOne",
    "GetRowRequestPickerZero",
    "ListWeighedHarvestsRequestGrade",
    "ListWeighedHarvestsRequestUnit",
    "ListWeighedHarvestsRequestUnitOne",
    "ListWeighedHarvestsRequestUnitZero",
]
