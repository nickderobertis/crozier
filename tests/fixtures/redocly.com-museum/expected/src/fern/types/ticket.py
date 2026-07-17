

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .date import Date
from .event_id import EventId
from .ticket_id import TicketId
from .ticket_type import TicketType


class Ticket(UniversalBaseModel):
    """
    Ticket for museum entry, can be general admission or special event.
    """

    ticket_id: typing_extensions.Annotated[
        typing.Optional[TicketId], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    ticket_date: typing_extensions.Annotated[
        Date,
        FieldMetadata(alias="ticketDate"),
        pydantic.Field(alias="ticketDate", description="Date when this ticket can be used for museum entry."),
    ]
    """
    Date when this ticket can be used for museum entry.
    """

    ticket_type: typing_extensions.Annotated[
        TicketType, FieldMetadata(alias="ticketType"), pydantic.Field(alias="ticketType")
    ]
    event_id: typing_extensions.Annotated[
        typing.Optional[EventId],
        FieldMetadata(alias="eventId"),
        pydantic.Field(
            alias="eventId",
            description="Unique identifier for a special event. Required if purchasing tickets for the museum's special events.",
        ),
    ] = None
    """
    Unique identifier for a special event. Required if purchasing tickets for the museum's special events.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
