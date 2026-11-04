

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .records_get_schema_response_attachments import RecordsGetSchemaResponseAttachments
from .records_get_schema_response_links import RecordsGetSchemaResponseLinks
from .records_get_schema_response_properties import RecordsGetSchemaResponseProperties
from .records_get_schema_response_record_types import RecordsGetSchemaResponseRecordTypes


class RecordsGetSchemaResponse(UniversalBaseModel):
    record_types: typing_extensions.Annotated[
        typing.Optional[RecordsGetSchemaResponseRecordTypes],
        FieldMetadata(alias="recordTypes"),
        pydantic.Field(alias="recordTypes"),
    ] = None
    properties: typing.Optional[RecordsGetSchemaResponseProperties] = None
    attachments: typing.Optional[RecordsGetSchemaResponseAttachments] = None
    links: typing.Optional[RecordsGetSchemaResponseLinks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
