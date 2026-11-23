



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .exposure_unit import ExposureUnit
    from .exposure_unit_one import ExposureUnitOne
    from .exposure_unit_zero import ExposureUnitZero
    from .filter_band import FilterBand
    from .filter_band_one import FilterBandOne
    from .filter_band_zero import FilterBandZero
    from .image_size import ImageSize
    from .lens_reading import LensReading
    from .presence import Presence
    from .sensor_reading import SensorReading
    from .session import Session
    from .session_calibrations_value_item import SessionCalibrationsValueItem
    from .session_calibrations_value_item_offset import SessionCalibrationsValueItemOffset
    from .session_problem import SessionProblem
    from .session_problem_details_item import SessionProblemDetailsItem
    from .session_problem_details_item_description import SessionProblemDetailsItemDescription
    from .session_problem_details_item_description_description import SessionProblemDetailsItemDescriptionDescription
    from .session_problem_details_item_description_issue import SessionProblemDetailsItemDescriptionIssue
    from .session_problem_details_item_one import SessionProblemDetailsItemOne
    from .session_problem_details_item_one_description import SessionProblemDetailsItemOneDescription
    from .session_problem_details_item_one_issue import SessionProblemDetailsItemOneIssue
    from .session_problem_details_item_three import SessionProblemDetailsItemThree
    from .session_problem_details_item_three_issue import SessionProblemDetailsItemThreeIssue
    from .session_reading_batches_item_item import (
        SessionReadingBatchesItemItem,
        SessionReadingBatchesItemItem_Lens,
        SessionReadingBatchesItemItem_Sensor,
    )
    from .session_readings_by_owner_value_value import (
        SessionReadingsByOwnerValueValue,
        SessionReadingsByOwnerValueValue_Lens,
        SessionReadingsByOwnerValueValue_Sensor,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ExposureUnit": ".exposure_unit",
    "ExposureUnitOne": ".exposure_unit_one",
    "ExposureUnitZero": ".exposure_unit_zero",
    "FilterBand": ".filter_band",
    "FilterBandOne": ".filter_band_one",
    "FilterBandZero": ".filter_band_zero",
    "ImageSize": ".image_size",
    "LensReading": ".lens_reading",
    "Presence": ".presence",
    "SensorReading": ".sensor_reading",
    "Session": ".session",
    "SessionCalibrationsValueItem": ".session_calibrations_value_item",
    "SessionCalibrationsValueItemOffset": ".session_calibrations_value_item_offset",
    "SessionProblem": ".session_problem",
    "SessionProblemDetailsItem": ".session_problem_details_item",
    "SessionProblemDetailsItemDescription": ".session_problem_details_item_description",
    "SessionProblemDetailsItemDescriptionDescription": ".session_problem_details_item_description_description",
    "SessionProblemDetailsItemDescriptionIssue": ".session_problem_details_item_description_issue",
    "SessionProblemDetailsItemOne": ".session_problem_details_item_one",
    "SessionProblemDetailsItemOneDescription": ".session_problem_details_item_one_description",
    "SessionProblemDetailsItemOneIssue": ".session_problem_details_item_one_issue",
    "SessionProblemDetailsItemThree": ".session_problem_details_item_three",
    "SessionProblemDetailsItemThreeIssue": ".session_problem_details_item_three_issue",
    "SessionReadingBatchesItemItem": ".session_reading_batches_item_item",
    "SessionReadingBatchesItemItem_Lens": ".session_reading_batches_item_item",
    "SessionReadingBatchesItemItem_Sensor": ".session_reading_batches_item_item",
    "SessionReadingsByOwnerValueValue": ".session_readings_by_owner_value_value",
    "SessionReadingsByOwnerValueValue_Lens": ".session_readings_by_owner_value_value",
    "SessionReadingsByOwnerValueValue_Sensor": ".session_readings_by_owner_value_value",
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
    "ExposureUnit",
    "ExposureUnitOne",
    "ExposureUnitZero",
    "FilterBand",
    "FilterBandOne",
    "FilterBandZero",
    "ImageSize",
    "LensReading",
    "Presence",
    "SensorReading",
    "Session",
    "SessionCalibrationsValueItem",
    "SessionCalibrationsValueItemOffset",
    "SessionProblem",
    "SessionProblemDetailsItem",
    "SessionProblemDetailsItemDescription",
    "SessionProblemDetailsItemDescriptionDescription",
    "SessionProblemDetailsItemDescriptionIssue",
    "SessionProblemDetailsItemOne",
    "SessionProblemDetailsItemOneDescription",
    "SessionProblemDetailsItemOneIssue",
    "SessionProblemDetailsItemThree",
    "SessionProblemDetailsItemThreeIssue",
    "SessionReadingBatchesItemItem",
    "SessionReadingBatchesItemItem_Lens",
    "SessionReadingBatchesItemItem_Sensor",
    "SessionReadingsByOwnerValueValue",
    "SessionReadingsByOwnerValueValue_Lens",
    "SessionReadingsByOwnerValueValue_Sensor",
]
