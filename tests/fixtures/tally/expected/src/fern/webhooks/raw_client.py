

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
from ..errors.unauthorized_error import UnauthorizedError
from ..types.event_type import EventType
from .types.create_webhook_request_http_headers_item import CreateWebhookRequestHttpHeadersItem
from .types.create_webhook_response import CreateWebhookResponse
from .types.list_webhook_events_response import ListWebhookEventsResponse
from .types.list_webhooks_response import ListWebhooksResponse
from .types.update_webhook_request_http_headers_item import UpdateWebhookRequestHttpHeadersItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_webhooks(
        self,
        *,
        page: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWebhooksResponse]:
        """
        Returns a paginated list of all webhooks across your accessible forms and workspaces.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        limit : typing.Optional[float]
            Number of webhooks per page (default: 25, max: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWebhooksResponse]
            List of webhooks
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks",
            method="GET",
            params={
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooksResponse,
                    parse_obj_as(
                        type_=ListWebhooksResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_webhook(
        self,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]] = OMIT,
        external_subscriber: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateWebhookResponse]:
        """
        Creates a new webhook for a form to receive form events.

        Parameters
        ----------
        form_id : str
            The ID of the form to create the webhook for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        external_subscriber : typing.Optional[str]
            Optional identifier for the external subscriber

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateWebhookResponse]
            Webhook created successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks",
            method="POST",
            json={
                "formId": form_id,
                "url": url,
                "signingSecret": signing_secret,
                "httpHeaders": convert_and_respect_annotation_metadata(
                    object_=http_headers,
                    annotation=typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]],
                    direction="write",
                ),
                "eventTypes": event_types,
                "externalSubscriber": external_subscriber,
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
                    CreateWebhookResponse,
                    parse_obj_as(
                        type_=CreateWebhookResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_webhook(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes a webhook. If this is the last webhook for a form, the webhooks integration will also be marked as deleted.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def update_webhook(
        self,
        webhook_id: str,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        is_enabled: bool,
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Updates an existing webhook configuration.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to update

        form_id : str
            The ID of the form the webhook is for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        is_enabled : bool
            Whether the webhook is enabled

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="PATCH",
            json={
                "formId": form_id,
                "url": url,
                "signingSecret": signing_secret,
                "httpHeaders": convert_and_respect_annotation_metadata(
                    object_=http_headers,
                    annotation=typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]],
                    direction="write",
                ),
                "eventTypes": event_types,
                "isEnabled": is_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def list_webhook_events(
        self,
        webhook_id: str,
        *,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListWebhookEventsResponse]:
        """
        Returns a paginated list of webhook delivery events for a specific webhook, including delivery status, response codes, and retry information.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        page : typing.Optional[float]
            Page number for pagination (default: 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListWebhookEventsResponse]
            List of webhook events
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/events",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhookEventsResponse,
                    parse_obj_as(
                        type_=ListWebhookEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    def retry_webhook_event(
        self, webhook_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Retries sending a failed webhook event. This will attempt to deliver the webhook payload again to the configured endpoint.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        event_id : str
            The ID of the webhook event to retry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/events/{encode_path_param(event_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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


class AsyncRawWebhooksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_webhooks(
        self,
        *,
        page: typing.Optional[float] = None,
        limit: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListWebhooksResponse]:
        """
        Returns a paginated list of all webhooks across your accessible forms and workspaces.

        Parameters
        ----------
        page : typing.Optional[float]
            Page number for pagination (default: 1)

        limit : typing.Optional[float]
            Number of webhooks per page (default: 25, max: 100)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWebhooksResponse]
            List of webhooks
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks",
            method="GET",
            params={
                "page": page,
                "limit": limit,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhooksResponse,
                    parse_obj_as(
                        type_=ListWebhooksResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_webhook(
        self,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]] = OMIT,
        external_subscriber: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateWebhookResponse]:
        """
        Creates a new webhook for a form to receive form events.

        Parameters
        ----------
        form_id : str
            The ID of the form to create the webhook for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        external_subscriber : typing.Optional[str]
            Optional identifier for the external subscriber

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateWebhookResponse]
            Webhook created successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks",
            method="POST",
            json={
                "formId": form_id,
                "url": url,
                "signingSecret": signing_secret,
                "httpHeaders": convert_and_respect_annotation_metadata(
                    object_=http_headers,
                    annotation=typing.Optional[typing.Sequence[CreateWebhookRequestHttpHeadersItem]],
                    direction="write",
                ),
                "eventTypes": event_types,
                "externalSubscriber": external_subscriber,
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
                    CreateWebhookResponse,
                    parse_obj_as(
                        type_=CreateWebhookResponse,
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_webhook(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes a webhook. If this is the last webhook for a form, the webhooks integration will also be marked as deleted.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def update_webhook(
        self,
        webhook_id: str,
        *,
        form_id: str,
        url: str,
        event_types: typing.Sequence[EventType],
        is_enabled: bool,
        signing_secret: typing.Optional[str] = OMIT,
        http_headers: typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Updates an existing webhook configuration.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook to update

        form_id : str
            The ID of the form the webhook is for

        url : str
            The URL to send webhook events to

        event_types : typing.Sequence[EventType]
            Types of events to receive

        is_enabled : bool
            Whether the webhook is enabled

        signing_secret : typing.Optional[str]
            Optional secret used to sign webhook payloads

        http_headers : typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]]
            Optional custom HTTP headers to include in webhook requests

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}",
            method="PATCH",
            json={
                "formId": form_id,
                "url": url,
                "signingSecret": signing_secret,
                "httpHeaders": convert_and_respect_annotation_metadata(
                    object_=http_headers,
                    annotation=typing.Optional[typing.Sequence[UpdateWebhookRequestHttpHeadersItem]],
                    direction="write",
                ),
                "eventTypes": event_types,
                "isEnabled": is_enabled,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
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
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def list_webhook_events(
        self,
        webhook_id: str,
        *,
        page: typing.Optional[float] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListWebhookEventsResponse]:
        """
        Returns a paginated list of webhook delivery events for a specific webhook, including delivery status, response codes, and retry information.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        page : typing.Optional[float]
            Page number for pagination (default: 1)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListWebhookEventsResponse]
            List of webhook events
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/events",
            method="GET",
            params={
                "page": page,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListWebhookEventsResponse,
                    parse_obj_as(
                        type_=ListWebhookEventsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
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

    async def retry_webhook_event(
        self, webhook_id: str, event_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Retries sending a failed webhook event. This will attempt to deliver the webhook payload again to the configured endpoint.

        Parameters
        ----------
        webhook_id : str
            The ID of the webhook

        event_id : str
            The ID of the webhook event to retry

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(webhook_id)}/events/{encode_path_param(event_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 401:
                raise UnauthorizedError(
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
