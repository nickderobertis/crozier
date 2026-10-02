

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ticket_participant import TicketParticipant


class TicketComment(UniversalBaseModel):
    id: typing.Optional[int] = None
    text: typing.Optional[str] = None
    created: typing.Optional[dt.datetime] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[TicketParticipant], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    last_modified: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastModified"), pydantic.Field(alias="lastModified")
    ] = None
    last_modified_by: typing_extensions.Annotated[
        typing.Optional[TicketParticipant],
        FieldMetadata(alias="lastModifiedBy"),
        pydantic.Field(alias="lastModifiedBy"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
