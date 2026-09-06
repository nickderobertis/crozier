

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class PageHashMatchDto(UniversalBaseModel):
    book_id: typing_extensions.Annotated[str, FieldMetadata(alias="bookId"), pydantic.Field(alias="bookId")]
    file_name: typing_extensions.Annotated[str, FieldMetadata(alias="fileName"), pydantic.Field(alias="fileName")]
    file_size: typing_extensions.Annotated[int, FieldMetadata(alias="fileSize"), pydantic.Field(alias="fileSize")]
    media_type: typing_extensions.Annotated[str, FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")]
    page_number: typing_extensions.Annotated[int, FieldMetadata(alias="pageNumber"), pydantic.Field(alias="pageNumber")]
    url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
