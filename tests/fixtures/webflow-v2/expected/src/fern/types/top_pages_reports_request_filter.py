

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .top_pages_reports_request_filter_audience_ids import TopPagesReportsRequestFilterAudienceIds
from .top_pages_reports_request_filter_browser import TopPagesReportsRequestFilterBrowser
from .top_pages_reports_request_filter_collection_id import TopPagesReportsRequestFilterCollectionId
from .top_pages_reports_request_filter_country import TopPagesReportsRequestFilterCountry
from .top_pages_reports_request_filter_day_of_week import TopPagesReportsRequestFilterDayOfWeek
from .top_pages_reports_request_filter_device_brand import TopPagesReportsRequestFilterDeviceBrand
from .top_pages_reports_request_filter_device_type import TopPagesReportsRequestFilterDeviceType
from .top_pages_reports_request_filter_domain import TopPagesReportsRequestFilterDomain
from .top_pages_reports_request_filter_item_slug import TopPagesReportsRequestFilterItemSlug
from .top_pages_reports_request_filter_language import TopPagesReportsRequestFilterLanguage
from .top_pages_reports_request_filter_locale import TopPagesReportsRequestFilterLocale
from .top_pages_reports_request_filter_next_collection_id import TopPagesReportsRequestFilterNextCollectionId
from .top_pages_reports_request_filter_next_item_slug import TopPagesReportsRequestFilterNextItemSlug
from .top_pages_reports_request_filter_next_page_id import TopPagesReportsRequestFilterNextPageId
from .top_pages_reports_request_filter_os import TopPagesReportsRequestFilterOs
from .top_pages_reports_request_filter_page_id import TopPagesReportsRequestFilterPageId
from .top_pages_reports_request_filter_page_path import TopPagesReportsRequestFilterPagePath
from .top_pages_reports_request_filter_previous_collection_id import TopPagesReportsRequestFilterPreviousCollectionId
from .top_pages_reports_request_filter_previous_item_slug import TopPagesReportsRequestFilterPreviousItemSlug
from .top_pages_reports_request_filter_previous_page_id import TopPagesReportsRequestFilterPreviousPageId
from .top_pages_reports_request_filter_referrer import TopPagesReportsRequestFilterReferrer
from .top_pages_reports_request_filter_region import TopPagesReportsRequestFilterRegion
from .top_pages_reports_request_filter_time_of_day import TopPagesReportsRequestFilterTimeOfDay
from .top_pages_reports_request_filter_timezone import TopPagesReportsRequestFilterTimezone
from .top_pages_reports_request_filter_traffic_source import TopPagesReportsRequestFilterTrafficSource
from .top_pages_reports_request_filter_utm_campaign import TopPagesReportsRequestFilterUtmCampaign
from .top_pages_reports_request_filter_utm_content import TopPagesReportsRequestFilterUtmContent
from .top_pages_reports_request_filter_utm_medium import TopPagesReportsRequestFilterUtmMedium
from .top_pages_reports_request_filter_utm_source import TopPagesReportsRequestFilterUtmSource
from .top_pages_reports_request_filter_utm_term import TopPagesReportsRequestFilterUtmTerm
from .top_pages_reports_request_filter_visit_status import TopPagesReportsRequestFilterVisitStatus


class TopPagesReportsRequestFilter(UniversalBaseModel):
    """
    Filter the top pages report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    audience_ids: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterAudienceIds],
        FieldMetadata(alias="audienceIds"),
        pydantic.Field(
            alias="audienceIds",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    browser: typing.Optional[TopPagesReportsRequestFilterBrowser] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterCollectionId],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    country: typing.Optional[TopPagesReportsRequestFilterCountry] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    day_of_week: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterDayOfWeek],
        FieldMetadata(alias="dayOfWeek"),
        pydantic.Field(
            alias="dayOfWeek",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    device_brand: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterDeviceBrand],
        FieldMetadata(alias="deviceBrand"),
        pydantic.Field(
            alias="deviceBrand",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    device_type: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterDeviceType],
        FieldMetadata(alias="deviceType"),
        pydantic.Field(
            alias="deviceType",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    domain: typing.Optional[TopPagesReportsRequestFilterDomain] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterItemSlug],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    language: typing.Optional[TopPagesReportsRequestFilterLanguage] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    locale: typing.Optional[TopPagesReportsRequestFilterLocale] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_collection_id: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterNextCollectionId],
        FieldMetadata(alias="nextCollectionId"),
        pydantic.Field(
            alias="nextCollectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_item_slug: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterNextItemSlug],
        FieldMetadata(alias="nextItemSlug"),
        pydantic.Field(
            alias="nextItemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_page_id: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterNextPageId],
        FieldMetadata(alias="nextPageId"),
        pydantic.Field(
            alias="nextPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    os: typing.Optional[TopPagesReportsRequestFilterOs] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterPageId],
        FieldMetadata(alias="pageId"),
        pydantic.Field(
            alias="pageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_path: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterPagePath],
        FieldMetadata(alias="pagePath"),
        pydantic.Field(
            alias="pagePath",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    previous_collection_id: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterPreviousCollectionId],
        FieldMetadata(alias="previousCollectionId"),
        pydantic.Field(
            alias="previousCollectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    previous_item_slug: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterPreviousItemSlug],
        FieldMetadata(alias="previousItemSlug"),
        pydantic.Field(
            alias="previousItemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    previous_page_id: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterPreviousPageId],
        FieldMetadata(alias="previousPageId"),
        pydantic.Field(
            alias="previousPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    referrer: typing.Optional[TopPagesReportsRequestFilterReferrer] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    region: typing.Optional[TopPagesReportsRequestFilterRegion] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    time_of_day: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterTimeOfDay],
        FieldMetadata(alias="timeOfDay"),
        pydantic.Field(
            alias="timeOfDay",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    timezone: typing.Optional[TopPagesReportsRequestFilterTimezone] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    traffic_source: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterTrafficSource],
        FieldMetadata(alias="trafficSource"),
        pydantic.Field(
            alias="trafficSource",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    utm_campaign: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterUtmCampaign],
        FieldMetadata(alias="utmCampaign"),
        pydantic.Field(
            alias="utmCampaign",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    utm_content: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterUtmContent],
        FieldMetadata(alias="utmContent"),
        pydantic.Field(
            alias="utmContent",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    utm_medium: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterUtmMedium],
        FieldMetadata(alias="utmMedium"),
        pydantic.Field(
            alias="utmMedium",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    utm_source: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterUtmSource],
        FieldMetadata(alias="utmSource"),
        pydantic.Field(
            alias="utmSource",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    utm_term: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterUtmTerm],
        FieldMetadata(alias="utmTerm"),
        pydantic.Field(
            alias="utmTerm",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    visit_status: typing_extensions.Annotated[
        typing.Optional[TopPagesReportsRequestFilterVisitStatus],
        FieldMetadata(alias="visitStatus"),
        pydantic.Field(
            alias="visitStatus",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
