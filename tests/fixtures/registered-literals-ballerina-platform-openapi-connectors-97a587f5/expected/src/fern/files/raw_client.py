

import contextlib
import typing
from json.decoder import JSONDecodeError

from .. import core
from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..types.file import File
from ..types.file_list import FileList
from ..types.purpose import Purpose
from .types.files_upload_request_purpose import FilesUploadRequestPurpose
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawFilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[FileList]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[FileList]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            "files",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileList,
                    parse_obj_as(
                        type_=FileList,
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

    def upload(
        self,
        *,
        api_version: str,
        purpose: FilesUploadRequestPurpose,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[File]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : FilesUploadRequestPurpose
            The intended purpose of the uploaded documents. Use "fine-tune" for fine-tuning. This allows us to validate the format of the uploaded file.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[File]
            The file has been successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "files",
            method="POST",
            params={
                "api-version": api_version,
            },
            data={
                "purpose": purpose,
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
                    File,
                    parse_obj_as(
                        type_=File,
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

    def get(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[File]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[File]
            Success
        """
        _response = self._client_wrapper.httpx_client.request(
            f"files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    File,
                    parse_obj_as(
                        type_=File,
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

    def delete(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"files/{encode_path_param(file_id)}",
            method="DELETE",
            params={
                "api-version": api_version,
            },
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

    @contextlib.contextmanager
    def getcontent(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[HttpResponse[typing.Iterator[bytes]]]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[HttpResponse[typing.Iterator[bytes]]]
            Success
        """
        with self._client_wrapper.httpx_client.stream(
            f"files/{encode_path_param(file_id)}/content",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        ) as _response:

            def _stream() -> HttpResponse[typing.Iterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return HttpResponse(
                            response=_response, data=(_chunk for _chunk in _response.iter_bytes(chunk_size=_chunk_size))
                        )
                    _response.read()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield _stream()

    def import_(
        self,
        *,
        api_version: str,
        purpose: Purpose,
        filename: str,
        content_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[File]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : Purpose

        filename : str
            The name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.
            If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt" and "completion" fields representing your training examples.

        content_url : str
            The url to download the document from (can be SAS url of a blob or any other external url accessible with a GET request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[File]
            The file has been successfully created.
        """
        _response = self._client_wrapper.httpx_client.request(
            "files/import",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "purpose": purpose,
                "filename": filename,
                "content_url": content_url,
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
                    File,
                    parse_obj_as(
                        type_=File,
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


class AsyncRawFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[FileList]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[FileList]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            "files",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    FileList,
                    parse_obj_as(
                        type_=FileList,
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

    async def upload(
        self,
        *,
        api_version: str,
        purpose: FilesUploadRequestPurpose,
        file: core.File,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[File]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : FilesUploadRequestPurpose
            The intended purpose of the uploaded documents. Use "fine-tune" for fine-tuning. This allows us to validate the format of the uploaded file.

        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[File]
            The file has been successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "files",
            method="POST",
            params={
                "api-version": api_version,
            },
            data={
                "purpose": purpose,
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
                    File,
                    parse_obj_as(
                        type_=File,
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

    async def get(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[File]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[File]
            Success
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    File,
                    parse_obj_as(
                        type_=File,
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

    async def delete(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"files/{encode_path_param(file_id)}",
            method="DELETE",
            params={
                "api-version": api_version,
            },
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

    @contextlib.asynccontextmanager
    async def getcontent(
        self, file_id: str, *, api_version: str, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]:
        """
        Parameters
        ----------
        file_id : str
            The identifier of the file.

        api_version : str
            The requested API version.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[AsyncHttpResponse[typing.AsyncIterator[bytes]]]
            Success
        """
        async with self._client_wrapper.httpx_client.stream(
            f"files/{encode_path_param(file_id)}/content",
            method="GET",
            params={
                "api-version": api_version,
            },
            request_options=request_options,
        ) as _response:

            async def _stream() -> AsyncHttpResponse[typing.AsyncIterator[bytes]]:
                try:
                    if 200 <= _response.status_code < 300:
                        _chunk_size = request_options.get("chunk_size", None) if request_options is not None else None
                        return AsyncHttpResponse(
                            response=_response,
                            data=(_chunk async for _chunk in _response.aiter_bytes(chunk_size=_chunk_size)),
                        )
                    await _response.aread()
                    _response_json = _response.json()
                except JSONDecodeError:
                    raise ApiError(
                        status_code=_response.status_code, headers=dict(_response.headers), body=_response.text
                    )
                except ValidationError as e:
                    raise ParsingError(
                        status_code=_response.status_code,
                        headers=dict(_response.headers),
                        body=_response.json(),
                        cause=e,
                    )
                raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

            yield await _stream()

    async def import_(
        self,
        *,
        api_version: str,
        purpose: Purpose,
        filename: str,
        content_url: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[File]:
        """
        Parameters
        ----------
        api_version : str
            The requested API version.

        purpose : Purpose

        filename : str
            The name of the [JSON Lines](https://jsonlines.readthedocs.io/en/latest/) file to be uploaded.
            If the `purpose` is set to "fine-tune", each line is a JSON record with "prompt" and "completion" fields representing your training examples.

        content_url : str
            The url to download the document from (can be SAS url of a blob or any other external url accessible with a GET request).

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[File]
            The file has been successfully created.
        """
        _response = await self._client_wrapper.httpx_client.request(
            "files/import",
            method="POST",
            params={
                "api-version": api_version,
            },
            json={
                "purpose": purpose,
                "filename": filename,
                "content_url": content_url,
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
                    File,
                    parse_obj_as(
                        type_=File,
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
