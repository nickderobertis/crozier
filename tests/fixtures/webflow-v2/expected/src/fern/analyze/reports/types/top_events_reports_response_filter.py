

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .top_events_reports_response_filter_audience_ids import TopEventsReportsResponseFilterAudienceIds
from .top_events_reports_response_filter_browser import TopEventsReportsResponseFilterBrowser
from .top_events_reports_response_filter_collection_id import TopEventsReportsResponseFilterCollectionId
from .top_events_reports_response_filter_country import TopEventsReportsResponseFilterCountry
from .top_events_reports_response_filter_day_of_week import TopEventsReportsResponseFilterDayOfWeek
from .top_events_reports_response_filter_device_brand import TopEventsReportsResponseFilterDeviceBrand
from .top_events_reports_response_filter_device_type import TopEventsReportsResponseFilterDeviceType
from .top_events_reports_response_filter_domain import TopEventsReportsResponseFilterDomain
from .top_events_reports_response_filter_item_slug import TopEventsReportsResponseFilterItemSlug
from .top_events_reports_response_filter_language import TopEventsReportsResponseFilterLanguage
from .top_events_reports_response_filter_locale import TopEventsReportsResponseFilterLocale
from .top_events_reports_response_filter_os import TopEventsReportsResponseFilterOs
from .top_events_reports_response_filter_page_id import TopEventsReportsResponseFilterPageId
from .top_events_reports_response_filter_page_path import TopEventsReportsResponseFilterPagePath
from .top_events_reports_response_filter_region import TopEventsReportsResponseFilterRegion
from .top_events_reports_response_filter_time_of_day import TopEventsReportsResponseFilterTimeOfDay
from .top_events_reports_response_filter_timezone import TopEventsReportsResponseFilterTimezone
from .top_events_reports_response_filter_traffic_source import TopEventsReportsResponseFilterTrafficSource
from .top_events_reports_response_filter_utm_campaign import TopEventsReportsResponseFilterUtmCampaign
from .top_events_reports_response_filter_utm_content import TopEventsReportsResponseFilterUtmContent
from .top_events_reports_response_filter_utm_medium import TopEventsReportsResponseFilterUtmMedium
from .top_events_reports_response_filter_utm_source import TopEventsReportsResponseFilterUtmSource
from .top_events_reports_response_filter_utm_term import TopEventsReportsResponseFilterUtmTerm
from .top_events_reports_response_filter_visit_status import TopEventsReportsResponseFilterVisitStatus


class TopEventsReportsResponseFilter(UniversalBaseModel):
    """
    Filter the top events report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    audience_ids: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterAudienceIds],
        FieldMetadata(alias="audienceIds"),
        pydantic.Field(
            alias="audienceIds",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    browser: typing.Optional[TopEventsReportsResponseFilterBrowser] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterCollectionId],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    country: typing.Optional[TopEventsReportsResponseFilterCountry] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    day_of_week: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterDayOfWeek],
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
        typing.Optional[TopEventsReportsResponseFilterDeviceBrand],
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
        typing.Optional[TopEventsReportsResponseFilterDeviceType],
        FieldMetadata(alias="deviceType"),
        pydantic.Field(
            alias="deviceType",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    domain: typing.Optional[TopEventsReportsResponseFilterDomain] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterItemSlug],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    language: typing.Optional[TopEventsReportsResponseFilterLanguage] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    locale: typing.Optional[TopEventsReportsResponseFilterLocale] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    os: typing.Optional[TopEventsReportsResponseFilterOs] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterPageId],
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
        typing.Optional[TopEventsReportsResponseFilterPagePath],
        FieldMetadata(alias="pagePath"),
        pydantic.Field(
            alias="pagePath",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    region: typing.Optional[TopEventsReportsResponseFilterRegion] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    time_of_day: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterTimeOfDay],
        FieldMetadata(alias="timeOfDay"),
        pydantic.Field(
            alias="timeOfDay",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    timezone: typing.Optional[TopEventsReportsResponseFilterTimezone] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    traffic_source: typing_extensions.Annotated[
        typing.Optional[TopEventsReportsResponseFilterTrafficSource],
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
        typing.Optional[TopEventsReportsResponseFilterUtmCampaign],
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
        typing.Optional[TopEventsReportsResponseFilterUtmContent],
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
        typing.Optional[TopEventsReportsResponseFilterUtmMedium],
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
        typing.Optional[TopEventsReportsResponseFilterUtmSource],
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
        typing.Optional[TopEventsReportsResponseFilterUtmTerm],
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
        typing.Optional[TopEventsReportsResponseFilterVisitStatus],
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
