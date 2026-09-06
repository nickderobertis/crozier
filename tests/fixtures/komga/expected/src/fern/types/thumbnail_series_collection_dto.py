

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ThumbnailSeriesCollectionDto(UniversalBaseModel):
    collection_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="collectionId"), pydantic.Field(alias="collectionId")
    ]
    file_size: typing_extensions.Annotated[int, FieldMetadata(alias="fileSize"), pydantic.Field(alias="fileSize")]
    height: int
    id: str
    media_type: typing_extensions.Annotated[str, FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")]
    selected: bool
    type: str
    width: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
