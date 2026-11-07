



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .schedule_create_new_schedule_request_attribution_actor import ScheduleCreateNewScheduleRequestAttributionActor
    from .schedule_create_new_schedule_request_parameters_value import ScheduleCreateNewScheduleRequestParametersValue
    from .schedule_create_new_schedule_request_timetable import ScheduleCreateNewScheduleRequestTimetable
    from .schedule_create_new_schedule_request_timetable_one import ScheduleCreateNewScheduleRequestTimetableOne
    from .schedule_create_new_schedule_request_timetable_one_days_of_week_item import (
        ScheduleCreateNewScheduleRequestTimetableOneDaysOfWeekItem,
    )
    from .schedule_create_new_schedule_request_timetable_one_months_item import (
        ScheduleCreateNewScheduleRequestTimetableOneMonthsItem,
    )
    from .schedule_create_new_schedule_request_timetable_zero import ScheduleCreateNewScheduleRequestTimetableZero
    from .schedule_create_new_schedule_request_timetable_zero_days_of_week_item import (
        ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem,
    )
    from .schedule_create_new_schedule_request_timetable_zero_months_item import (
        ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem,
    )
    from .schedule_update_schedule_request_attribution_actor import ScheduleUpdateScheduleRequestAttributionActor
    from .schedule_update_schedule_request_parameters_value import ScheduleUpdateScheduleRequestParametersValue
    from .schedule_update_schedule_request_timetable import ScheduleUpdateScheduleRequestTimetable
    from .schedule_update_schedule_request_timetable_days_of_week_item import (
        ScheduleUpdateScheduleRequestTimetableDaysOfWeekItem,
    )
    from .schedule_update_schedule_request_timetable_months_item import ScheduleUpdateScheduleRequestTimetableMonthsItem
_dynamic_imports: typing.Dict[str, str] = {
    "ScheduleCreateNewScheduleRequestAttributionActor": ".schedule_create_new_schedule_request_attribution_actor",
    "ScheduleCreateNewScheduleRequestParametersValue": ".schedule_create_new_schedule_request_parameters_value",
    "ScheduleCreateNewScheduleRequestTimetable": ".schedule_create_new_schedule_request_timetable",
    "ScheduleCreateNewScheduleRequestTimetableOne": ".schedule_create_new_schedule_request_timetable_one",
    "ScheduleCreateNewScheduleRequestTimetableOneDaysOfWeekItem": ".schedule_create_new_schedule_request_timetable_one_days_of_week_item",
    "ScheduleCreateNewScheduleRequestTimetableOneMonthsItem": ".schedule_create_new_schedule_request_timetable_one_months_item",
    "ScheduleCreateNewScheduleRequestTimetableZero": ".schedule_create_new_schedule_request_timetable_zero",
    "ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem": ".schedule_create_new_schedule_request_timetable_zero_days_of_week_item",
    "ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem": ".schedule_create_new_schedule_request_timetable_zero_months_item",
    "ScheduleUpdateScheduleRequestAttributionActor": ".schedule_update_schedule_request_attribution_actor",
    "ScheduleUpdateScheduleRequestParametersValue": ".schedule_update_schedule_request_parameters_value",
    "ScheduleUpdateScheduleRequestTimetable": ".schedule_update_schedule_request_timetable",
    "ScheduleUpdateScheduleRequestTimetableDaysOfWeekItem": ".schedule_update_schedule_request_timetable_days_of_week_item",
    "ScheduleUpdateScheduleRequestTimetableMonthsItem": ".schedule_update_schedule_request_timetable_months_item",
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
    "ScheduleCreateNewScheduleRequestAttributionActor",
    "ScheduleCreateNewScheduleRequestParametersValue",
    "ScheduleCreateNewScheduleRequestTimetable",
    "ScheduleCreateNewScheduleRequestTimetableOne",
    "ScheduleCreateNewScheduleRequestTimetableOneDaysOfWeekItem",
    "ScheduleCreateNewScheduleRequestTimetableOneMonthsItem",
    "ScheduleCreateNewScheduleRequestTimetableZero",
    "ScheduleCreateNewScheduleRequestTimetableZeroDaysOfWeekItem",
    "ScheduleCreateNewScheduleRequestTimetableZeroMonthsItem",
    "ScheduleUpdateScheduleRequestAttributionActor",
    "ScheduleUpdateScheduleRequestParametersValue",
    "ScheduleUpdateScheduleRequestTimetable",
    "ScheduleUpdateScheduleRequestTimetableDaysOfWeekItem",
    "ScheduleUpdateScheduleRequestTimetableMonthsItem",
]
