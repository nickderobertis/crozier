

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ticket_status import TicketStatus


class TicketStatusUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_status: typing_extensions.Annotated[
        typing.Optional[TicketStatus], FieldMetadata(alias="newStatus"), pydantic.Field(alias="newStatus")
    ] = None
    old_status: typing_extensions.Annotated[
        typing.Optional[TicketStatus], FieldMetadata(alias="oldStatus"), pydantic.Field(alias="oldStatus")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
