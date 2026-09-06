

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .time_on_page_reports_request_filter_audience_ids import TimeOnPageReportsRequestFilterAudienceIds
from .time_on_page_reports_request_filter_browser import TimeOnPageReportsRequestFilterBrowser
from .time_on_page_reports_request_filter_collection_id import TimeOnPageReportsRequestFilterCollectionId
from .time_on_page_reports_request_filter_country import TimeOnPageReportsRequestFilterCountry
from .time_on_page_reports_request_filter_day_of_week import TimeOnPageReportsRequestFilterDayOfWeek
from .time_on_page_reports_request_filter_device_brand import TimeOnPageReportsRequestFilterDeviceBrand
from .time_on_page_reports_request_filter_device_type import TimeOnPageReportsRequestFilterDeviceType
from .time_on_page_reports_request_filter_domain import TimeOnPageReportsRequestFilterDomain
from .time_on_page_reports_request_filter_item_slug import TimeOnPageReportsRequestFilterItemSlug
from .time_on_page_reports_request_filter_language import TimeOnPageReportsRequestFilterLanguage
from .time_on_page_reports_request_filter_locale import TimeOnPageReportsRequestFilterLocale
from .time_on_page_reports_request_filter_next_collection_id import TimeOnPageReportsRequestFilterNextCollectionId
from .time_on_page_reports_request_filter_next_item_slug import TimeOnPageReportsRequestFilterNextItemSlug
from .time_on_page_reports_request_filter_next_page_id import TimeOnPageReportsRequestFilterNextPageId
from .time_on_page_reports_request_filter_os import TimeOnPageReportsRequestFilterOs
from .time_on_page_reports_request_filter_page_id import TimeOnPageReportsRequestFilterPageId
from .time_on_page_reports_request_filter_page_path import TimeOnPageReportsRequestFilterPagePath
from .time_on_page_reports_request_filter_previous_collection_id import (
    TimeOnPageReportsRequestFilterPreviousCollectionId,
)
from .time_on_page_reports_request_filter_previous_item_slug import TimeOnPageReportsRequestFilterPreviousItemSlug
from .time_on_page_reports_request_filter_previous_page_id import TimeOnPageReportsRequestFilterPreviousPageId
from .time_on_page_reports_request_filter_referrer import TimeOnPageReportsRequestFilterReferrer
from .time_on_page_reports_request_filter_region import TimeOnPageReportsRequestFilterRegion
from .time_on_page_reports_request_filter_time_of_day import TimeOnPageReportsRequestFilterTimeOfDay
from .time_on_page_reports_request_filter_timezone import TimeOnPageReportsRequestFilterTimezone
from .time_on_page_reports_request_filter_traffic_source import TimeOnPageReportsRequestFilterTrafficSource
from .time_on_page_reports_request_filter_utm_campaign import TimeOnPageReportsRequestFilterUtmCampaign
from .time_on_page_reports_request_filter_utm_content import TimeOnPageReportsRequestFilterUtmContent
from .time_on_page_reports_request_filter_utm_medium import TimeOnPageReportsRequestFilterUtmMedium
from .time_on_page_reports_request_filter_utm_source import TimeOnPageReportsRequestFilterUtmSource
from .time_on_page_reports_request_filter_utm_term import TimeOnPageReportsRequestFilterUtmTerm
from .time_on_page_reports_request_filter_visit_status import TimeOnPageReportsRequestFilterVisitStatus


class TimeOnPageReportsRequestFilter(UniversalBaseModel):
    """
    Filter the time on page report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    audience_ids: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterAudienceIds],
        FieldMetadata(alias="audienceIds"),
        pydantic.Field(
            alias="audienceIds",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    browser: typing.Optional[TimeOnPageReportsRequestFilterBrowser] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterCollectionId],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    country: typing.Optional[TimeOnPageReportsRequestFilterCountry] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    day_of_week: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterDayOfWeek],
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
        typing.Optional[TimeOnPageReportsRequestFilterDeviceBrand],
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
        typing.Optional[TimeOnPageReportsRequestFilterDeviceType],
        FieldMetadata(alias="deviceType"),
        pydantic.Field(
            alias="deviceType",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    domain: typing.Optional[TimeOnPageReportsRequestFilterDomain] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterItemSlug],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    language: typing.Optional[TimeOnPageReportsRequestFilterLanguage] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    locale: typing.Optional[TimeOnPageReportsRequestFilterLocale] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_collection_id: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterNextCollectionId],
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
        typing.Optional[TimeOnPageReportsRequestFilterNextItemSlug],
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
        typing.Optional[TimeOnPageReportsRequestFilterNextPageId],
        FieldMetadata(alias="nextPageId"),
        pydantic.Field(
            alias="nextPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    os: typing.Optional[TimeOnPageReportsRequestFilterOs] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterPageId],
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
        typing.Optional[TimeOnPageReportsRequestFilterPagePath],
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
        typing.Optional[TimeOnPageReportsRequestFilterPreviousCollectionId],
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
        typing.Optional[TimeOnPageReportsRequestFilterPreviousItemSlug],
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
        typing.Optional[TimeOnPageReportsRequestFilterPreviousPageId],
        FieldMetadata(alias="previousPageId"),
        pydantic.Field(
            alias="previousPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    referrer: typing.Optional[TimeOnPageReportsRequestFilterReferrer] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    region: typing.Optional[TimeOnPageReportsRequestFilterRegion] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    time_of_day: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterTimeOfDay],
        FieldMetadata(alias="timeOfDay"),
        pydantic.Field(
            alias="timeOfDay",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    timezone: typing.Optional[TimeOnPageReportsRequestFilterTimezone] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    traffic_source: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsRequestFilterTrafficSource],
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
        typing.Optional[TimeOnPageReportsRequestFilterUtmCampaign],
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
        typing.Optional[TimeOnPageReportsRequestFilterUtmContent],
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
        typing.Optional[TimeOnPageReportsRequestFilterUtmMedium],
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
        typing.Optional[TimeOnPageReportsRequestFilterUtmSource],
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
        typing.Optional[TimeOnPageReportsRequestFilterUtmTerm],
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
        typing.Optional[TimeOnPageReportsRequestFilterVisitStatus],
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
