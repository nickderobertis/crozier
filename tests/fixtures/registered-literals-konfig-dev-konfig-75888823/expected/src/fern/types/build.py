

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .app_id import AppId
from .build_id import BuildId
from .build_regional_container_tags_item import BuildRegionalContainerTagsItem
from .build_status import BuildStatus
from .build_tag import BuildTag


class Build(UniversalBaseModel):
    """
    A build represents a game server artifact and its associated metadata.
    """

    build_tag: typing_extensions.Annotated[
        typing.Optional[BuildTag], FieldMetadata(alias="buildTag"), pydantic.Field(alias="buildTag")
    ] = None
    regional_container_tags: typing_extensions.Annotated[
        typing.List[BuildRegionalContainerTagsItem],
        FieldMetadata(alias="regionalContainerTags"),
        pydantic.Field(alias="regionalContainerTags"),
    ]
    image_size: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="imageSize"),
        pydantic.Field(alias="imageSize", description="The size (in bytes) of the Docker image built by Hathora."),
    ]
    """
    The size (in bytes) of the Docker image built by Hathora.
    """

    status: BuildStatus = pydantic.Field()
    """
    Current status of your build.
    
    `created`: a build was created but not yet run
    
    `running`: the build process is actively executing
    
    `succeeded`: the game server artifact was successfully built and stored in the Hathora registries
    
    `failed`: the build process was unsuccessful, most likely due to an error with the `Dockerfile`
    """

    deleted_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="deletedAt"),
        pydantic.Field(alias="deletedAt", description="When the build was deleted."),
    ] = None
    """
    When the build was deleted.
    """

    finished_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="finishedAt"),
        pydantic.Field(
            alias="finishedAt",
            description="When [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) finished executing.",
        ),
    ] = None
    """
    When [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) finished executing.
    """

    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startedAt"),
        pydantic.Field(
            alias="startedAt",
            description="When [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) is called.",
        ),
    ] = None
    """
    When [`RunBuild()`](https://hathora.dev/api#tag/BuildV1/operation/RunBuild) is called.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(
            alias="createdAt",
            description="When [`CreateBuild()`](https://hathora.dev/api#tag/BuildV1/operation/CreateBuild) is called.",
        ),
    ]
    """
    When [`CreateBuild()`](https://hathora.dev/api#tag/BuildV1/operation/CreateBuild) is called.
    """

    created_by: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdBy"),
        pydantic.Field(alias="createdBy", description="UserId or email address for the user that created the build."),
    ]
    """
    UserId or email address for the user that created the build.
    """

    build_id: typing_extensions.Annotated[BuildId, FieldMetadata(alias="buildId"), pydantic.Field(alias="buildId")]
    app_id: typing_extensions.Annotated[AppId, FieldMetadata(alias="appId"), pydantic.Field(alias="appId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
