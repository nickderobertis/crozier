

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.not_found_error import NotFoundError
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.get_subscribers_subscription_get_subscribers_get_request_limit import (
    GetSubscribersSubscriptionGetSubscribersGetRequestLimit,
)
from ..types.get_subscribers_subscription_get_subscribers_get_request_offset import (
    GetSubscribersSubscriptionGetSubscribersGetRequestOffset,
)
from ..types.get_subscriptions_order import GetSubscriptionsOrder
from ..types.get_subscriptions_subscription_get_subscriptions_get_request_limit import (
    GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit,
)
from ..types.get_subscriptions_subscription_get_subscriptions_get_request_offset import (
    GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset,
)
from ..types.http_validation_error import HttpValidationError
from ..types.subscribe_response import SubscribeResponse
from ..types.subscribers_response import SubscribersResponse
from ..types.subscriptions_response import SubscriptionsResponse
from ..types.unsubscribe_response import UnsubscribeResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawSubscriptionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def subscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscribeResponse]:
        """
        Оформление подписки

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди на кого подписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscribeResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscription/subscribe",
            method="POST",
            json={
                "subscription_id": subscription_id,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscribeResponse,
                    parse_obj_as(
                        type_=SubscribeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    def unsubscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UnsubscribeResponse]:
        """
        Отписка от пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди от кого отписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UnsubscribeResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscription/unsubscribe",
            method="DELETE",
            json={
                "subscription_id": subscription_id,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnsubscribeResponse,
                    parse_obj_as(
                        type_=UnsubscribeResponse,
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

    def get_subscriptions(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset] = None,
        limit: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscriptionsResponse]:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset]

        limit : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionsResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscription/get_subscriptions",
            method="GET",
            params={
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionsResponse,
                    parse_obj_as(
                        type_=SubscriptionsResponse,
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

    def get_subscribers(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset] = None,
        limit: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[SubscribersResponse]:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset]

        limit : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscribersResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscription/get_subscribers",
            method="GET",
            params={
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscribersResponse,
                    parse_obj_as(
                        type_=SubscribersResponse,
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


class AsyncRawSubscriptionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def subscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscribeResponse]:
        """
        Оформление подписки

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди на кого подписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscribeResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscription/subscribe",
            method="POST",
            json={
                "subscription_id": subscription_id,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscribeResponse,
                    parse_obj_as(
                        type_=SubscribeResponse,
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
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
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

    async def unsubscribe(
        self, *, authorization: str, subscription_id: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UnsubscribeResponse]:
        """
        Отписка от пользователя

        Parameters
        ----------
        authorization : str
            Enter the token with the 'Bearer:' prefix.

        subscription_id : int
            Айди от кого отписка

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UnsubscribeResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscription/unsubscribe",
            method="DELETE",
            json={
                "subscription_id": subscription_id,
            },
            headers={
                "content-type": "application/json",
                "Authorization": str(authorization) if authorization is not None else None,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UnsubscribeResponse,
                    parse_obj_as(
                        type_=UnsubscribeResponse,
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

    async def get_subscriptions(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset] = None,
        limit: typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscriptionsResponse]:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestOffset]

        limit : typing.Optional[GetSubscriptionsSubscriptionGetSubscriptionsGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionsResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscription/get_subscriptions",
            method="GET",
            params={
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionsResponse,
                    parse_obj_as(
                        type_=SubscriptionsResponse,
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

    async def get_subscribers(
        self,
        *,
        user_id: int,
        offset: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset] = None,
        limit: typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit] = None,
        order: typing.Optional[GetSubscriptionsOrder] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[SubscribersResponse]:
        """
        Получение подписчиков пользователя

        Parameters
        ----------
        user_id : int

        offset : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestOffset]

        limit : typing.Optional[GetSubscribersSubscriptionGetSubscribersGetRequestLimit]

        order : typing.Optional[GetSubscriptionsOrder]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscribersResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscription/get_subscribers",
            method="GET",
            params={
                "user_id": user_id,
                "offset": offset,
                "limit": limit,
                "order": order,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscribersResponse,
                    parse_obj_as(
                        type_=SubscribersResponse,
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
