

import datetime as dt
import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.unauthorized_error import UnauthorizedError
from ..types.v1user_capacity import V1UserCapacity
from .types.list_users_capacities_response_item import ListUsersCapacitiesResponseItem
from pydantic import ValidationError


class RawUserCapacitiesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_user_capacities(
        self, account_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[V1UserCapacity]]:
        """
        Retrieve capacity configurations for a specific user. Capacities define a user's working hours, working days, and daily/weekly hour limits.

        Parameters
        ----------
        account_id : int
            Account ID

        user_id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[V1UserCapacity]]
            User's capacities retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(user_id)}/capacities",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1UserCapacity],
                    parse_obj_as(
                        type_=typing.List[V1UserCapacity],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def list_users_capacities(
        self,
        account_id: int,
        *,
        user_ids: typing.Optional[str] = None,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[typing.List[ListUsersCapacitiesResponseItem]]:
        """
        Retrieve capacity configurations for multiple users in the account. Supports filtering by user IDs and date range.

        Parameters
        ----------
        account_id : int
            Account ID

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        since : typing.Optional[dt.date]
            Fetch capacities after this date (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            Fetch capacities before this date (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[ListUsersCapacitiesResponseItem]]
            Users capacities retrieved successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/capacities",
            method="GET",
            params={
                "user_ids": user_ids,
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListUsersCapacitiesResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListUsersCapacitiesResponseItem],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUserCapacitiesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_user_capacities(
        self, account_id: int, user_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[V1UserCapacity]]:
        """
        Retrieve capacity configurations for a specific user. Capacities define a user's working hours, working days, and daily/weekly hour limits.

        Parameters
        ----------
        account_id : int
            Account ID

        user_id : int
            User ID

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[V1UserCapacity]]
            User's capacities retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/{encode_path_param(user_id)}/capacities",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[V1UserCapacity],
                    parse_obj_as(
                        type_=typing.List[V1UserCapacity],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def list_users_capacities(
        self,
        account_id: int,
        *,
        user_ids: typing.Optional[str] = None,
        since: typing.Optional[dt.date] = None,
        until: typing.Optional[dt.date] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[typing.List[ListUsersCapacitiesResponseItem]]:
        """
        Retrieve capacity configurations for multiple users in the account. Supports filtering by user IDs and date range.

        Parameters
        ----------
        account_id : int
            Account ID

        user_ids : typing.Optional[str]
            Comma-separated list of user IDs to filter by

        since : typing.Optional[dt.date]
            Fetch capacities after this date (YYYY-MM-DD)

        until : typing.Optional[dt.date]
            Fetch capacities before this date (YYYY-MM-DD)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[ListUsersCapacitiesResponseItem]]
            Users capacities retrieved successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"1.1/{encode_path_param(account_id)}/users/capacities",
            method="GET",
            params={
                "user_ids": user_ids,
                "since": str(since) if since is not None else None,
                "until": str(until) if until is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[ListUsersCapacitiesResponseItem],
                    parse_obj_as(
                        type_=typing.List[ListUsersCapacitiesResponseItem],
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
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
