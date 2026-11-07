

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .records_get_schema_response_attachments_signed_copy import RecordsGetSchemaResponseAttachmentsSignedCopy


class RecordsGetSchemaResponseAttachments(UniversalBaseModel):
    signed_copy: typing_extensions.Annotated[
        typing.Optional[RecordsGetSchemaResponseAttachmentsSignedCopy],
        FieldMetadata(alias="signedCopy"),
        pydantic.Field(alias="signedCopy"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
