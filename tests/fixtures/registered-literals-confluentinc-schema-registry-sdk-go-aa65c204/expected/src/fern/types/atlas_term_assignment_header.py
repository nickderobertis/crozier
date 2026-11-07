

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .atlas_term_assignment_header_status import AtlasTermAssignmentHeaderStatus


class AtlasTermAssignmentHeader(UniversalBaseModel):
    term_guid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="termGuid"), pydantic.Field(alias="termGuid")
    ] = None
    relation_guid: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="relationGuid"), pydantic.Field(alias="relationGuid")
    ] = None
    description: typing.Optional[str] = None
    display_text: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayText"), pydantic.Field(alias="displayText")
    ] = None
    expression: typing.Optional[str] = None
    created_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="createdBy"), pydantic.Field(alias="createdBy")
    ] = None
    steward: typing.Optional[str] = None
    source: typing.Optional[str] = None
    confidence: typing.Optional[int] = None
    status: typing.Optional[AtlasTermAssignmentHeaderStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
