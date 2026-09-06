

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .top_pages_reports_response_data_item_timeseries_item import TopPagesReportsResponseDataItemTimeseriesItem


class TopPagesReportsResponseDataItem(UniversalBaseModel):
    """
    A single page in the ranked response. Every row carries all three scope counts (`sessionCount`, `userCount`, `pageviewCount`); `sortBy` governs only the row ordering.
    """

    page_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="pageId"),
        pydantic.Field(alias="pageId", description="Identifier of the Webflow page."),
    ]
    """
    Identifier of the Webflow page.
    """

    title: str = pydantic.Field()
    """
    Display title for the page. Resolves to the page's CMS item name when applicable, otherwise the page label. Falls back to `pageId` when no title is available.
    """

    session_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="sessionCount"),
        pydantic.Field(
            alias="sessionCount", description="Sessions attributed to this page during the requested window."
        ),
    ]
    """
    Sessions attributed to this page during the requested window.
    """

    user_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="userCount"),
        pydantic.Field(
            alias="userCount", description="Unique users that visited this page during the requested window."
        ),
    ]
    """
    Unique users that visited this page during the requested window.
    """

    pageview_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="pageviewCount"),
        pydantic.Field(
            alias="pageviewCount", description="Pageviews recorded for this page during the requested window."
        ),
    ]
    """
    Pageviews recorded for this page during the requested window.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Identifier of the CMS collection this page belongs to. Present only for CMS-templated pages.",
        ),
    ] = None
    """
    Identifier of the CMS collection this page belongs to. Present only for CMS-templated pages.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Slug of the CMS item this row represents. Present only for CMS-templated pages.",
        ),
    ] = None
    """
    Slug of the CMS item this row represents. Present only for CMS-templated pages.
    """

    timeseries: typing.Optional[typing.List[TopPagesReportsResponseDataItemTimeseriesItem]] = pydantic.Field(
        default=None
    )
    """
    Daily pageview timeseries for this page over the requested window. Returned when `timeseries` is requested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
