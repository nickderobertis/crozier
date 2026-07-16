



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        Date,
        Email,
        Error,
        EventDates,
        EventDescription,
        EventId,
        EventLocation,
        EventName,
        EventPrice,
        MuseumDailyHours,
        MuseumHours,
        MuseumTicketsConfirmation,
        SpecialEvent,
        SpecialEventCollection,
        Ticket,
        TicketCodeImage,
        TicketConfirmation,
        TicketId,
        TicketMessage,
        TicketType,
    )
    from .errors import BadRequestError, NotFoundError, UnauthorizedError
    from . import events, operations, tickets
    from .client import AsyncFernApi, FernApi
    from .environment import FernApiEnvironment
    from .version import __version__
_dynamic_imports: typing.Dict[str, str] = {
    "AsyncFernApi": ".client",
    "BadRequestError": ".errors",
    "Date": ".types",
    "Email": ".types",
    "Error": ".types",
    "EventDates": ".types",
    "EventDescription": ".types",
    "EventId": ".types",
    "EventLocation": ".types",
    "EventName": ".types",
    "EventPrice": ".types",
    "FernApi": ".client",
    "FernApiEnvironment": ".environment",
    "MuseumDailyHours": ".types",
    "MuseumHours": ".types",
    "MuseumTicketsConfirmation": ".types",
    "NotFoundError": ".errors",
    "SpecialEvent": ".types",
    "SpecialEventCollection": ".types",
    "Ticket": ".types",
    "TicketCodeImage": ".types",
    "TicketConfirmation": ".types",
    "TicketId": ".types",
    "TicketMessage": ".types",
    "TicketType": ".types",
    "UnauthorizedError": ".errors",
    "__version__": ".version",
    "events": ".events",
    "operations": ".operations",
    "tickets": ".tickets",
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
    "AsyncFernApi",
    "BadRequestError",
    "Date",
    "Email",
    "Error",
    "EventDates",
    "EventDescription",
    "EventId",
    "EventLocation",
    "EventName",
    "EventPrice",
    "FernApi",
    "FernApiEnvironment",
    "MuseumDailyHours",
    "MuseumHours",
    "MuseumTicketsConfirmation",
    "NotFoundError",
    "SpecialEvent",
    "SpecialEventCollection",
    "Ticket",
    "TicketCodeImage",
    "TicketConfirmation",
    "TicketId",
    "TicketMessage",
    "TicketType",
    "UnauthorizedError",
    "__version__",
    "events",
    "operations",
    "tickets",
]
