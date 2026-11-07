

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.dav_direct_get_url200response import DavDirectGetUrl200Response
from pydantic import ValidationError


class RawDavDirectClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_url(
        self,
        *,
        file_id: int,
        expiration_time: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[DavDirectGetUrl200Response]:
        """
        Parameters
        ----------
        file_id : int
            ID of the file

        expiration_time : typing.Optional[int]
            Duration until the link expires

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DavDirectGetUrl200Response]
            Direct link returned
        """
        _response = self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/dav/api/v1/direct",
            method="POST",
            params={
                "fileId": file_id,
                "expirationTime": expiration_time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DavDirectGetUrl200Response,
                    parse_obj_as(
                        type_=DavDirectGetUrl200Response,
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


class AsyncRawDavDirectClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_url(
        self,
        *,
        file_id: int,
        expiration_time: typing.Optional[int] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[DavDirectGetUrl200Response]:
        """
        Parameters
        ----------
        file_id : int
            ID of the file

        expiration_time : typing.Optional[int]
            Duration until the link expires

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DavDirectGetUrl200Response]
            Direct link returned
        """
        _response = await self._client_wrapper.httpx_client.request(
            "ocs/v2.php/apps/dav/api/v1/direct",
            method="POST",
            params={
                "fileId": file_id,
                "expirationTime": expiration_time,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    DavDirectGetUrl200Response,
                    parse_obj_as(
                        type_=DavDirectGetUrl200Response,
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
