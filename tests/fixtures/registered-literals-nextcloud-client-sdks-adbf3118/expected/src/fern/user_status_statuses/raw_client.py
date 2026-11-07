

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.user_status_statuses_find200response import UserStatusStatusesFind200Response
from ..types.user_status_statuses_find_all200response import UserStatusStatusesFindAll200Response
from pydantic import ValidationError


class RawUserStatusStatusesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def find_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UserStatusStatusesFindAll200Response]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of statuses to find

        offset : typing.Optional[int]
            Offset for finding statuses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusStatusesFindAll200Response]

        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/statuses",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusStatusesFindAll200Response,
                    parse_obj_as(
                        type_=UserStatusStatusesFindAll200Response,
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

    def find(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UserStatusStatusesFind200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UserStatusStatusesFind200Response]
            The status was found successfully
        """
        _response = self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/user_status/api/v1/statuses/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusStatusesFind200Response,
                    parse_obj_as(
                        type_=UserStatusStatusesFind200Response,
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


class AsyncRawUserStatusStatusesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def find_all(
        self,
        *,
        limit: typing.Optional[int] = None,
        offset: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UserStatusStatusesFindAll200Response]:
        """
        Parameters
        ----------
        limit : typing.Optional[int]
            Maximum number of statuses to find

        offset : typing.Optional[int]
            Offset for finding statuses

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusStatusesFindAll200Response]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/user_status/api/v1/statuses",
            method="GET",
            params={
                "limit": limit,
                "offset": offset,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusStatusesFindAll200Response,
                    parse_obj_as(
                        type_=UserStatusStatusesFindAll200Response,
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

    async def find(
        self, user_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UserStatusStatusesFind200Response]:
        """
        Parameters
        ----------
        user_id : str
            ID of the user

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UserStatusStatusesFind200Response]
            The status was found successfully
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"ocs/v2.php/apps/user_status/api/v1/statuses/{encode_path_param(user_id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UserStatusStatusesFind200Response,
                    parse_obj_as(
                        type_=UserStatusStatusesFind200Response,
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
