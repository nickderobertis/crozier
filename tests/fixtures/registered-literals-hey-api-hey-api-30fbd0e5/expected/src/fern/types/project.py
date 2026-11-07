

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .project_author import ProjectAuthor
from .project_links import ProjectLinks
from .project_privacy import ProjectPrivacy


class Project(UniversalBaseModel):
    """
    A Project
    """

    name: str
    id: str = pydantic.Field()
    """
    The id of the project
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]
    privacy: ProjectPrivacy = pydantic.Field()
    """
    This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.
    """

    author: ProjectAuthor
    description: typing.Optional[str] = None
    image_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="imageUrl"),
        pydantic.Field(alias="imageUrl", description="The URL of this project's image"),
    ] = None
    """
    The URL of this project's image
    """

    links: ProjectLinks

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
