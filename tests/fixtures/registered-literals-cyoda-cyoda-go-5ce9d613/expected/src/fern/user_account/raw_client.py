

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.subscriptions_response_dto import SubscriptionsResponseDto
from ..types.user_account_info_response_dto import UserAccountInfoResponseDto
from pydantic import ValidationError


class RawUserAccountClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def account_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserAccountInfoResponseDto]:
        """
        Fetch information related to the current user's account, such as legal entity, roles, and current subscription.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserAccountInfoResponseDto]
            Current user's account information with current subscription details
        """
        _response = self._client_wrapper.httpx_client.request(
            "account",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserAccountInfoResponseDto,
                    parse_obj_as(
                        type_=UserAccountInfoResponseDto,
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

    def account_subscriptions_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[SubscriptionsResponseDto]:
        """
        Fetch all subscription details associated with the legal entity of the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[SubscriptionsResponseDto]
            Collection of all subscriptions for the user's legal entity
        """
        _response = self._client_wrapper.httpx_client.request(
            "account/subscriptions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionsResponseDto,
                    parse_obj_as(
                        type_=SubscriptionsResponseDto,
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


class AsyncRawUserAccountClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def account_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserAccountInfoResponseDto]:
        """
        Fetch information related to the current user's account, such as legal entity, roles, and current subscription.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserAccountInfoResponseDto]
            Current user's account information with current subscription details
        """
        _response = await self._client_wrapper.httpx_client.request(
            "account",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserAccountInfoResponseDto,
                    parse_obj_as(
                        type_=UserAccountInfoResponseDto,
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

    async def account_subscriptions_get(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[SubscriptionsResponseDto]:
        """
        Fetch all subscription details associated with the legal entity of the current user.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[SubscriptionsResponseDto]
            Collection of all subscriptions for the user's legal entity
        """
        _response = await self._client_wrapper.httpx_client.request(
            "account/subscriptions",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    SubscriptionsResponseDto,
                    parse_obj_as(
                        type_=SubscriptionsResponseDto,
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
