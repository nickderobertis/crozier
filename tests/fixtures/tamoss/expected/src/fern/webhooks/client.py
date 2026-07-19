

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.tags import Tags
from ..types.url_tag_list import UrlTagList
from ..types.uuid_ import Uuid
from ..types.webhook_events_item import WebhookEventsItem
from ..types.webhook_get import WebhookGet
from .raw_client import AsyncRawWebhooksClient, RawWebhooksClient
from .types.webhook_post_status import WebhookPostStatus
from .types.webhook_put_status import WebhookPutStatus


OMIT = typing.cast(typing.Any, ...)


class WebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawWebhooksClient
        """
        return self._raw_client

    def get_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebhookGet]:
        """
        Get the list of registered webhook URLs.
        Service implementations SHOULD take steps to avoid displaying URLs to users other than those who have suitable permissions (e.g. the owning user).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [/service](#/operations/GET_service) endpoint.

        Parameters
        ----------
        tag_name : typing.Optional[UrlTagList]
            Filter on webhooks that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on webhooks that have a tag named {name} regardless of value.
            The {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebhookGet]
            Return the list of known webhook URLs.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.get_webhooks()
        """
        _response = self._raw_client.get_webhooks(
            tag_name=tag_name, tag_exists_name=tag_exists_name, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    def post_webhooks(
        self,
        *,
        url: str,
        events: typing.Sequence[WebhookEventsItem],
        api_key_value: typing.Optional[str] = OMIT,
        status: typing.Optional[WebhookPostStatus] = OMIT,
        api_key_name: typing.Optional[str] = OMIT,
        flow_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        flow_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        accept_get_urls: typing.Optional[typing.Sequence[str]] = OMIT,
        accept_storage_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        presigned: typing.Optional[bool] = OMIT,
        verbose_storage: typing.Optional[bool] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookGet:
        """
        Register to receive event notifications as webhooks on a specified URL. Webhook messages will conform to the
        format in the `webhooks` section of the API docs, depending on the event type (as defined in the same section).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms`
        list on the service endpoint.

        HTTP requests from the service SHOULD include a `api_key_name` header with the 'api_key_value' value. Clients SHOULD verify this against the value they provided when registering the webhook.

        API implementations MAY partially support event filtering and transformations.
        API implementations SHALL return a 400 response code if the filtering or transformation specified in the request is not supported.

        API implementations SHOULD consider the security implementations of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar. API implementations SHOULD take appropriate steps to authorize the modification of existing webhooks. This may take the form of RBAC, or ABAC.

        Parameters
        ----------
        url : str
            The URL to which the service instance should make HTTP POST requests with event data

        events : typing.Sequence[WebhookEventsItem]
            List of event types to receive

        api_key_value : typing.Optional[str]
            The value that the HTTP header 'api_key_name' will be set to

        status : typing.Optional[WebhookPostStatus]
            Status of the Webhook. `created` will register the webhook in the created state and the service instance will attempt to start sending events. `disabled` will register the webhook in a disabled state and will not send events. Assumed to be `created` if not set.

        api_key_name : typing.Optional[str]
            The HTTP header name that is added to the event POST

        flow_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to Flows in the given list of Flow IDs

        source_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs

        flow_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs

        source_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs

        accept_get_urls : typing.Optional[typing.Sequence[str]]
            List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.

        accept_storage_ids : typing.Optional[typing.Sequence[Uuid]]
            List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.

        presigned : typing.Optional[bool]
            Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        verbose_storage : typing.Optional[bool]
            Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        tags : typing.Optional[Tags]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGet
            Success. The webhook has been registered.

        Examples
        --------
        from fern import FernApi, WebhookEventsItem

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.post_webhooks(
            url="url",
            events=[WebhookEventsItem.FLOWS_CREATED],
        )
        """
        _response = self._raw_client.post_webhooks(
            url=url,
            events=events,
            api_key_value=api_key_value,
            status=status,
            api_key_name=api_key_name,
            flow_ids=flow_ids,
            source_ids=source_ids,
            flow_collected_by_ids=flow_collected_by_ids,
            source_collected_by_ids=source_collected_by_ids,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            verbose_storage=verbose_storage,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def head_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return webhooks path headers

        Parameters
        ----------
        tag_name : typing.Optional[UrlTagList]
            Filter on webhooks that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on webhooks that have a tag named {name} regardless of value.
            The {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.head_webhooks()
        """
        _response = self._raw_client.head_webhooks(
            tag_name=tag_name, tag_exists_name=tag_exists_name, page=page, limit=limit, request_options=request_options
        )
        return _response.headers

    def get_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookGet:
        """
        Get the details of a webhook. Service implementations SHOULD take steps to avoid displaying URLs to users other than those who have suitable permissions (e.g. the owning user).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [`/service`](#/operations/GET_service) endpoint.

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGet
            Return the webhook details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.get_webhooks_webhook_id(
            webhook_id="webhookId",
        )
        """
        _response = self._raw_client.get_webhooks_webhook_id(webhook_id, request_options=request_options)
        return _response.data

    def put_webhooks(
        self,
        webhook_id: Uuid,
        *,
        status: WebhookPutStatus,
        id: Uuid,
        url: str,
        events: typing.Sequence[WebhookEventsItem],
        api_key_value: typing.Optional[str] = OMIT,
        api_key_name: typing.Optional[str] = OMIT,
        flow_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        flow_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        accept_get_urls: typing.Optional[typing.Sequence[str]] = OMIT,
        accept_storage_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        presigned: typing.Optional[bool] = OMIT,
        verbose_storage: typing.Optional[bool] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookGet:
        """
        Update the configuration of an existing webhook.

        Webhook messages will conform to the format in the `webhooks` section of the API docs, depending on the event type (as defined in the same section).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [`/service`](#/operations/GET_service) endpoint.

        HTTP events sent by the service to a client webhook's endpoint SHOULD include a `api_key_name` header with the 'api_key_value' value.
        Clients SHOULD verify this against the value they provided when registering the webhook.

        Service implementations MAY partially support event filtering and transformations.
        Service implementations SHALL return a 400 response code if the filtering or transformation specified in the request is not supported.

        Service implementations SHOULD consider the security implications of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar.
        Service implementations SHOULD take appropriate steps to authorize the modification of existing webhooks.
        This may take the form of RBAC, or ABAC.

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        status : WebhookPutStatus
            Status of the Webhook. `created` indicates the webhook has been successfully registered but is yet to begin sending events or, depending on the service implementation, the worker responsible for sending the events has yet to start. `started` indicates the webhook is active and sending events. `disabled` indicates the webhook has been disabled by a client and is not currently sending events. `error` indicates an error condition has been encountered and the webhook has been disabled by the service instance. More information about the error condition will be indicated by the service instance in the `error` parameter. Service implementations SHOULD implement appropriate retries and only enter the `error` state when absolutely necesary. A webhook in the `error` or `disabled` state may be re-enabled by a client by setting the status to `created`. A webhook in the `created` or `started` state may be disabled by a client by setting the status to `disabled`. Attempting to transition an `error` status to `disabled` SHOULD be rejected.

        id : Uuid
            Webhook identifier

        url : str
            The URL to which the service instance should make HTTP POST requests with event data

        events : typing.Sequence[WebhookEventsItem]
            List of event types to receive

        api_key_value : typing.Optional[str]
            The value that the HTTP header 'api_key_name' will be set to

        api_key_name : typing.Optional[str]
            The HTTP header name that is added to the event POST

        flow_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to Flows in the given list of Flow IDs

        source_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs

        flow_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs

        source_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs

        accept_get_urls : typing.Optional[typing.Sequence[str]]
            List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.

        accept_storage_ids : typing.Optional[typing.Sequence[Uuid]]
            List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.

        presigned : typing.Optional[bool]
            Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        verbose_storage : typing.Optional[bool]
            Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        tags : typing.Optional[Tags]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGet
            Success. The webhook has been updated

        Examples
        --------
        from fern.webhooks import WebhookPutStatus

        from fern import FernApi, WebhookEventsItem

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.put_webhooks(
            webhook_id="webhookId",
            url="url",
            events=[WebhookEventsItem.FLOWS_CREATED],
            id="id",
            status=WebhookPutStatus.CREATED,
        )
        """
        _response = self._raw_client.put_webhooks(
            webhook_id,
            status=status,
            id=id,
            url=url,
            events=events,
            api_key_value=api_key_value,
            api_key_name=api_key_name,
            flow_ids=flow_ids,
            source_ids=source_ids,
            flow_collected_by_ids=flow_collected_by_ids,
            source_collected_by_ids=source_collected_by_ids,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            verbose_storage=verbose_storage,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    def delete_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the webhook.
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the service endpoint.

        Service implementations SHOULD consider the security implementations of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar.
        Service implementations SHOULD take appropriate steps to authorize the deleting of webhooks.
        This may take the form of RBAC, or ABAC.

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.delete_webhooks_webhook_id(
            webhook_id="webhookId",
        )
        """
        _response = self._raw_client.delete_webhooks_webhook_id(webhook_id, request_options=request_options)
        return _response.data

    def head_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return webhook path headers

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        from fern import FernApi

        client = FernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )
        client.webhooks.head_webhooks_webhook_id(
            webhook_id="webhookId",
        )
        """
        _response = self._raw_client.head_webhooks_webhook_id(webhook_id, request_options=request_options)
        return _response.headers


class AsyncWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawWebhooksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawWebhooksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawWebhooksClient
        """
        return self._raw_client

    async def get_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[WebhookGet]:
        """
        Get the list of registered webhook URLs.
        Service implementations SHOULD take steps to avoid displaying URLs to users other than those who have suitable permissions (e.g. the owning user).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [/service](#/operations/GET_service) endpoint.

        Parameters
        ----------
        tag_name : typing.Optional[UrlTagList]
            Filter on webhooks that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on webhooks that have a tag named {name} regardless of value.
            The {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[WebhookGet]
            Return the list of known webhook URLs.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.get_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks(
            tag_name=tag_name, tag_exists_name=tag_exists_name, page=page, limit=limit, request_options=request_options
        )
        return _response.data

    async def post_webhooks(
        self,
        *,
        url: str,
        events: typing.Sequence[WebhookEventsItem],
        api_key_value: typing.Optional[str] = OMIT,
        status: typing.Optional[WebhookPostStatus] = OMIT,
        api_key_name: typing.Optional[str] = OMIT,
        flow_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        flow_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        accept_get_urls: typing.Optional[typing.Sequence[str]] = OMIT,
        accept_storage_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        presigned: typing.Optional[bool] = OMIT,
        verbose_storage: typing.Optional[bool] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookGet:
        """
        Register to receive event notifications as webhooks on a specified URL. Webhook messages will conform to the
        format in the `webhooks` section of the API docs, depending on the event type (as defined in the same section).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms`
        list on the service endpoint.

        HTTP requests from the service SHOULD include a `api_key_name` header with the 'api_key_value' value. Clients SHOULD verify this against the value they provided when registering the webhook.

        API implementations MAY partially support event filtering and transformations.
        API implementations SHALL return a 400 response code if the filtering or transformation specified in the request is not supported.

        API implementations SHOULD consider the security implementations of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar. API implementations SHOULD take appropriate steps to authorize the modification of existing webhooks. This may take the form of RBAC, or ABAC.

        Parameters
        ----------
        url : str
            The URL to which the service instance should make HTTP POST requests with event data

        events : typing.Sequence[WebhookEventsItem]
            List of event types to receive

        api_key_value : typing.Optional[str]
            The value that the HTTP header 'api_key_name' will be set to

        status : typing.Optional[WebhookPostStatus]
            Status of the Webhook. `created` will register the webhook in the created state and the service instance will attempt to start sending events. `disabled` will register the webhook in a disabled state and will not send events. Assumed to be `created` if not set.

        api_key_name : typing.Optional[str]
            The HTTP header name that is added to the event POST

        flow_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to Flows in the given list of Flow IDs

        source_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs

        flow_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs

        source_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs

        accept_get_urls : typing.Optional[typing.Sequence[str]]
            List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.

        accept_storage_ids : typing.Optional[typing.Sequence[Uuid]]
            List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.

        presigned : typing.Optional[bool]
            Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        verbose_storage : typing.Optional[bool]
            Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        tags : typing.Optional[Tags]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGet
            Success. The webhook has been registered.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, WebhookEventsItem

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.post_webhooks(
                url="url",
                events=[WebhookEventsItem.FLOWS_CREATED],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.post_webhooks(
            url=url,
            events=events,
            api_key_value=api_key_value,
            status=status,
            api_key_name=api_key_name,
            flow_ids=flow_ids,
            source_ids=source_ids,
            flow_collected_by_ids=flow_collected_by_ids,
            source_collected_by_ids=source_collected_by_ids,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            verbose_storage=verbose_storage,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def head_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, str]:
        """
        Return webhooks path headers

        Parameters
        ----------
        tag_name : typing.Optional[UrlTagList]
            Filter on webhooks that have a tag named {name} with a value in the given comma-separated list of values.
            The {name} and the value MUST be URL encoded where special characters are present.
            Where the tag's value is a string, at least one of the given values will match.
            Where the tag's value is an array, at least one value in the array will match at least one of the given values.
            Partial string matches of the values are not valid.

        tag_exists_name : typing.Optional[bool]
            Filter on webhooks that have a tag named {name} regardless of value.
            The {name} MUST be URL encoded where special characters are present.
            If set to true then the presence of the tag is filtered for.
            If set to false then its absence is.
            If left out then no filtering on tag presence is performed.

        page : typing.Optional[str]
            Opaque string used by backend to access a specific page of results. Clients should read the next URL from the `Link` header returned with responses, or use value of the returned X-Paging-NextKey header. If not supplied, the first page is accessed. Service implementations should ensure a consistent sort order is applied to pages of results.

        limit : typing.Optional[int]
            Restrict the response to the specified number of results. Service implementations may specify their own default and maximum for the limit

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.head_webhooks()


        asyncio.run(main())
        """
        _response = await self._raw_client.head_webhooks(
            tag_name=tag_name, tag_exists_name=tag_exists_name, page=page, limit=limit, request_options=request_options
        )
        return _response.headers

    async def get_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> WebhookGet:
        """
        Get the details of a webhook. Service implementations SHOULD take steps to avoid displaying URLs to users other than those who have suitable permissions (e.g. the owning user).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [`/service`](#/operations/GET_service) endpoint.

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGet
            Return the webhook details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.get_webhooks_webhook_id(
                webhook_id="webhookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_webhooks_webhook_id(webhook_id, request_options=request_options)
        return _response.data

    async def put_webhooks(
        self,
        webhook_id: Uuid,
        *,
        status: WebhookPutStatus,
        id: Uuid,
        url: str,
        events: typing.Sequence[WebhookEventsItem],
        api_key_value: typing.Optional[str] = OMIT,
        api_key_name: typing.Optional[str] = OMIT,
        flow_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        flow_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        source_collected_by_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        accept_get_urls: typing.Optional[typing.Sequence[str]] = OMIT,
        accept_storage_ids: typing.Optional[typing.Sequence[Uuid]] = OMIT,
        presigned: typing.Optional[bool] = OMIT,
        verbose_storage: typing.Optional[bool] = OMIT,
        tags: typing.Optional[Tags] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> WebhookGet:
        """
        Update the configuration of an existing webhook.

        Webhook messages will conform to the format in the `webhooks` section of the API docs, depending on the event type (as defined in the same section).
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the [`/service`](#/operations/GET_service) endpoint.

        HTTP events sent by the service to a client webhook's endpoint SHOULD include a `api_key_name` header with the 'api_key_value' value.
        Clients SHOULD verify this against the value they provided when registering the webhook.

        Service implementations MAY partially support event filtering and transformations.
        Service implementations SHALL return a 400 response code if the filtering or transformation specified in the request is not supported.

        Service implementations SHOULD consider the security implications of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar.
        Service implementations SHOULD take appropriate steps to authorize the modification of existing webhooks.
        This may take the form of RBAC, or ABAC.

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        status : WebhookPutStatus
            Status of the Webhook. `created` indicates the webhook has been successfully registered but is yet to begin sending events or, depending on the service implementation, the worker responsible for sending the events has yet to start. `started` indicates the webhook is active and sending events. `disabled` indicates the webhook has been disabled by a client and is not currently sending events. `error` indicates an error condition has been encountered and the webhook has been disabled by the service instance. More information about the error condition will be indicated by the service instance in the `error` parameter. Service implementations SHOULD implement appropriate retries and only enter the `error` state when absolutely necesary. A webhook in the `error` or `disabled` state may be re-enabled by a client by setting the status to `created`. A webhook in the `created` or `started` state may be disabled by a client by setting the status to `disabled`. Attempting to transition an `error` status to `disabled` SHOULD be rejected.

        id : Uuid
            Webhook identifier

        url : str
            The URL to which the service instance should make HTTP POST requests with event data

        events : typing.Sequence[WebhookEventsItem]
            List of event types to receive

        api_key_value : typing.Optional[str]
            The value that the HTTP header 'api_key_name' will be set to

        api_key_name : typing.Optional[str]
            The HTTP header name that is added to the event POST

        flow_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to Flows in the given list of Flow IDs

        source_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to Sources in the given list of Source IDs

        flow_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow and Flow Segment events to those with Flow that is collected by a Flow Collection in the given list of Flow Collection IDs

        source_collected_by_ids : typing.Optional[typing.Sequence[Uuid]]
            Limit Flow, Flow Segment and Source events to those with Source that is collected by a Source Collection in the given list of Source Collection IDs

        accept_get_urls : typing.Optional[typing.Sequence[str]]
            List of labels of URLs to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_get_urls` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the labels are represented using a JSON array rather than a (comma separated list) string.

        accept_storage_ids : typing.Optional[typing.Sequence[Uuid]]
            List of labels of `storage_id`s to include in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `accept_storage_ids` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint, except that the IDs are represented using a JSON array rather than a (comma separated list) string.

        presigned : typing.Optional[bool]
            Whether to include presigned/non-presigned URLs in the `get_urls` property in `flows/segments_added` events. Where multiple `get_urls` filter query parameters are provided, the included `get_urls` will match all filters. This option is the same as the `presigned` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        verbose_storage : typing.Optional[bool]
            Whether to include storage metadata in the `get_urls` property in `flows/segments_added` events. This option is the same as the `verbose_storage` query parameter for the [/flows/{flowId}/segments](#/operations/GET_flows-flowId-segments) API endpoint.

        tags : typing.Optional[Tags]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        WebhookGet
            Success. The webhook has been updated

        Examples
        --------
        import asyncio

        from fern.webhooks import WebhookPutStatus

        from fern import AsyncFernApi, WebhookEventsItem

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.put_webhooks(
                webhook_id="webhookId",
                url="url",
                events=[WebhookEventsItem.FLOWS_CREATED],
                id="id",
                status=WebhookPutStatus.CREATED,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.put_webhooks(
            webhook_id,
            status=status,
            id=id,
            url=url,
            events=events,
            api_key_value=api_key_value,
            api_key_name=api_key_name,
            flow_ids=flow_ids,
            source_ids=source_ids,
            flow_collected_by_ids=flow_collected_by_ids,
            source_collected_by_ids=source_collected_by_ids,
            accept_get_urls=accept_get_urls,
            accept_storage_ids=accept_storage_ids,
            presigned=presigned,
            verbose_storage=verbose_storage,
            tags=tags,
            request_options=request_options,
        )
        return _response.data

    async def delete_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> None:
        """
        Deletes the webhook.
        Availability of this endpoint is indicated by the name "webhooks" appearing in the `event_stream_mechanisms` list on the service endpoint.

        Service implementations SHOULD consider the security implementations of providing webhooks, and include appropriate mitigations against Server Side Request Forgery (SSRF) attacks and similar.
        Service implementations SHOULD take appropriate steps to authorize the deleting of webhooks.
        This may take the form of RBAC, or ABAC.

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.delete_webhooks_webhook_id(
                webhook_id="webhookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_webhooks_webhook_id(webhook_id, request_options=request_options)
        return _response.data

    async def head_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Dict[str, str]:
        """
        Return webhook path headers

        Parameters
        ----------
        webhook_id : Uuid
            The Webhook identifier.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, str]


        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            username="YOUR_USERNAME",
            password="YOUR_PASSWORD",
        )


        async def main() -> None:
            await client.webhooks.head_webhooks_webhook_id(
                webhook_id="webhookId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.head_webhooks_webhook_id(webhook_id, request_options=request_options)
        return _response.headers
