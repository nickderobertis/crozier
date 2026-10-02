

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TicketDescriptionUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newDescription"), pydantic.Field(alias="newDescription")
    ] = None
    old_description: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldDescription"), pydantic.Field(alias="oldDescription")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
