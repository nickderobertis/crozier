

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ticket_participant import TicketParticipant


class TicketAssigneeUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    assigned_participant: typing_extensions.Annotated[
        typing.Optional[TicketParticipant],
        FieldMetadata(alias="assignedParticipant"),
        pydantic.Field(alias="assignedParticipant"),
    ] = None
    old_assigned_participant: typing_extensions.Annotated[
        typing.Optional[TicketParticipant],
        FieldMetadata(alias="oldAssignedParticipant"),
        pydantic.Field(alias="oldAssignedParticipant"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
