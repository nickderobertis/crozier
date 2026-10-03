

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TicketEstimatedTimeUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newTime"), pydantic.Field(alias="newTime")
    ] = None
    old_time: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldTime"), pydantic.Field(alias="oldTime")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
