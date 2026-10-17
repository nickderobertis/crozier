

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.event_type import EventType
from ..types.http_method import HttpMethod
from ..types.http_validation_error import HttpValidationError
from ..types.webhook import Webhook
from ..types.webhook_page import WebhookPage
from ..types.webhook_update_params_method import WebhookUpdateParamsMethod
from ..types.webhook_update_params_subscriptions import WebhookUpdateParamsSubscriptions
from ..types.webhook_update_params_url import WebhookUpdateParamsUrl
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_webhook(self, *, id: str, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[Webhook]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/webhooks",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def list_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhookPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookPage]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/webhooks/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookPage,
                    parse_obj_as(
                        type_=WebhookPage,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
        subscriptions: typing.Sequence[EventType],
        url: str,
        method: typing.Optional[HttpMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """
        Parameters
        ----------
        subscriptions : typing.Sequence[EventType]

        url : str

        method : typing.Optional[HttpMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/webhooks/create",
            method="POST",
            json={
                "subscriptions": subscriptions,
                "url": url,
                "method": method,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
        *,
        id: str,
        subscriptions: typing.Optional[WebhookUpdateParamsSubscriptions] = OMIT,
        url: typing.Optional[WebhookUpdateParamsUrl] = OMIT,
        method: typing.Optional[WebhookUpdateParamsMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[Webhook]:
        """
        Parameters
        ----------
        id : str

        subscriptions : typing.Optional[WebhookUpdateParamsSubscriptions]

        url : typing.Optional[WebhookUpdateParamsUrl]

        method : typing.Optional[WebhookUpdateParamsMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[Webhook]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v1/webhooks/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=WebhookUpdateParamsSubscriptions, direction="write"
                ),
                "url": convert_and_respect_annotation_metadata(
                    object_=url, annotation=WebhookUpdateParamsUrl, direction="write"
                ),
                "method": convert_and_respect_annotation_metadata(
                    object_=method, annotation=WebhookUpdateParamsMethod, direction="write"
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_webhook(
        self, *, id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[Webhook]:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/webhooks",
            method="GET",
            params={
                "id": id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def list_webhooks(
        self,
        *,
        page: typing.Optional[int] = None,
        size: typing.Optional[int] = None,
        sort_column: typing.Optional[str] = None,
        sort_desc: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhookPage]:
        """
        Parameters
        ----------
        page : typing.Optional[int]

        size : typing.Optional[int]

        sort_column : typing.Optional[str]

        sort_desc : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookPage]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/webhooks/list",
            method="GET",
            params={
                "page": page,
                "size": size,
                "sort_column": sort_column,
                "sort_desc": sort_desc,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookPage,
                    parse_obj_as(
                        type_=WebhookPage,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
        subscriptions: typing.Sequence[EventType],
        url: str,
        method: typing.Optional[HttpMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """
        Parameters
        ----------
        subscriptions : typing.Sequence[EventType]

        url : str

        method : typing.Optional[HttpMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/webhooks/create",
            method="POST",
            json={
                "subscriptions": subscriptions,
                "url": url,
                "method": method,
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
        *,
        id: str,
        subscriptions: typing.Optional[WebhookUpdateParamsSubscriptions] = OMIT,
        url: typing.Optional[WebhookUpdateParamsUrl] = OMIT,
        method: typing.Optional[WebhookUpdateParamsMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[Webhook]:
        """
        Parameters
        ----------
        id : str

        subscriptions : typing.Optional[WebhookUpdateParamsSubscriptions]

        url : typing.Optional[WebhookUpdateParamsUrl]

        method : typing.Optional[WebhookUpdateParamsMethod]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[Webhook]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v1/webhooks/update",
            method="POST",
            params={
                "id": id,
            },
            json={
                "subscriptions": convert_and_respect_annotation_metadata(
                    object_=subscriptions, annotation=WebhookUpdateParamsSubscriptions, direction="write"
                ),
                "url": convert_and_respect_annotation_metadata(
                    object_=url, annotation=WebhookUpdateParamsUrl, direction="write"
                ),
                "method": convert_and_respect_annotation_metadata(
                    object_=method, annotation=WebhookUpdateParamsMethod, direction="write"
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
                    Webhook,
                    parse_obj_as(
                        type_=Webhook,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
