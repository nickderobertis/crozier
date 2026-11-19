



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .bundle import Bundle
    from .firing_notes import FiringNotes
    from .firing_summary import FiringSummary
    from .glazing_step import GlazingStep
    from .glazing_step_kind import GlazingStepKind
    from .kiln_alarm import KilnAlarm
    from .kiln_alarm_view import KilnAlarmView
    from .kiln_plate import KilnPlate
    from .plate_base import PlateBase
    from .plate_extra import PlateExtra
    from .plate_extra_plate_type import PlateExtraPlateType
    from .shelf_summary import ShelfSummary
    from .step import Step
    from .step_config import StepConfig
    from .step_config_reason import StepConfigReason
    from .step_state import StepState
    from .store_ids import StoreIds
    from .summary_base import SummaryBase
    from .timed_summary import TimedSummary
_dynamic_imports: typing.Dict[str, str] = {
    "Bundle": ".bundle",
    "FiringNotes": ".firing_notes",
    "FiringSummary": ".firing_summary",
    "GlazingStep": ".glazing_step",
    "GlazingStepKind": ".glazing_step_kind",
    "KilnAlarm": ".kiln_alarm",
    "KilnAlarmView": ".kiln_alarm_view",
    "KilnPlate": ".kiln_plate",
    "PlateBase": ".plate_base",
    "PlateExtra": ".plate_extra",
    "PlateExtraPlateType": ".plate_extra_plate_type",
    "ShelfSummary": ".shelf_summary",
    "Step": ".step",
    "StepConfig": ".step_config",
    "StepConfigReason": ".step_config_reason",
    "StepState": ".step_state",
    "StoreIds": ".store_ids",
    "SummaryBase": ".summary_base",
    "TimedSummary": ".timed_summary",
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
    "Bundle",
    "FiringNotes",
    "FiringSummary",
    "GlazingStep",
    "GlazingStepKind",
    "KilnAlarm",
    "KilnAlarmView",
    "KilnPlate",
    "PlateBase",
    "PlateExtra",
    "PlateExtraPlateType",
    "ShelfSummary",
    "Step",
    "StepConfig",
    "StepConfigReason",
    "StepState",
    "StoreIds",
    "SummaryBase",
    "TimedSummary",
]
