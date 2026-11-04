

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .excerpt import Excerpt
from .single_page_spec_visible import SinglePageSpecVisible


class SinglePageSpec(UniversalBaseModel):
    """
    Desired single page content, publication, and rendering configuration.
    """

    allow_comment: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="allowComment"),
        pydantic.Field(alias="allowComment", description="Whether new comments are allowed for this single page."),
    ]
    """
    Whether new comments are allowed for this single page.
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

    cover: typing.Optional[str] = pydantic.Field(default=None)
    """
    Cover image URL or attachment URI of the single page.
    """

    deleted: bool = pydantic.Field()
    """
    Whether the single page is logically deleted and should be treated as recycled.
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
            alias="htmlMetas", description="HTML meta tag attribute maps injected into the rendered single page head."
        ),
    ] = None
    """
    HTML meta tag attribute maps injected into the rendered single page head.
    """

    owner: typing.Optional[str] = pydantic.Field(default=None)
    """
    User metadata.name of the single page owner.
    """

    pinned: bool = pydantic.Field()
    """
    Whether the single page should be pinned ahead of normal page ordering.
    """

    priority: int = pydantic.Field()
    """
    Sorting priority. Higher values sort before lower values where priority ordering is applied.
    """

    publish: bool = pydantic.Field()
    """
    Desired publish state. False keeps the single page as a draft or moves it back to draft.
    """

    publish_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="publishTime"),
        pydantic.Field(
            alias="publishTime", description="Time when the single page was published or is scheduled to be published."
        ),
    ] = None
    """
    Time when the single page was published or is scheduled to be published.
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
    URL slug used to build the single page permalink.
    """

    template: typing.Optional[str] = pydantic.Field(default=None)
    """
    Theme template used to render this single page.
    """

    title: str = pydantic.Field()
    """
    Display title of the single page.
    """

    visible: SinglePageSpecVisible = pydantic.Field()
    """
    Visibility used by theme-side and public REST queries; anonymous clients only receive PUBLIC single pages.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
