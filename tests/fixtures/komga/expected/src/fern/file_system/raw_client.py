

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..errors.bad_request_error import BadRequestError
from ..types.directory_listing_dto import DirectoryListingDto
from ..types.validation_error_response import ValidationErrorResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFileSystemClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def get_directory_listing(
        self, *, path: str, show_files: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[DirectoryListingDto]:
        """
        List folders and files from the host server's file system. If no request body is passed then the root directories are returned.

        Required role: **ADMIN**

        Parameters
        ----------
        path : str

        show_files : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[DirectoryListingDto]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/v1/filesystem",
            method="POST",
            json={
                "path": path,
                "showFiles": show_files,
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
                    DirectoryListingDto,
                    parse_obj_as(
                        type_=DirectoryListingDto,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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


class AsyncRawFileSystemClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def get_directory_listing(
        self, *, path: str, show_files: bool, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[DirectoryListingDto]:
        """
        List folders and files from the host server's file system. If no request body is passed then the root directories are returned.

        Required role: **ADMIN**

        Parameters
        ----------
        path : str

        show_files : bool

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[DirectoryListingDto]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/v1/filesystem",
            method="POST",
            json={
                "path": path,
                "showFiles": show_files,
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
                    DirectoryListingDto,
                    parse_obj_as(
                        type_=DirectoryListingDto,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ValidationErrorResponse,
                        parse_obj_as(
                            type_=ValidationErrorResponse,
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
