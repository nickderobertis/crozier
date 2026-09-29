

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .language_course_target_language import LanguageCourseTargetLanguage


class LanguageCourse(UniversalBaseModel):
    id: str
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    language: str
    slug: str
    target_language: typing_extensions.Annotated[
        LanguageCourseTargetLanguage, FieldMetadata(alias="targetLanguage"), pydantic.Field(alias="targetLanguage")
    ]
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
