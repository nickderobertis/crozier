



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .date import Date
    from .email import Email
    from .error import Error
    from .event_dates import EventDates
    from .event_description import EventDescription
    from .event_id import EventId
    from .event_location import EventLocation
    from .event_name import EventName
    from .event_price import EventPrice
    from .museum_daily_hours import MuseumDailyHours
    from .museum_hours import MuseumHours
    from .museum_tickets_confirmation import MuseumTicketsConfirmation
    from .special_event import SpecialEvent
    from .special_event_collection import SpecialEventCollection
    from .ticket import Ticket
    from .ticket_code_image import TicketCodeImage
    from .ticket_confirmation import TicketConfirmation
    from .ticket_id import TicketId
    from .ticket_message import TicketMessage
    from .ticket_type import TicketType
_dynamic_imports: typing.Dict[str, str] = {
    "Date": ".date",
    "Email": ".email",
    "Error": ".error",
    "EventDates": ".event_dates",
    "EventDescription": ".event_description",
    "EventId": ".event_id",
    "EventLocation": ".event_location",
    "EventName": ".event_name",
    "EventPrice": ".event_price",
    "MuseumDailyHours": ".museum_daily_hours",
    "MuseumHours": ".museum_hours",
    "MuseumTicketsConfirmation": ".museum_tickets_confirmation",
    "SpecialEvent": ".special_event",
    "SpecialEventCollection": ".special_event_collection",
    "Ticket": ".ticket",
    "TicketCodeImage": ".ticket_code_image",
    "TicketConfirmation": ".ticket_confirmation",
    "TicketId": ".ticket_id",
    "TicketMessage": ".ticket_message",
    "TicketType": ".ticket_type",
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
    "Date",
    "Email",
    "Error",
    "EventDates",
    "EventDescription",
    "EventId",
    "EventLocation",
    "EventName",
    "EventPrice",
    "MuseumDailyHours",
    "MuseumHours",
    "MuseumTicketsConfirmation",
    "SpecialEvent",
    "SpecialEventCollection",
    "Ticket",
    "TicketCodeImage",
    "TicketConfirmation",
    "TicketId",
    "TicketMessage",
    "TicketType",
]
