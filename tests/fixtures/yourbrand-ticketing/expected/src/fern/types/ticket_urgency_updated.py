

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ticket_urgency import TicketUrgency


class TicketUrgencyUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_urgency: typing_extensions.Annotated[
        typing.Optional[TicketUrgency], FieldMetadata(alias="newUrgency"), pydantic.Field(alias="newUrgency")
    ] = None
    old_urgency: typing_extensions.Annotated[
        typing.Optional[TicketUrgency], FieldMetadata(alias="oldUrgency"), pydantic.Field(alias="oldUrgency")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
