

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class MediaDto(UniversalBaseModel):
    comment: str
    epub_divina_compatible: typing_extensions.Annotated[
        bool, FieldMetadata(alias="epubDivinaCompatible"), pydantic.Field(alias="epubDivinaCompatible")
    ]
    epub_is_kepub: typing_extensions.Annotated[
        bool, FieldMetadata(alias="epubIsKepub"), pydantic.Field(alias="epubIsKepub")
    ]
    media_profile: typing_extensions.Annotated[
        str, FieldMetadata(alias="mediaProfile"), pydantic.Field(alias="mediaProfile")
    ]
    media_type: typing_extensions.Annotated[str, FieldMetadata(alias="mediaType"), pydantic.Field(alias="mediaType")]
    pages_count: typing_extensions.Annotated[int, FieldMetadata(alias="pagesCount"), pydantic.Field(alias="pagesCount")]
    status: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
