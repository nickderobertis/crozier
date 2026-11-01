

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
from ..errors.too_many_requests_error import TooManyRequestsError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.error import Error
from ..types.webhook_envelope import WebhookEnvelope
from ..types.webhook_list import WebhookList
from .types.webhook_toevoegen_request_event import WebhookToevoegenRequestEvent
from .types.webhook_wijzigen_request_event import WebhookWijzigenRequestEvent
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawWebhooksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def alle_webhooks_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookList]:
        """
        All webhooks of a list in an array of member objects. The webhook objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookList]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhook",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookList,
                    parse_obj_as(
                        type_=WebhookList,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def webhook_toevoegen(
        self,
        *,
        list_id: str,
        event: WebhookToevoegenRequestEvent,
        url: str,
        blocked: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhookEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : WebhookToevoegenRequestEvent
            When will the webhook be requested? (subscribed, modified of deactivated)

        url : str
            The URL to be accessed

        blocked : bool
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            "webhook",
            method="POST",
            data={
                "list_id": list_id,
                "event": event,
                "url": url,
                "blocked": blocked,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def webhook_opvragen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookEnvelope]:
        """
        All information about a webhook

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def webhook_wijzigen(
        self,
        webhook_id: str,
        *,
        list_id: str,
        event: typing.Optional[WebhookWijzigenRequestEvent] = OMIT,
        url: typing.Optional[str] = OMIT,
        blocked: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[WebhookEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : typing.Optional[WebhookWijzigenRequestEvent]
            When will the webhook be requested? (subscribed, modified or deactivated)

        url : typing.Optional[str]
            The URL to be accessed

        blocked : typing.Optional[bool]
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="POST",
            data={
                "list_id": list_id,
                "event": event,
                "url": url,
                "blocked": blocked,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    def webhook_verwijderen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[WebhookEnvelope]:
        """
        This permanently deletes a webhook. Potentially outstanding requests from the webhook will still be completed. If the field does not exist, an error message is displayed. In response you are shown another webhook object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the webhook.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="DELETE",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def alle_webhooks_opvragen(
        self, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookList]:
        """
        All webhooks of a list in an array of member objects. The webhook objects are formatted in an array named 'data'.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookList]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhook",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookList,
                    parse_obj_as(
                        type_=WebhookList,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def webhook_toevoegen(
        self,
        *,
        list_id: str,
        event: WebhookToevoegenRequestEvent,
        url: str,
        blocked: bool,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhookEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : WebhookToevoegenRequestEvent
            When will the webhook be requested? (subscribed, modified of deactivated)

        url : str
            The URL to be accessed

        blocked : bool
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "webhook",
            method="POST",
            data={
                "list_id": list_id,
                "event": event,
                "url": url,
                "blocked": blocked,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def webhook_opvragen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookEnvelope]:
        """
        All information about a webhook

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="GET",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def webhook_wijzigen(
        self,
        webhook_id: str,
        *,
        list_id: str,
        event: typing.Optional[WebhookWijzigenRequestEvent] = OMIT,
        url: typing.Optional[str] = OMIT,
        blocked: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[WebhookEnvelope]:
        """
        If there is something wrong with the parameters provided, a code is displayed with an error message. Fields that are not mentioned will keep their current value fields keep their current value. As soon as a field is mentioned it does get checked, and thus can cause an error message. This error message displays a code with a message. See above under 'Error messages' what the codes stand for. See above under 'Error messages' what the codes stand for.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        event : typing.Optional[WebhookWijzigenRequestEvent]
            When will the webhook be requested? (subscribed, modified or deactivated)

        url : typing.Optional[str]
            The URL to be accessed

        blocked : typing.Optional[bool]
            Is the accessing of the webhook (temporarily) blocked? (true or false)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="POST",
            data={
                "list_id": list_id,
                "event": event,
                "url": url,
                "blocked": blocked,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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

    async def webhook_verwijderen(
        self, webhook_id: str, *, list_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[WebhookEnvelope]:
        """
        This permanently deletes a webhook. Potentially outstanding requests from the webhook will still be completed. If the field does not exist, an error message is displayed. In response you are shown another webhook object, but now with the state 'deleted'. After having finished this procedure, it is no longer possible for the user to request the webhook.

        Parameters
        ----------
        webhook_id : str
            The id of the webhook. You find it in the response of [Get all webhooks](/webhooks/alle-webhooks-opvragen).

        list_id : str
            The id of the list. You find it in the response of [Get all lists](/lijsten/alle-lijsten-opvragen), and in the application in the URL of the list.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[WebhookEnvelope]
            The request succeeded.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"webhook/{encode_path_param(webhook_id)}",
            method="DELETE",
            params={
                "list_id": list_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    WebhookEnvelope,
                    parse_obj_as(
                        type_=WebhookEnvelope,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 429:
                raise TooManyRequestsError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        Error,
                        parse_obj_as(
                            type_=Error,
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
