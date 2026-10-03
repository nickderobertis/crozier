

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TicketSubjectUpdated(UniversalBaseModel):
    ticket_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="ticketId"), pydantic.Field(alias="ticketId")
    ] = None
    new_subject: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="newSubject"), pydantic.Field(alias="newSubject")
    ] = None
    old_subject: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="oldSubject"), pydantic.Field(alias="oldSubject")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
