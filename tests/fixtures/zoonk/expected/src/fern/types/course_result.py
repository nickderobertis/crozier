

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .organization_summary import OrganizationSummary


class CourseResult(UniversalBaseModel):
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Course description
    """

    id: str = pydantic.Field()
    """
    Course ID
    """

    image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imageUrl"),
        pydantic.Field(alias="imageUrl", description="Cover image URL"),
    ] = None
    """
    Cover image URL
    """

    language: str = pydantic.Field()
    """
    Language code
    """

    organization: OrganizationSummary
    slug: str = pydantic.Field()
    """
    URL slug
    """

    title: str = pydantic.Field()
    """
    Course title
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
