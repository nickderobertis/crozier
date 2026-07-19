

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .tags import Tags
from .uuid_ import Uuid
from .webhook_events_item import WebhookEventsItem


class Webhook(UniversalBaseModel):
    """
    Register to receive updates via webhook
    """

    url: str = pydantic.Field()
    """
    The URL to which the service instance should make HTTP POST requests with event data
    """

    api_key_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The HTTP header name that is added to the event POST
    """

    events: typing.List[WebhookEventsItem] = pydantic.Field()
    """
    List of event types to receive
    """

    flow_ids: typing.Optional[typing.List[Uuid]] = pydantic.Field(default=None)
    """
    Limit Flow and Flow Segment events to Flows in the given list of Flow IDs
    """

    source_ids: typing.Optional[typing.List[Uuid]] = pydantic.Field(default=None)
    """
    Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs
    """

    flow_collected_by_ids: typing.Optional[typing.List[Uuid]] = pydantic.Field(default=None)
    """
    Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs
    """

    source_collected_by_ids: typing.Optional[typing.List[Uuid]] = pydantic.Field(default=None)
    """
    Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs
    """

    accept_get_urls: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.
    """

    accept_storage_ids: typing.Optional[typing.List[Uuid]] = pydantic.Field(default=None)
    """
    List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.
    """

    presigned: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.
    """

    verbose_storage: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.
    """

    tags: typing.Optional[Tags] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
