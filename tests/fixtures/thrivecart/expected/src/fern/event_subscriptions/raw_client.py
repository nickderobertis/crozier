

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.unauthorized_error import UnauthorizedError
from .types.create_event_subscription_request_event import CreateEventSubscriptionRequestEvent
from .types.create_event_subscription_response import CreateEventSubscriptionResponse
from .types.delete_event_subscription_response import DeleteEventSubscriptionResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawEventSubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_event_subscription(
        self,
        *,
        event: CreateEventSubscriptionRequestEvent,
        target_url: str,
        product_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateEventSubscriptionResponse]:
        """
        Create a webhook-style event subscription. Unlike standard webhooks, event subscriptions always receive JSON and can target specific events.

        Parameters
        ----------
        event : CreateEventSubscriptionRequestEvent
            Event type to subscribe to. Use '*' for all events.

        target_url : str
            URL to receive the event notifications

        product_id : typing.Optional[int]
            Optional: limit to a specific product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateEventSubscriptionResponse]
            Subscription created
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscribe",
            method="POST",
            json={
                "event": event,
                "target_url": target_url,
                "product_id": product_id,
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
                    CreateEventSubscriptionResponse,
                    parse_obj_as(
                        type_=CreateEventSubscriptionResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def delete_event_subscription(
        self, *, subscription_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DeleteEventSubscriptionResponse]:
        """
        Remove an existing event subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DeleteEventSubscriptionResponse]
            Subscription removed
        """
        _response = self._client_wrapper.httpx_client.request(
            "unsubscribe",
            method="POST",
            json={
                "subscription_id": subscription_id,
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
                    DeleteEventSubscriptionResponse,
                    parse_obj_as(
                        type_=DeleteEventSubscriptionResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawEventSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_event_subscription(
        self,
        *,
        event: CreateEventSubscriptionRequestEvent,
        target_url: str,
        product_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateEventSubscriptionResponse]:
        """
        Create a webhook-style event subscription. Unlike standard webhooks, event subscriptions always receive JSON and can target specific events.

        Parameters
        ----------
        event : CreateEventSubscriptionRequestEvent
            Event type to subscribe to. Use '*' for all events.

        target_url : str
            URL to receive the event notifications

        product_id : typing.Optional[int]
            Optional: limit to a specific product

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateEventSubscriptionResponse]
            Subscription created
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscribe",
            method="POST",
            json={
                "event": event,
                "target_url": target_url,
                "product_id": product_id,
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
                    CreateEventSubscriptionResponse,
                    parse_obj_as(
                        type_=CreateEventSubscriptionResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def delete_event_subscription(
        self, *, subscription_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DeleteEventSubscriptionResponse]:
        """
        Remove an existing event subscription.

        Parameters
        ----------
        subscription_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DeleteEventSubscriptionResponse]
            Subscription removed
        """
        _response = await self._client_wrapper.httpx_client.request(
            "unsubscribe",
            method="POST",
            json={
                "subscription_id": subscription_id,
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
                    DeleteEventSubscriptionResponse,
                    parse_obj_as(
                        type_=DeleteEventSubscriptionResponse,
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
