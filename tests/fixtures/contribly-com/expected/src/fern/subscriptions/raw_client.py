

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.subscription import Subscription
from ..types.subscription_type import SubscriptionType
from pydantic import ValidationError


class RawSubscriptionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def subscription_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[SubscriptionType]]:
        """
        List available subscription types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[SubscriptionType]]
            A list of subscription event types
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscription-types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SubscriptionType],
                    parse_obj_as(
                        type_=typing.List[SubscriptionType],
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

    def list_subscriptions_for_the_authorised_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[Subscription]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[Subscription]]
            A list of notification subscriptions
        """
        _response = self._client_wrapper.httpx_client.request(
            "subscriptions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Subscription],
                    parse_obj_as(
                        type_=typing.List[Subscription],
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

    def delete_a_subscription(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Id of the subscription to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawSubscriptionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def subscription_types(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[SubscriptionType]]:
        """
        List available subscription types

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[SubscriptionType]]
            A list of subscription event types
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscription-types",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[SubscriptionType],
                    parse_obj_as(
                        type_=typing.List[SubscriptionType],
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

    async def list_subscriptions_for_the_authorised_user(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[Subscription]]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[Subscription]]
            A list of notification subscriptions
        """
        _response = await self._client_wrapper.httpx_client.request(
            "subscriptions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[Subscription],
                    parse_obj_as(
                        type_=typing.List[Subscription],
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

    async def delete_a_subscription(
        self, id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        id : str
            Id of the subscription to delete

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"subscriptions/{encode_path_param(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
