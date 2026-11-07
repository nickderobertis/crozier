

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.profile_data_list import ProfileDataList
from pydantic import ValidationError


class RawDseClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_profile_data(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ProfileDataList]:
        """
        Get profile data for all submitted ids. If a profile is not found, an error message will be supplied.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (here - mostly URLs) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ProfileDataList]
            Success, returning profiles - may contain profiles with error messages
        """
        _response = self._client_wrapper.httpx_client.request(
            "dse/profile-data",
            method="GET",
            params={
                "ids": ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileDataList,
                    parse_obj_as(
                        type_=ProfileDataList,
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


class AsyncRawDseClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_profile_data(
        self, *, ids: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ProfileDataList]:
        """
        Get profile data for all submitted ids. If a profile is not found, an error message will be supplied.

        Parameters
        ----------
        ids : str
            A comma-separated list of IDs (here - mostly URLs) of the entries that shall be retrieved.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ProfileDataList]
            Success, returning profiles - may contain profiles with error messages
        """
        _response = await self._client_wrapper.httpx_client.request(
            "dse/profile-data",
            method="GET",
            params={
                "ids": ids,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ProfileDataList,
                    parse_obj_as(
                        type_=ProfileDataList,
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
