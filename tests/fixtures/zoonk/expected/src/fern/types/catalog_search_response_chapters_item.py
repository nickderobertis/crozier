

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CatalogSearchResponseChaptersItem(UniversalBaseModel):
    course_id: typing_extensions.Annotated[str, FieldMetadata(alias="courseId"), pydantic.Field(alias="courseId")]
    course_slug: typing_extensions.Annotated[str, FieldMetadata(alias="courseSlug"), pydantic.Field(alias="courseSlug")]
    course_title: typing_extensions.Annotated[
        str, FieldMetadata(alias="courseTitle"), pydantic.Field(alias="courseTitle")
    ]
    description: str
    id: str
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    language: str
    organization_slug: typing_extensions.Annotated[
        str, FieldMetadata(alias="organizationSlug"), pydantic.Field(alias="organizationSlug")
    ]
    slug: str
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
