

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
from ..types.webhooks_create_new_response import WebhooksCreateNewResponse
from ..types.webhooks_delete_specific_response import WebhooksDeleteSpecificResponse
from ..types.webhooks_get_data_response import WebhooksGetDataResponse
from ..types.webhooks_list_all_response import WebhooksListAllResponse
from ..types.webhooks_update_webhook_data_response import WebhooksUpdateWebhookDataResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhooksListAllResponse]:
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
        HttpResponse[WebhooksListAllResponse]
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
                    WebhooksListAllResponse,
                    parse_obj_as(
                        type_=WebhooksListAllResponse,
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

    def createnew(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhooksCreateNewResponse]:
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
        HttpResponse[WebhooksCreateNewResponse]
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
                    WebhooksCreateNewResponse,
                    parse_obj_as(
                        type_=WebhooksCreateNewResponse,
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

    def getdata(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhooksGetDataResponse]:
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
        HttpResponse[WebhooksGetDataResponse]
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
                    WebhooksGetDataResponse,
                    parse_obj_as(
                        type_=WebhooksGetDataResponse,
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

    def deletespecific(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhooksDeleteSpecificResponse]:
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
        HttpResponse[WebhooksDeleteSpecificResponse]
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
                    WebhooksDeleteSpecificResponse,
                    parse_obj_as(
                        type_=WebhooksDeleteSpecificResponse,
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

    def updatewebhookdata(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhooksUpdateWebhookDataResponse]:
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
        HttpResponse[WebhooksUpdateWebhookDataResponse]
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
                    WebhooksUpdateWebhookDataResponse,
                    parse_obj_as(
                        type_=WebhooksUpdateWebhookDataResponse,
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

    def getverificationkey(self, *, request_options: typing.Optional[RequestOptions] = None) -> HttpResponse[str]:
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

    async def listall(
        self,
        *,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhooksListAllResponse]:
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
        AsyncHttpResponse[WebhooksListAllResponse]
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
                    WebhooksListAllResponse,
                    parse_obj_as(
                        type_=WebhooksListAllResponse,
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

    async def createnew(
        self,
        *,
        events: typing.Sequence[WebhookEventTypeValue],
        target_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhooksCreateNewResponse]:
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
        AsyncHttpResponse[WebhooksCreateNewResponse]
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
                    WebhooksCreateNewResponse,
                    parse_obj_as(
                        type_=WebhooksCreateNewResponse,
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

    async def getdata(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhooksGetDataResponse]:
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
        AsyncHttpResponse[WebhooksGetDataResponse]
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
                    WebhooksGetDataResponse,
                    parse_obj_as(
                        type_=WebhooksGetDataResponse,
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

    async def deletespecific(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhooksDeleteSpecificResponse]:
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
        AsyncHttpResponse[WebhooksDeleteSpecificResponse]
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
                    WebhooksDeleteSpecificResponse,
                    parse_obj_as(
                        type_=WebhooksDeleteSpecificResponse,
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

    async def updatewebhookdata(
        self,
        id: str,
        *,
        events: typing.Optional[typing.Sequence[str]] = OMIT,
        target_url: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhooksUpdateWebhookDataResponse]:
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
        AsyncHttpResponse[WebhooksUpdateWebhookDataResponse]
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
                    WebhooksUpdateWebhookDataResponse,
                    parse_obj_as(
                        type_=WebhooksUpdateWebhookDataResponse,
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

    async def getverificationkey(
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
