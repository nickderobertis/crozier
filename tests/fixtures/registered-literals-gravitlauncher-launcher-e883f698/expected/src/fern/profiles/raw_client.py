

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.list_profiles_response import ListProfilesResponse
from ..types.update_info import UpdateInfo
from pydantic import ValidationError


class RawProfilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_all_available_client_profiles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListProfilesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListProfilesResponse]
            Profile list.
        """
        _response = self._client_wrapper.httpx_client.request(
            "profile/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListProfilesResponse,
                    parse_obj_as(
                        type_=ListProfilesResponse,
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

    def fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
        self, profile_uuid: str, dir_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UpdateInfo]:
        """
        Parameters
        ----------
        profile_uuid : str

        dir_name : str
            Directory name, e.g. "client" or "assets".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UpdateInfo]
            Update info including HashedDir and base download URL.
        """
        _response = self._client_wrapper.httpx_client.request(
            f"profile/by/uuid/{encode_path_param(profile_uuid)}/dir/{encode_path_param(dir_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateInfo,
                    parse_obj_as(
                        type_=UpdateInfo,
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


class AsyncRawProfilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_all_available_client_profiles(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListProfilesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListProfilesResponse]
            Profile list.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "profile/list",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListProfilesResponse,
                    parse_obj_as(
                        type_=ListProfilesResponse,
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

    async def fetch_hashed_directory_update_info_for_a_named_directory_of_a_profile(
        self, profile_uuid: str, dir_name: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UpdateInfo]:
        """
        Parameters
        ----------
        profile_uuid : str

        dir_name : str
            Directory name, e.g. "client" or "assets".

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UpdateInfo]
            Update info including HashedDir and base download URL.
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"profile/by/uuid/{encode_path_param(profile_uuid)}/dir/{encode_path_param(dir_name)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UpdateInfo,
                    parse_obj_as(
                        type_=UpdateInfo,
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
