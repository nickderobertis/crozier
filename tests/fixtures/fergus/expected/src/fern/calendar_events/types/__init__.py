



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .delete_calendar_events_calendar_event_id_request_delete_all_grouped import (
        DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped,
    )
    from .delete_calendar_events_calendar_event_id_request_delete_all_recurring import (
        DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring,
    )
    from .get_calendar_events_request_filter_calendar_event_type import GetCalendarEventsRequestFilterCalendarEventType
    from .get_calendar_events_request_filter_calendar_range import GetCalendarEventsRequestFilterCalendarRange
    from .post_calendar_events_calendar_event_id_request_frequency import (
        PostCalendarEventsCalendarEventIdRequestFrequency,
    )
    from .post_calendar_events_calendar_event_id_request_repeat_end_type import (
        PostCalendarEventsCalendarEventIdRequestRepeatEndType,
    )
    from .post_calendar_events_calendar_event_id_request_update_all_grouped import (
        PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped,
    )
    from .post_calendar_events_calendar_event_id_request_update_all_recurring import (
        PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring,
    )
    from .post_calendar_events_request_event_type import PostCalendarEventsRequestEventType
    from .post_calendar_events_request_frequency import PostCalendarEventsRequestFrequency
    from .post_calendar_events_request_repeat_end_type import PostCalendarEventsRequestRepeatEndType
_dynamic_imports: typing.Dict[str, str] = {
    "DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped": ".delete_calendar_events_calendar_event_id_request_delete_all_grouped",
    "DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring": ".delete_calendar_events_calendar_event_id_request_delete_all_recurring",
    "GetCalendarEventsRequestFilterCalendarEventType": ".get_calendar_events_request_filter_calendar_event_type",
    "GetCalendarEventsRequestFilterCalendarRange": ".get_calendar_events_request_filter_calendar_range",
    "PostCalendarEventsCalendarEventIdRequestFrequency": ".post_calendar_events_calendar_event_id_request_frequency",
    "PostCalendarEventsCalendarEventIdRequestRepeatEndType": ".post_calendar_events_calendar_event_id_request_repeat_end_type",
    "PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped": ".post_calendar_events_calendar_event_id_request_update_all_grouped",
    "PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring": ".post_calendar_events_calendar_event_id_request_update_all_recurring",
    "PostCalendarEventsRequestEventType": ".post_calendar_events_request_event_type",
    "PostCalendarEventsRequestFrequency": ".post_calendar_events_request_frequency",
    "PostCalendarEventsRequestRepeatEndType": ".post_calendar_events_request_repeat_end_type",
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
    "DeleteCalendarEventsCalendarEventIdRequestDeleteAllGrouped",
    "DeleteCalendarEventsCalendarEventIdRequestDeleteAllRecurring",
    "GetCalendarEventsRequestFilterCalendarEventType",
    "GetCalendarEventsRequestFilterCalendarRange",
    "PostCalendarEventsCalendarEventIdRequestFrequency",
    "PostCalendarEventsCalendarEventIdRequestRepeatEndType",
    "PostCalendarEventsCalendarEventIdRequestUpdateAllGrouped",
    "PostCalendarEventsCalendarEventIdRequestUpdateAllRecurring",
    "PostCalendarEventsRequestEventType",
    "PostCalendarEventsRequestFrequency",
    "PostCalendarEventsRequestRepeatEndType",
]
