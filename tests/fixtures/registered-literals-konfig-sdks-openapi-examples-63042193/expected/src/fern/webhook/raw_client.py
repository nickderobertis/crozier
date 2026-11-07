

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
from ..types.webhook_create_outbound_webhook_response import WebhookCreateOutboundWebhookResponse
from ..types.webhook_delete_outbound_webhook_response import WebhookDeleteOutboundWebhookResponse
from ..types.webhook_get_by_id_response import WebhookGetByIdResponse
from ..types.webhook_list_matching_scope_response import WebhookListMatchingScopeResponse
from ..types.webhook_update_outbound_webhook_response import WebhookUpdateOutboundWebhookResponse
from .types.webhook_create_outbound_webhook_request_events_item import WebhookCreateOutboundWebhookRequestEventsItem
from .types.webhook_create_outbound_webhook_request_scope import WebhookCreateOutboundWebhookRequestScope
from .types.webhook_list_matching_scope_request_scope_type import WebhookListMatchingScopeRequestScopeType
from .types.webhook_update_outbound_webhook_request_events_item import WebhookUpdateOutboundWebhookRequestEventsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhookClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listmatchingscope(
        self,
        *,
        scope_id: str,
        scope_type: WebhookListMatchingScopeRequestScopeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhookListMatchingScopeResponse]:
        """
        Get a list of outbound webhooks that match the given scope-type and scope-id

        Parameters
        ----------
        scope_id : str
            ID of the scope being used (at the moment, only project ID is supported)

        scope_type : WebhookListMatchingScopeRequestScopeType
            Type of the scope being used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookListMatchingScopeResponse]
            A list of webhooks
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhook",
            method="GET",
            params={
                "scope-id": scope_id,
                "scope-type": scope_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookListMatchingScopeResponse,
                    parse_obj_as(
                        type_=WebhookListMatchingScopeResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def createoutboundwebhook(
        self,
        *,
        name: str,
        events: typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem],
        url: str,
        verify_tls: bool,
        signing_secret: str,
        scope: WebhookCreateOutboundWebhookRequestScope,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhookCreateOutboundWebhookResponse]:
        """
        Creates an outbound webhook.

        Parameters
        ----------
        name : str
            Name of the webhook

        events : typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem]
            Events that will trigger the webhook

        url : str
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        verify_tls : bool
            Whether to enforce TLS certificate verification when delivering the webhook

        signing_secret : str
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        scope : WebhookCreateOutboundWebhookRequestScope
            The scope in which the relevant events that will trigger webhooks

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookCreateOutboundWebhookResponse]
            A webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhook",
            method="POST",
            json={
                "name": name,
                "events": events,
                "url": url,
                "verify-tls": verify_tls,
                "signing-secret": signing_secret,
                "scope": convert_and_respect_annotation_metadata(
                    object_=scope, annotation=WebhookCreateOutboundWebhookRequestScope, direction="write"
                ),
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
                    WebhookCreateOutboundWebhookResponse,
                    parse_obj_as(
                        type_=WebhookCreateOutboundWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def getbyid(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookGetByIdResponse]:
        """
        Get an outbound webhook by id.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookGetByIdResponse]
            A webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGetByIdResponse,
                    parse_obj_as(
                        type_=WebhookGetByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def updateoutboundwebhook(
        self,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        events: typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]] = OMIT,
        url: typing.Optional[str] = OMIT,
        signing_secret: typing.Optional[str] = OMIT,
        verify_tls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhookUpdateOutboundWebhookResponse]:
        """
        Updates an outbound webhook.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        name : typing.Optional[str]
            Name of the webhook

        events : typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]]
            Events that will trigger the webhook

        url : typing.Optional[str]
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        signing_secret : typing.Optional[str]
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        verify_tls : typing.Optional[bool]
            Whether to enforce TLS certificate verification when delivering the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookUpdateOutboundWebhookResponse]
            A webhook
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="PUT",
            json={
                "name": name,
                "events": events,
                "url": url,
                "signing-secret": signing_secret,
                "verify-tls": verify_tls,
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
                    WebhookUpdateOutboundWebhookResponse,
                    parse_obj_as(
                        type_=WebhookUpdateOutboundWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def deleteoutboundwebhook(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookDeleteOutboundWebhookResponse]:
        """
        Deletes an outbound webhook

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookDeleteOutboundWebhookResponse]
            A confirmation message
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookDeleteOutboundWebhookResponse,
                    parse_obj_as(
                        type_=WebhookDeleteOutboundWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawWebhookClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def listmatchingscope(
        self,
        *,
        scope_id: str,
        scope_type: WebhookListMatchingScopeRequestScopeType,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhookListMatchingScopeResponse]:
        """
        Get a list of outbound webhooks that match the given scope-type and scope-id

        Parameters
        ----------
        scope_id : str
            ID of the scope being used (at the moment, only project ID is supported)

        scope_type : WebhookListMatchingScopeRequestScopeType
            Type of the scope being used

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookListMatchingScopeResponse]
            A list of webhooks
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhook",
            method="GET",
            params={
                "scope-id": scope_id,
                "scope-type": scope_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookListMatchingScopeResponse,
                    parse_obj_as(
                        type_=WebhookListMatchingScopeResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def createoutboundwebhook(
        self,
        *,
        name: str,
        events: typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem],
        url: str,
        verify_tls: bool,
        signing_secret: str,
        scope: WebhookCreateOutboundWebhookRequestScope,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhookCreateOutboundWebhookResponse]:
        """
        Creates an outbound webhook.

        Parameters
        ----------
        name : str
            Name of the webhook

        events : typing.Sequence[WebhookCreateOutboundWebhookRequestEventsItem]
            Events that will trigger the webhook

        url : str
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        verify_tls : bool
            Whether to enforce TLS certificate verification when delivering the webhook

        signing_secret : str
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        scope : WebhookCreateOutboundWebhookRequestScope
            The scope in which the relevant events that will trigger webhooks

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookCreateOutboundWebhookResponse]
            A webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhook",
            method="POST",
            json={
                "name": name,
                "events": events,
                "url": url,
                "verify-tls": verify_tls,
                "signing-secret": signing_secret,
                "scope": convert_and_respect_annotation_metadata(
                    object_=scope, annotation=WebhookCreateOutboundWebhookRequestScope, direction="write"
                ),
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
                    WebhookCreateOutboundWebhookResponse,
                    parse_obj_as(
                        type_=WebhookCreateOutboundWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def getbyid(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookGetByIdResponse]:
        """
        Get an outbound webhook by id.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookGetByIdResponse]
            A webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookGetByIdResponse,
                    parse_obj_as(
                        type_=WebhookGetByIdResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def updateoutboundwebhook(
        self,
        webhook_id: str,
        *,
        name: typing.Optional[str] = OMIT,
        events: typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]] = OMIT,
        url: typing.Optional[str] = OMIT,
        signing_secret: typing.Optional[str] = OMIT,
        verify_tls: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhookUpdateOutboundWebhookResponse]:
        """
        Updates an outbound webhook.

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        name : typing.Optional[str]
            Name of the webhook

        events : typing.Optional[typing.Sequence[WebhookUpdateOutboundWebhookRequestEventsItem]]
            Events that will trigger the webhook

        url : typing.Optional[str]
            URL to deliver the webhook to. Note: protocol must be included as well (only https is supported)

        signing_secret : typing.Optional[str]
            Secret used to build an HMAC hash of the payload and passed as a header in the webhook request

        verify_tls : typing.Optional[bool]
            Whether to enforce TLS certificate verification when delivering the webhook

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookUpdateOutboundWebhookResponse]
            A webhook
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="PUT",
            json={
                "name": name,
                "events": events,
                "url": url,
                "signing-secret": signing_secret,
                "verify-tls": verify_tls,
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
                    WebhookUpdateOutboundWebhookResponse,
                    parse_obj_as(
                        type_=WebhookUpdateOutboundWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def deleteoutboundwebhook(
        self, webhook_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookDeleteOutboundWebhookResponse]:
        """
        Deletes an outbound webhook

        Parameters
        ----------
        webhook_id : str
            ID of the webhook (UUID)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookDeleteOutboundWebhookResponse]
            A confirmation message
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookDeleteOutboundWebhookResponse,
                    parse_obj_as(
                        type_=WebhookDeleteOutboundWebhookResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
