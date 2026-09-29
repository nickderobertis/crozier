

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .course_resource_categories_item import CourseResourceCategoriesItem
from .course_resource_format import CourseResourceFormat
from .course_resource_generation_status import CourseResourceGenerationStatus
from .organization_summary import OrganizationSummary


class CourseResource(UniversalBaseModel):
    categories: typing.List[CourseResourceCategoriesItem]
    course_prompt_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="coursePromptId"), pydantic.Field(alias="coursePromptId")
    ] = None
    description: typing.Optional[str] = None
    format: CourseResourceFormat
    generation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="generationId"), pydantic.Field(alias="generationId")
    ] = None
    generation_status: typing_extensions.Annotated[
        CourseResourceGenerationStatus,
        FieldMetadata(alias="generationStatus"),
        pydantic.Field(alias="generationStatus"),
    ]
    id: str
    image_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="imageUrl"), pydantic.Field(alias="imageUrl")
    ] = None
    language: str
    organization: OrganizationSummary
    slug: str
    target_language: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetLanguage"), pydantic.Field(alias="targetLanguage")
    ] = None
    title: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
