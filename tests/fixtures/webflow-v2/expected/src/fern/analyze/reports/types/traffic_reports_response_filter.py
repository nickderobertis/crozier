

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .traffic_reports_response_filter_audience_ids import TrafficReportsResponseFilterAudienceIds
from .traffic_reports_response_filter_browser import TrafficReportsResponseFilterBrowser
from .traffic_reports_response_filter_collection_id import TrafficReportsResponseFilterCollectionId
from .traffic_reports_response_filter_country import TrafficReportsResponseFilterCountry
from .traffic_reports_response_filter_day_of_week import TrafficReportsResponseFilterDayOfWeek
from .traffic_reports_response_filter_device_brand import TrafficReportsResponseFilterDeviceBrand
from .traffic_reports_response_filter_device_type import TrafficReportsResponseFilterDeviceType
from .traffic_reports_response_filter_domain import TrafficReportsResponseFilterDomain
from .traffic_reports_response_filter_item_slug import TrafficReportsResponseFilterItemSlug
from .traffic_reports_response_filter_language import TrafficReportsResponseFilterLanguage
from .traffic_reports_response_filter_locale import TrafficReportsResponseFilterLocale
from .traffic_reports_response_filter_next_collection_id import TrafficReportsResponseFilterNextCollectionId
from .traffic_reports_response_filter_next_item_slug import TrafficReportsResponseFilterNextItemSlug
from .traffic_reports_response_filter_next_page_id import TrafficReportsResponseFilterNextPageId
from .traffic_reports_response_filter_os import TrafficReportsResponseFilterOs
from .traffic_reports_response_filter_page_id import TrafficReportsResponseFilterPageId
from .traffic_reports_response_filter_page_path import TrafficReportsResponseFilterPagePath
from .traffic_reports_response_filter_previous_collection_id import TrafficReportsResponseFilterPreviousCollectionId
from .traffic_reports_response_filter_previous_item_slug import TrafficReportsResponseFilterPreviousItemSlug
from .traffic_reports_response_filter_previous_page_id import TrafficReportsResponseFilterPreviousPageId
from .traffic_reports_response_filter_referrer import TrafficReportsResponseFilterReferrer
from .traffic_reports_response_filter_region import TrafficReportsResponseFilterRegion
from .traffic_reports_response_filter_time_of_day import TrafficReportsResponseFilterTimeOfDay
from .traffic_reports_response_filter_timezone import TrafficReportsResponseFilterTimezone
from .traffic_reports_response_filter_traffic_source import TrafficReportsResponseFilterTrafficSource
from .traffic_reports_response_filter_utm_campaign import TrafficReportsResponseFilterUtmCampaign
from .traffic_reports_response_filter_utm_content import TrafficReportsResponseFilterUtmContent
from .traffic_reports_response_filter_utm_medium import TrafficReportsResponseFilterUtmMedium
from .traffic_reports_response_filter_utm_source import TrafficReportsResponseFilterUtmSource
from .traffic_reports_response_filter_utm_term import TrafficReportsResponseFilterUtmTerm
from .traffic_reports_response_filter_visit_status import TrafficReportsResponseFilterVisitStatus


class TrafficReportsResponseFilter(UniversalBaseModel):
    """
    Filter the traffic report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    audience_ids: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterAudienceIds],
        FieldMetadata(alias="audienceIds"),
        pydantic.Field(
            alias="audienceIds",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    browser: typing.Optional[TrafficReportsResponseFilterBrowser] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterCollectionId],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    country: typing.Optional[TrafficReportsResponseFilterCountry] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    day_of_week: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterDayOfWeek],
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
        typing.Optional[TrafficReportsResponseFilterDeviceBrand],
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
        typing.Optional[TrafficReportsResponseFilterDeviceType],
        FieldMetadata(alias="deviceType"),
        pydantic.Field(
            alias="deviceType",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    domain: typing.Optional[TrafficReportsResponseFilterDomain] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterItemSlug],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    language: typing.Optional[TrafficReportsResponseFilterLanguage] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    locale: typing.Optional[TrafficReportsResponseFilterLocale] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_collection_id: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterNextCollectionId],
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
        typing.Optional[TrafficReportsResponseFilterNextItemSlug],
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
        typing.Optional[TrafficReportsResponseFilterNextPageId],
        FieldMetadata(alias="nextPageId"),
        pydantic.Field(
            alias="nextPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    os: typing.Optional[TrafficReportsResponseFilterOs] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterPageId],
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
        typing.Optional[TrafficReportsResponseFilterPagePath],
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
        typing.Optional[TrafficReportsResponseFilterPreviousCollectionId],
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
        typing.Optional[TrafficReportsResponseFilterPreviousItemSlug],
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
        typing.Optional[TrafficReportsResponseFilterPreviousPageId],
        FieldMetadata(alias="previousPageId"),
        pydantic.Field(
            alias="previousPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    referrer: typing.Optional[TrafficReportsResponseFilterReferrer] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    region: typing.Optional[TrafficReportsResponseFilterRegion] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    time_of_day: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterTimeOfDay],
        FieldMetadata(alias="timeOfDay"),
        pydantic.Field(
            alias="timeOfDay",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    timezone: typing.Optional[TrafficReportsResponseFilterTimezone] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    traffic_source: typing_extensions.Annotated[
        typing.Optional[TrafficReportsResponseFilterTrafficSource],
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
        typing.Optional[TrafficReportsResponseFilterUtmCampaign],
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
        typing.Optional[TrafficReportsResponseFilterUtmContent],
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
        typing.Optional[TrafficReportsResponseFilterUtmMedium],
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
        typing.Optional[TrafficReportsResponseFilterUtmSource],
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
        typing.Optional[TrafficReportsResponseFilterUtmTerm],
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
        typing.Optional[TrafficReportsResponseFilterVisitStatus],
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
