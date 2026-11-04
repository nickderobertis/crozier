

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .excerpt import Excerpt
from .post_spec_visible import PostSpecVisible


class PostSpec(UniversalBaseModel):
    """
    Desired post content, publication, taxonomy, and rendering configuration.
    """

    allow_comment: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="allowComment"),
        pydantic.Field(alias="allowComment", description="Whether new comments are allowed for this post."),
    ]
    """
    Whether new comments are allowed for this post.
    """

    base_snapshot: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="baseSnapshot"),
        pydantic.Field(
            alias="baseSnapshot",
            description="Base Snapshot metadata.name used to reconstruct raw and rendered content from patches.",
        ),
    ] = None
    """
    Base Snapshot metadata.name used to reconstruct raw and rendered content from patches.
    """

    categories: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Category metadata.name values associated with the post.
    """

    cover: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cover image URL or attachment URI of the post.
    """

    deleted: bool = pydantic.Field()
    """
    Whether the post is logically deleted and should be treated as recycled.
    """

    excerpt: Excerpt
    head_snapshot: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="headSnapshot"),
        pydantic.Field(
            alias="headSnapshot", description="Snapshot metadata.name containing the latest editable draft content."
        ),
    ] = None
    """
    Snapshot metadata.name containing the latest editable draft content.
    """

    html_metas: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, str]]],
        FieldMetadata(alias="htmlMetas"),
        pydantic.Field(
            alias="htmlMetas", description="HTML meta tag attribute maps injected into the rendered post page head."
        ),
    ] = None
    """
    HTML meta tag attribute maps injected into the rendered post page head.
    """

    owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    User metadata.name of the post owner.
    """

    pinned: bool = pydantic.Field()
    """
    Whether the post should be pinned ahead of normal post ordering.
    """

    priority: int = pydantic.Field()
    """
    Sorting priority. Higher values sort before lower values where priority ordering is applied.
    """

    publish: bool = pydantic.Field()
    """
    Desired publish state. False keeps the post as a draft or moves it back to draft.
    """

    publish_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="publishTime"),
        pydantic.Field(
            alias="publishTime", description="Time when the post was published or is scheduled to be published."
        ),
    ] = None
    """
    Time when the post was published or is scheduled to be published.
    """

    release_snapshot: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="releaseSnapshot"),
        pydantic.Field(
            alias="releaseSnapshot", description="Snapshot metadata.name selected as the published content version."
        ),
    ] = None
    """
    Snapshot metadata.name selected as the published content version.
    """

    slug: str = pydantic.Field()
    """
    URL slug used to build the post permalink.
    """

    tags: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Tag metadata.name values associated with the post.
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Theme template used to render this post.
    """

    title: str = pydantic.Field()
    """
    Display title of the post.
    """

    visible: PostSpecVisible = pydantic.Field()
    """
    Visibility used by theme-side and public REST queries; anonymous clients only receive PUBLIC posts.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
