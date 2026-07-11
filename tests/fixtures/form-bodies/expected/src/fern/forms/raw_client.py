

import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.file_metadata import FileMetadata
from ..types.upload_response import UploadResponse


OMIT = typing.cast(typing.Any, ...)


class RawFormsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload(
        self,
        *,
        file: core.File,
        filename: typing.Optional[str] = OMIT,
        metadata: typing.Optional[FileMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        filename : typing.Optional[str]

        metadata : typing.Optional[FileMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadResponse]

        """
        _response = self._client_wrapper.httpx_client.request(
            "upload",
            method="POST",
            data={
                "filename": filename,
                "metadata": metadata,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadResponse,
                    parse_obj_as(
                        type_=UploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def submit(
        self,
        *,
        name: str,
        age: typing.Optional[int] = OMIT,
        subscribe: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        name : str

        age : typing.Optional[int]

        subscribe : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            "submit",
            method="POST",
            data={
                "name": name,
                "age": age,
                "subscribe": subscribe,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawFormsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload(
        self,
        *,
        file: core.File,
        filename: typing.Optional[str] = OMIT,
        metadata: typing.Optional[FileMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadResponse]:
        """
        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        filename : typing.Optional[str]

        metadata : typing.Optional[FileMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadResponse]

        """
        _response = await self._client_wrapper.httpx_client.request(
            "upload",
            method="POST",
            data={
                "filename": filename,
                "metadata": metadata,
            },
            files={
                "file": file,
            },
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadResponse,
                    parse_obj_as(
                        type_=UploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def submit(
        self,
        *,
        name: str,
        age: typing.Optional[int] = OMIT,
        subscribe: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        name : str

        age : typing.Optional[int]

        subscribe : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            "submit",
            method="POST",
            data={
                "name": name,
                "age": age,
                "subscribe": subscribe,
            },
            headers={
                "content-type": "application/x-www-form-urlencoded",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
