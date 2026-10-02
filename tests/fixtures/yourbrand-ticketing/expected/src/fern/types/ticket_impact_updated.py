

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ticket_impact import TicketImpact


class TicketImpactUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_impact: typing_extensions.Annotated[
        typing.Optional[TicketImpact], FieldMetadata(alias="newImpact"), pydantic.Field(alias="newImpact")
    ] = None
    old_impact: typing_extensions.Annotated[
        typing.Optional[TicketImpact], FieldMetadata(alias="oldImpact"), pydantic.Field(alias="oldImpact")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
