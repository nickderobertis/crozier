

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .time_on_page_reports_response_filter_audience_ids import TimeOnPageReportsResponseFilterAudienceIds
from .time_on_page_reports_response_filter_browser import TimeOnPageReportsResponseFilterBrowser
from .time_on_page_reports_response_filter_collection_id import TimeOnPageReportsResponseFilterCollectionId
from .time_on_page_reports_response_filter_country import TimeOnPageReportsResponseFilterCountry
from .time_on_page_reports_response_filter_day_of_week import TimeOnPageReportsResponseFilterDayOfWeek
from .time_on_page_reports_response_filter_device_brand import TimeOnPageReportsResponseFilterDeviceBrand
from .time_on_page_reports_response_filter_device_type import TimeOnPageReportsResponseFilterDeviceType
from .time_on_page_reports_response_filter_domain import TimeOnPageReportsResponseFilterDomain
from .time_on_page_reports_response_filter_item_slug import TimeOnPageReportsResponseFilterItemSlug
from .time_on_page_reports_response_filter_language import TimeOnPageReportsResponseFilterLanguage
from .time_on_page_reports_response_filter_locale import TimeOnPageReportsResponseFilterLocale
from .time_on_page_reports_response_filter_next_collection_id import TimeOnPageReportsResponseFilterNextCollectionId
from .time_on_page_reports_response_filter_next_item_slug import TimeOnPageReportsResponseFilterNextItemSlug
from .time_on_page_reports_response_filter_next_page_id import TimeOnPageReportsResponseFilterNextPageId
from .time_on_page_reports_response_filter_os import TimeOnPageReportsResponseFilterOs
from .time_on_page_reports_response_filter_page_id import TimeOnPageReportsResponseFilterPageId
from .time_on_page_reports_response_filter_page_path import TimeOnPageReportsResponseFilterPagePath
from .time_on_page_reports_response_filter_previous_collection_id import (
    TimeOnPageReportsResponseFilterPreviousCollectionId,
)
from .time_on_page_reports_response_filter_previous_item_slug import TimeOnPageReportsResponseFilterPreviousItemSlug
from .time_on_page_reports_response_filter_previous_page_id import TimeOnPageReportsResponseFilterPreviousPageId
from .time_on_page_reports_response_filter_referrer import TimeOnPageReportsResponseFilterReferrer
from .time_on_page_reports_response_filter_region import TimeOnPageReportsResponseFilterRegion
from .time_on_page_reports_response_filter_time_of_day import TimeOnPageReportsResponseFilterTimeOfDay
from .time_on_page_reports_response_filter_timezone import TimeOnPageReportsResponseFilterTimezone
from .time_on_page_reports_response_filter_traffic_source import TimeOnPageReportsResponseFilterTrafficSource
from .time_on_page_reports_response_filter_utm_campaign import TimeOnPageReportsResponseFilterUtmCampaign
from .time_on_page_reports_response_filter_utm_content import TimeOnPageReportsResponseFilterUtmContent
from .time_on_page_reports_response_filter_utm_medium import TimeOnPageReportsResponseFilterUtmMedium
from .time_on_page_reports_response_filter_utm_source import TimeOnPageReportsResponseFilterUtmSource
from .time_on_page_reports_response_filter_utm_term import TimeOnPageReportsResponseFilterUtmTerm
from .time_on_page_reports_response_filter_visit_status import TimeOnPageReportsResponseFilterVisitStatus


class TimeOnPageReportsResponseFilter(UniversalBaseModel):
    """
    Filter the time on page report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    audience_ids: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterAudienceIds],
        FieldMetadata(alias="audienceIds"),
        pydantic.Field(
            alias="audienceIds",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    browser: typing.Optional[TimeOnPageReportsResponseFilterBrowser] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterCollectionId],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    country: typing.Optional[TimeOnPageReportsResponseFilterCountry] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    day_of_week: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterDayOfWeek],
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
        typing.Optional[TimeOnPageReportsResponseFilterDeviceBrand],
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
        typing.Optional[TimeOnPageReportsResponseFilterDeviceType],
        FieldMetadata(alias="deviceType"),
        pydantic.Field(
            alias="deviceType",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    domain: typing.Optional[TimeOnPageReportsResponseFilterDomain] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterItemSlug],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    language: typing.Optional[TimeOnPageReportsResponseFilterLanguage] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    locale: typing.Optional[TimeOnPageReportsResponseFilterLocale] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_collection_id: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterNextCollectionId],
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
        typing.Optional[TimeOnPageReportsResponseFilterNextItemSlug],
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
        typing.Optional[TimeOnPageReportsResponseFilterNextPageId],
        FieldMetadata(alias="nextPageId"),
        pydantic.Field(
            alias="nextPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    os: typing.Optional[TimeOnPageReportsResponseFilterOs] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterPageId],
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
        typing.Optional[TimeOnPageReportsResponseFilterPagePath],
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
        typing.Optional[TimeOnPageReportsResponseFilterPreviousCollectionId],
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
        typing.Optional[TimeOnPageReportsResponseFilterPreviousItemSlug],
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
        typing.Optional[TimeOnPageReportsResponseFilterPreviousPageId],
        FieldMetadata(alias="previousPageId"),
        pydantic.Field(
            alias="previousPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    referrer: typing.Optional[TimeOnPageReportsResponseFilterReferrer] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    region: typing.Optional[TimeOnPageReportsResponseFilterRegion] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    time_of_day: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterTimeOfDay],
        FieldMetadata(alias="timeOfDay"),
        pydantic.Field(
            alias="timeOfDay",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    timezone: typing.Optional[TimeOnPageReportsResponseFilterTimezone] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    traffic_source: typing_extensions.Annotated[
        typing.Optional[TimeOnPageReportsResponseFilterTrafficSource],
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
        typing.Optional[TimeOnPageReportsResponseFilterUtmCampaign],
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
        typing.Optional[TimeOnPageReportsResponseFilterUtmContent],
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
        typing.Optional[TimeOnPageReportsResponseFilterUtmMedium],
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
        typing.Optional[TimeOnPageReportsResponseFilterUtmSource],
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
        typing.Optional[TimeOnPageReportsResponseFilterUtmTerm],
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
        typing.Optional[TimeOnPageReportsResponseFilterVisitStatus],
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
