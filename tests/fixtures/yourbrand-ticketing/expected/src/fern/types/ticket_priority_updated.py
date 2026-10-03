

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ticket_priority import TicketPriority


class TicketPriorityUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_priority: typing_extensions.Annotated[
        typing.Optional[TicketPriority], FieldMetadata(alias="newPriority"), pydantic.Field(alias="newPriority")
    ] = None
    old_priority: typing_extensions.Annotated[
        typing.Optional[TicketPriority], FieldMetadata(alias="oldPriority"), pydantic.Field(alias="oldPriority")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
