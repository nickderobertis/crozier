

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PageDto(UniversalBaseModel):
    file_name: typing_extensions.Annotated[str, FieldMetadata(alias="fileName"), pydantic.Field(alias="fileName")]
    height: typing.Optional[int] = None
    media_type: typing_extensions.Annotated[str, FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")]
    number: int
    size: str
    size_bytes: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="sizeBytes"), pydantic.Field(alias="sizeBytes")
    ] = None
    width: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
