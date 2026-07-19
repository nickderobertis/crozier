

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..types.tags import Tags
from ..types.url_tag_list import UrlTagList
from ..types.uuid_ import Uuid
from ..types.webhook_events_item import WebhookEventsItem
from ..types.webhook_get import WebhookGet
from .types.webhook_post_status import WebhookPostStatus
from .types.webhook_put_status import WebhookPutStatus
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[WebhookGet]]:
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
        HttpResponse[typing.List[WebhookGet]]
            Return the list of known webhook URLs.
        """
        _response = self._client_wrapper.httpx_client.request(
            "service/webhooks",
            method="GET",
            params={
                "tag.{name}": tag_name,
                "tag_exists.{name}": tag_exists_name,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebhookGet],
                    parse_obj_as(
                        type_=typing.List[WebhookGet],
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[WebhookGet]:
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
        HttpResponse[WebhookGet]
            Success. The webhook has been registered.
        """
        _response = self._client_wrapper.httpx_client.request(
            "service/webhooks",
            method="POST",
            json={
                "api_key_value": api_key_value,
                "status": status,
                "url": url,
                "api_key_name": api_key_name,
                "events": events,
                "flow_ids": flow_ids,
                "source_ids": source_ids,
                "flow_collected_by_ids": flow_collected_by_ids,
                "source_collected_by_ids": source_collected_by_ids,
                "accept_get_urls": accept_get_urls,
                "accept_storage_ids": accept_storage_ids,
                "presigned": presigned,
                "verbose_storage": verbose_storage,
                "tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tags, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGet,
                    parse_obj_as(
                        type_=WebhookGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def head_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[str]:
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
        HttpResponse[str]

        """
        _response = self._client_wrapper.httpx_client.request(
            "service/webhooks",
            method="HEAD",
            params={
                "tag.{name}": tag_name,
                "tag_exists.{name}": tag_exists_name,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def get_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookGet]:
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
        HttpResponse[WebhookGet]
            Return the webhook details.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGet,
                    parse_obj_as(
                        type_=WebhookGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[WebhookGet]:
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
        HttpResponse[WebhookGet]
            Success. The webhook has been updated
        """
        _response = self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="PUT",
            json={
                "api_key_value": api_key_value,
                "status": status,
                "id": id,
                "url": url,
                "api_key_name": api_key_name,
                "events": events,
                "flow_ids": flow_ids,
                "source_ids": source_ids,
                "flow_collected_by_ids": flow_collected_by_ids,
                "source_collected_by_ids": source_collected_by_ids,
                "accept_get_urls": accept_get_urls,
                "accept_storage_ids": accept_storage_ids,
                "presigned": presigned,
                "verbose_storage": verbose_storage,
                "tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tags, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGet,
                    parse_obj_as(
                        type_=WebhookGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
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
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def head_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
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
        HttpResponse[str]

        """
        _response = self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[WebhookGet]]:
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
        AsyncHttpResponse[typing.List[WebhookGet]]
            Return the list of known webhook URLs.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "service/webhooks",
            method="GET",
            params={
                "tag.{name}": tag_name,
                "tag_exists.{name}": tag_exists_name,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[WebhookGet],
                    parse_obj_as(
                        type_=typing.List[WebhookGet],
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[WebhookGet]:
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
        AsyncHttpResponse[WebhookGet]
            Success. The webhook has been registered.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "service/webhooks",
            method="POST",
            json={
                "api_key_value": api_key_value,
                "status": status,
                "url": url,
                "api_key_name": api_key_name,
                "events": events,
                "flow_ids": flow_ids,
                "source_ids": source_ids,
                "flow_collected_by_ids": flow_collected_by_ids,
                "source_collected_by_ids": source_collected_by_ids,
                "accept_get_urls": accept_get_urls,
                "accept_storage_ids": accept_storage_ids,
                "presigned": presigned,
                "verbose_storage": verbose_storage,
                "tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tags, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGet,
                    parse_obj_as(
                        type_=WebhookGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def head_webhooks(
        self,
        *,
        tag_name: typing.Optional[UrlTagList] = None,
        tag_exists_name: typing.Optional[bool] = None,
        page: typing.Optional[str] = None,
        limit: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "service/webhooks",
            method="HEAD",
            params={
                "tag.{name}": tag_name,
                "tag_exists.{name}": tag_exists_name,
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def get_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookGet]:
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
        AsyncHttpResponse[WebhookGet]
            Return the webhook details.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGet,
                    parse_obj_as(
                        type_=WebhookGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[WebhookGet]:
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
        AsyncHttpResponse[WebhookGet]
            Success. The webhook has been updated
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="PUT",
            json={
                "api_key_value": api_key_value,
                "status": status,
                "id": id,
                "url": url,
                "api_key_name": api_key_name,
                "events": events,
                "flow_ids": flow_ids,
                "source_ids": source_ids,
                "flow_collected_by_ids": flow_collected_by_ids,
                "source_collected_by_ids": source_collected_by_ids,
                "accept_get_urls": accept_get_urls,
                "accept_storage_ids": accept_storage_ids,
                "presigned": presigned,
                "verbose_storage": verbose_storage,
                "tags": convert_and_respect_annotation_metadata(object_=tags, annotation=Tags, direction="write"),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGet,
                    parse_obj_as(
                        type_=WebhookGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
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
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def head_webhooks_webhook_id(
        self, webhook_id: Uuid, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
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
        AsyncHttpResponse[str]

        """
        _response = await self._client_wrapper.httpx_client.request(
            f"service/webhooks/{encode_path_param(webhook_id)}",
            method="HEAD",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    str,
                    parse_obj_as(
                        type_=str,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
