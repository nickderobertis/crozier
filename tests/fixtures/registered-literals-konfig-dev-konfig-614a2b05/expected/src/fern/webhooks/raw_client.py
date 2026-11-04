

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.webhook_event_type_value import WebhookEventTypeValue
from .types.create_a_webhook_response import CreateAWebhookResponse
from .types.delete_a_webhook_response import DeleteAWebhookResponse
from .types.list_all_webhooks_response import ListAllWebhooksResponse
from .types.retrieve_a_webhook_response import RetrieveAWebhookResponse
from .types.update_a_webhook_response import UpdateAWebhookResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[ListAllWebhooksResponse]:
        """
        View all webhooks associated with a specific company with filtering available via query parameters

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListAllWebhooksResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAllWebhooksResponse,
                    parse_obj_as(
                        type_=ListAllWebhooksResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_a_webhook(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateAWebhookResponse]:
        """
        Creates a webhook for the specified events. Send separate requests if you need to create webhooks for multiple target URLs. Each target URL may only have one active registration.

        Parameters
        ----------
        events : typing.Sequence[WebhookEventTypeValue]
            The event type(s) to trigger the webhook. Note: you can use `*` to receive events for all events, although we don't recommend this path, especially for environments with higher volume.

        target_url : str
            The URL to send the webhook event payload to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateAWebhookResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks",
            method="POST",
            json={
                "events": events,
                "targetURL": target_url,
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
                    CreateAWebhookResponse,
                    parse_obj_as(
                        type_=CreateAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[RetrieveAWebhookResponse]:
        """
        View the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[RetrieveAWebhookResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveAWebhookResponse,
                    parse_obj_as(
                        type_=RetrieveAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteAWebhookResponse]:
        """
        Delete a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteAWebhookResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAWebhookResponse,
                    parse_obj_as(
                        type_=DeleteAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def update_a_webhook(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UpdateAWebhookResponse]:
        """
        Update the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        events : typing.Optional[typing.Sequence[str]]
            The type of events that will trigger a notification to the target URL.

        target_url : typing.Optional[str]
            The URL of where the notification gets sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateAWebhookResponse]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(id)}",
            method="PATCH",
            json={
                "events": events,
                "targetURL": target_url,
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
                    UpdateAWebhookResponse,
                    parse_obj_as(
                        type_=UpdateAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def retrieve_webhook_verification_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[str]:
        """
        View the verification key for webhook security implementations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[str]
            200
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhooks/verification-key",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=_response.text)
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

    async def list_all_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[ListAllWebhooksResponse]:
        """
        View all webhooks associated with a specific company with filtering available via query parameters

        Parameters
        ----------
        page : typing.Optional[int]
            The page number used when paginating through a list of results.

        page_size : typing.Optional[int]
            A limit of the number of results to return.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListAllWebhooksResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks",
            method="GET",
            params={
                "page": page,
                "pageSize": page_size,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListAllWebhooksResponse,
                    parse_obj_as(
                        type_=ListAllWebhooksResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_a_webhook(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateAWebhookResponse]:
        """
        Creates a webhook for the specified events. Send separate requests if you need to create webhooks for multiple target URLs. Each target URL may only have one active registration.

        Parameters
        ----------
        events : typing.Sequence[WebhookEventTypeValue]
            The event type(s) to trigger the webhook. Note: you can use `*` to receive events for all events, although we don't recommend this path, especially for environments with higher volume.

        target_url : str
            The URL to send the webhook event payload to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateAWebhookResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks",
            method="POST",
            json={
                "events": events,
                "targetURL": target_url,
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
                    CreateAWebhookResponse,
                    parse_obj_as(
                        type_=CreateAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[RetrieveAWebhookResponse]:
        """
        View the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[RetrieveAWebhookResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    RetrieveAWebhookResponse,
                    parse_obj_as(
                        type_=RetrieveAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_a_webhook(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteAWebhookResponse]:
        """
        Delete a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteAWebhookResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DeleteAWebhookResponse,
                    parse_obj_as(
                        type_=DeleteAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def update_a_webhook(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UpdateAWebhookResponse]:
        """
        Update the data associated with a specific webhook

        Parameters
        ----------
        id : str
            The ID of the webhook.

        events : typing.Optional[typing.Sequence[str]]
            The type of events that will trigger a notification to the target URL.

        target_url : typing.Optional[str]
            The URL of where the notification gets sent.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateAWebhookResponse]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhooks/{encode_path_param(id)}",
            method="PATCH",
            json={
                "events": events,
                "targetURL": target_url,
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
                    UpdateAWebhookResponse,
                    parse_obj_as(
                        type_=UpdateAWebhookResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def retrieve_webhook_verification_key(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[str]:
        """
        View the verification key for webhook security implementations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[str]
            200
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhooks/verification-key",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=_response.text)
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
