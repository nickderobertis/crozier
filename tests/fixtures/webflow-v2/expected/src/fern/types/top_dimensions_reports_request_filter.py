

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .top_dimensions_reports_request_filter_audience_ids import TopDimensionsReportsRequestFilterAudienceIds
from .top_dimensions_reports_request_filter_browser import TopDimensionsReportsRequestFilterBrowser
from .top_dimensions_reports_request_filter_collection_id import TopDimensionsReportsRequestFilterCollectionId
from .top_dimensions_reports_request_filter_country import TopDimensionsReportsRequestFilterCountry
from .top_dimensions_reports_request_filter_day_of_week import TopDimensionsReportsRequestFilterDayOfWeek
from .top_dimensions_reports_request_filter_device_brand import TopDimensionsReportsRequestFilterDeviceBrand
from .top_dimensions_reports_request_filter_device_type import TopDimensionsReportsRequestFilterDeviceType
from .top_dimensions_reports_request_filter_domain import TopDimensionsReportsRequestFilterDomain
from .top_dimensions_reports_request_filter_item_slug import TopDimensionsReportsRequestFilterItemSlug
from .top_dimensions_reports_request_filter_language import TopDimensionsReportsRequestFilterLanguage
from .top_dimensions_reports_request_filter_locale import TopDimensionsReportsRequestFilterLocale
from .top_dimensions_reports_request_filter_next_collection_id import TopDimensionsReportsRequestFilterNextCollectionId
from .top_dimensions_reports_request_filter_next_item_slug import TopDimensionsReportsRequestFilterNextItemSlug
from .top_dimensions_reports_request_filter_next_page_id import TopDimensionsReportsRequestFilterNextPageId
from .top_dimensions_reports_request_filter_os import TopDimensionsReportsRequestFilterOs
from .top_dimensions_reports_request_filter_page_id import TopDimensionsReportsRequestFilterPageId
from .top_dimensions_reports_request_filter_page_path import TopDimensionsReportsRequestFilterPagePath
from .top_dimensions_reports_request_filter_previous_collection_id import (
    TopDimensionsReportsRequestFilterPreviousCollectionId,
)
from .top_dimensions_reports_request_filter_previous_item_slug import TopDimensionsReportsRequestFilterPreviousItemSlug
from .top_dimensions_reports_request_filter_previous_page_id import TopDimensionsReportsRequestFilterPreviousPageId
from .top_dimensions_reports_request_filter_referrer import TopDimensionsReportsRequestFilterReferrer
from .top_dimensions_reports_request_filter_region import TopDimensionsReportsRequestFilterRegion
from .top_dimensions_reports_request_filter_time_of_day import TopDimensionsReportsRequestFilterTimeOfDay
from .top_dimensions_reports_request_filter_timezone import TopDimensionsReportsRequestFilterTimezone
from .top_dimensions_reports_request_filter_traffic_source import TopDimensionsReportsRequestFilterTrafficSource
from .top_dimensions_reports_request_filter_utm_campaign import TopDimensionsReportsRequestFilterUtmCampaign
from .top_dimensions_reports_request_filter_utm_content import TopDimensionsReportsRequestFilterUtmContent
from .top_dimensions_reports_request_filter_utm_medium import TopDimensionsReportsRequestFilterUtmMedium
from .top_dimensions_reports_request_filter_utm_source import TopDimensionsReportsRequestFilterUtmSource
from .top_dimensions_reports_request_filter_utm_term import TopDimensionsReportsRequestFilterUtmTerm
from .top_dimensions_reports_request_filter_visit_status import TopDimensionsReportsRequestFilterVisitStatus


class TopDimensionsReportsRequestFilter(UniversalBaseModel):
    """
    Filter the top dimensions report by dimension. Each property is an optional set of `AnalyzeFilterOperators` (`eq`, `in`, `ne`, `nin`) applied to the named dimension. Filter a given dimension in one place — either inside `filter` or as a top-level query parameter.
    """

    audience_ids: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterAudienceIds],
        FieldMetadata(alias="audienceIds"),
        pydantic.Field(
            alias="audienceIds",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    browser: typing.Optional[TopDimensionsReportsRequestFilterBrowser] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterCollectionId],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    country: typing.Optional[TopDimensionsReportsRequestFilterCountry] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    day_of_week: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterDayOfWeek],
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
        typing.Optional[TopDimensionsReportsRequestFilterDeviceBrand],
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
        typing.Optional[TopDimensionsReportsRequestFilterDeviceType],
        FieldMetadata(alias="deviceType"),
        pydantic.Field(
            alias="deviceType",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    domain: typing.Optional[TopDimensionsReportsRequestFilterDomain] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterItemSlug],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    language: typing.Optional[TopDimensionsReportsRequestFilterLanguage] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    locale: typing.Optional[TopDimensionsReportsRequestFilterLocale] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    next_collection_id: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterNextCollectionId],
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
        typing.Optional[TopDimensionsReportsRequestFilterNextItemSlug],
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
        typing.Optional[TopDimensionsReportsRequestFilterNextPageId],
        FieldMetadata(alias="nextPageId"),
        pydantic.Field(
            alias="nextPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    os: typing.Optional[TopDimensionsReportsRequestFilterOs] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterPageId],
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
        typing.Optional[TopDimensionsReportsRequestFilterPagePath],
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
        typing.Optional[TopDimensionsReportsRequestFilterPreviousCollectionId],
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
        typing.Optional[TopDimensionsReportsRequestFilterPreviousItemSlug],
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
        typing.Optional[TopDimensionsReportsRequestFilterPreviousPageId],
        FieldMetadata(alias="previousPageId"),
        pydantic.Field(
            alias="previousPageId",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    referrer: typing.Optional[TopDimensionsReportsRequestFilterReferrer] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    region: typing.Optional[TopDimensionsReportsRequestFilterRegion] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    time_of_day: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterTimeOfDay],
        FieldMetadata(alias="timeOfDay"),
        pydantic.Field(
            alias="timeOfDay",
            description="Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.",
        ),
    ] = None
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    timezone: typing.Optional[TopDimensionsReportsRequestFilterTimezone] = pydantic.Field(default=None)
    """
    Operators for filtering a single dimension. Specify at least one of `eq`, `in`, `ne`, or `nin`.
    """

    traffic_source: typing_extensions.Annotated[
        typing.Optional[TopDimensionsReportsRequestFilterTrafficSource],
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
        typing.Optional[TopDimensionsReportsRequestFilterUtmCampaign],
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
        typing.Optional[TopDimensionsReportsRequestFilterUtmContent],
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
        typing.Optional[TopDimensionsReportsRequestFilterUtmMedium],
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
        typing.Optional[TopDimensionsReportsRequestFilterUtmSource],
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
        typing.Optional[TopDimensionsReportsRequestFilterUtmTerm],
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
        typing.Optional[TopDimensionsReportsRequestFilterVisitStatus],
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
