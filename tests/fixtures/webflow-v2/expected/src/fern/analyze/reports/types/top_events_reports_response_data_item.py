

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata
from .top_events_reports_response_data_item_cms_context_item import TopEventsReportsResponseDataItemCmsContextItem
from .top_events_reports_response_data_item_component_context_item import (
    TopEventsReportsResponseDataItemComponentContextItem,
)
from .top_events_reports_response_data_item_timeseries_item import TopEventsReportsResponseDataItemTimeseriesItem


class TopEventsReportsResponseDataItem(UniversalBaseModel):
    """
    A single event in the ranked response, with its event count over the requested window. Events are counted individually, not rolled up into sessions, users, or pageviews, so this report has no `metricScope` — `count` is always the number of times the event fired.
    """

    event_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="eventId"),
        pydantic.Field(alias="eventId", description="Opaque identifier of the event."),
    ]
    """
    Opaque identifier of the event.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name of the event. Omitted when the event has no name (customer-defined events may leave it blank).
    """

    page_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageId"),
        pydantic.Field(
            alias="pageId",
            description="Identifier of the Webflow page the event is associated with. Omitted when the upstream has no page context for the event.",
        ),
    ] = None
    """
    Identifier of the Webflow page the event is associated with. Omitted when the upstream has no page context for the event.
    """

    page_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="pageName"),
        pydantic.Field(
            alias="pageName", description="Display name of the associated page. Omitted when the page label is unknown."
        ),
    ] = None
    """
    Display name of the associated page. Omitted when the page label is unknown.
    """

    count: int = pydantic.Field()
    """
    Number of times the event fired during the requested window.
    """

    component_context: typing_extensions.Annotated[
        typing.Optional[typing.List[TopEventsReportsResponseDataItemComponentContextItem]],
        FieldMetadata(alias="componentContext"),
        pydantic.Field(
            alias="componentContext",
            description="Component rendering context for the event. Omitted when the event is not rendered inside a component.",
        ),
    ] = None
    """
    Component rendering context for the event. Omitted when the event is not rendered inside a component.
    """

    cms_context: typing_extensions.Annotated[
        typing.Optional[typing.List[TopEventsReportsResponseDataItemCmsContextItem]],
        FieldMetadata(alias="cmsContext"),
        pydantic.Field(
            alias="cmsContext",
            description="CMS collection-list rendering context for the event. Omitted when the event is not rendered inside a CMS collection list.",
        ),
    ] = None
    """
    CMS collection-list rendering context for the event. Omitted when the event is not rendered inside a CMS collection list.
    """

    collection_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="collectionId"),
        pydantic.Field(
            alias="collectionId",
            description="Identifier of the CMS collection the associated page belongs to. Present only for events on CMS-templated pages.",
        ),
    ] = None
    """
    Identifier of the CMS collection the associated page belongs to. Present only for events on CMS-templated pages.
    """

    item_slug: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="itemSlug"),
        pydantic.Field(
            alias="itemSlug",
            description="Slug of the CMS item the associated page represents. Present only for events on CMS-templated pages.",
        ),
    ] = None
    """
    Slug of the CMS item the associated page represents. Present only for events on CMS-templated pages.
    """

    timeseries: typing.Optional[typing.List[TopEventsReportsResponseDataItemTimeseriesItem]] = pydantic.Field(
        default=None
    )
    """
    Daily count timeseries for this event over the requested window. Returned when `timeseries` is requested.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
