

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .post_platform_result import PostPlatformResult


class Post(UniversalBaseModel):
    id: str
    business_id: typing_extensions.Annotated[str, FieldMetadata(alias="businessId"), pydantic.Field(alias="businessId")]
    content: str
    media_urls: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="mediaUrls"), pydantic.Field(alias="mediaUrls")
    ] = None
    platform_results: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, PostPlatformResult]],
        FieldMetadata(alias="platformResults"),
        pydantic.Field(alias="platformResults"),
    ] = None
    status: str
    scheduled_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="scheduledAt"), pydantic.Field(alias="scheduledAt")
    ] = None
    published_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="publishedAt"), pydantic.Field(alias="publishedAt")
    ] = None
    broadcast_group_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="broadcastGroupId"),
        pydantic.Field(
            alias="broadcastGroupId",
            description="Groups posts fanned out by one cross-platform broadcast turn. Posts sharing a non-empty value were created together; absent for standalone posts and records that predate the field.",
        ),
    ] = None
    """
    Groups posts fanned out by one cross-platform broadcast turn. Posts sharing a non-empty value were created together; absent for standalone posts and records that predate the field.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
