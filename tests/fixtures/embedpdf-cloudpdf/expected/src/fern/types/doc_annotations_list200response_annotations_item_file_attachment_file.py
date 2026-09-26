

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DocAnnotationsList200ResponseAnnotationsItemFileAttachmentFile(UniversalBaseModel):
    name: str
    mime_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="mimeType"), pydantic.Field(alias="mimeType")
    ] = None
    description: typing.Optional[str] = None
    size: typing.Optional[int] = None
    checksum: typing.Optional[str] = None
    creation_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="creationDate"), pydantic.Field(alias="creationDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
