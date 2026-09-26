

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.jsonable_encoder import encode_path_param
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from ..errors.bad_request_error import BadRequestError
from ..errors.conflict_error import ConflictError
from ..errors.forbidden_error import ForbiddenError
from ..errors.not_found_error import NotFoundError
from ..errors.service_unavailable_error import ServiceUnavailableError
from ..errors.unauthorized_error import UnauthorizedError
from ..types.api_error_response import ApiErrorResponse
from ..types.complete_nnue_upload_response import CompleteNnueUploadResponse
from ..types.initialize_nnue_upload_response import InitializeNnueUploadResponse
from ..types.list_nnue_files_response import ListNnueFilesResponse
from ..types.ok_response import OkResponse
from ..types.upload_nnue_part_response import UploadNnuePartResponse
from .types.complete_nnue_upload_request_parts_item import CompleteNnueUploadRequestPartsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawNnueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_nnue_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[ListNnueFilesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[ListNnueFilesResponse]
            List NNUE files
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/nnue/files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListNnueFilesResponse,
                    parse_obj_as(
                        type_=ListNnueFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def initialize_nnue_upload(
        self,
        *,
        original_filename: str,
        size_bytes: int,
        sha256hex: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[InitializeNnueUploadResponse]:
        """
        Parameters
        ----------
        original_filename : str

        size_bytes : int

        sha256hex : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[InitializeNnueUploadResponse]
            Initialized NNUE upload
        """
        _response = self._client_wrapper.httpx_client.request(
            "api/nnue/uploads/init",
            method="POST",
            json={
                "originalFilename": original_filename,
                "sizeBytes": size_bytes,
                "sha256Hex": sha256hex,
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
                    InitializeNnueUploadResponse,
                    parse_obj_as(
                        type_=InitializeNnueUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def upload_nnue_part(
        self, file_id: str, part_number: int, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[UploadNnuePartResponse]:
        """
        Parameters
        ----------
        file_id : str

        part_number : int

        upload_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadNnuePartResponse]
            Uploaded NNUE part
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nnue/uploads/{encode_path_param(file_id)}/parts/{encode_path_param(part_number)}",
            method="PUT",
            params={
                "uploadId": upload_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadNnuePartResponse,
                    parse_obj_as(
                        type_=UploadNnuePartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def complete_nnue_upload(
        self,
        file_id: str,
        *,
        upload_id: str,
        parts: typing.Sequence[CompleteNnueUploadRequestPartsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompleteNnueUploadResponse]:
        """
        Parameters
        ----------
        file_id : str

        upload_id : str

        parts : typing.Sequence[CompleteNnueUploadRequestPartsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompleteNnueUploadResponse]
            Completed NNUE upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nnue/uploads/{encode_path_param(file_id)}/complete",
            method="POST",
            json={
                "uploadId": upload_id,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[CompleteNnueUploadRequestPartsItem], direction="write"
                ),
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
                    CompleteNnueUploadResponse,
                    parse_obj_as(
                        type_=CompleteNnueUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def abort_nnue_upload(
        self, file_id: str, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """
        Parameters
        ----------
        file_id : str

        upload_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            Aborted NNUE upload
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nnue/uploads/{encode_path_param(file_id)}/abort",
            method="POST",
            params={
                "uploadId": upload_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    def delete_nnue_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[OkResponse]:
        """
        Parameters
        ----------
        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[OkResponse]
            Deleted NNUE file
        """
        _response = self._client_wrapper.httpx_client.request(
            f"api/nnue/files/{encode_path_param(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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


class AsyncRawNnueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_nnue_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[ListNnueFilesResponse]:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[ListNnueFilesResponse]
            List NNUE files
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/nnue/files",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    ListNnueFilesResponse,
                    parse_obj_as(
                        type_=ListNnueFilesResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def initialize_nnue_upload(
        self,
        *,
        original_filename: str,
        size_bytes: int,
        sha256hex: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[InitializeNnueUploadResponse]:
        """
        Parameters
        ----------
        original_filename : str

        size_bytes : int

        sha256hex : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[InitializeNnueUploadResponse]
            Initialized NNUE upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            "api/nnue/uploads/init",
            method="POST",
            json={
                "originalFilename": original_filename,
                "sizeBytes": size_bytes,
                "sha256Hex": sha256hex,
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
                    InitializeNnueUploadResponse,
                    parse_obj_as(
                        type_=InitializeNnueUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 400:
                raise BadRequestError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 409:
                raise ConflictError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def upload_nnue_part(
        self, file_id: str, part_number: int, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[UploadNnuePartResponse]:
        """
        Parameters
        ----------
        file_id : str

        part_number : int

        upload_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadNnuePartResponse]
            Uploaded NNUE part
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nnue/uploads/{encode_path_param(file_id)}/parts/{encode_path_param(part_number)}",
            method="PUT",
            params={
                "uploadId": upload_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadNnuePartResponse,
                    parse_obj_as(
                        type_=UploadNnuePartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def complete_nnue_upload(
        self,
        file_id: str,
        *,
        upload_id: str,
        parts: typing.Sequence[CompleteNnueUploadRequestPartsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompleteNnueUploadResponse]:
        """
        Parameters
        ----------
        file_id : str

        upload_id : str

        parts : typing.Sequence[CompleteNnueUploadRequestPartsItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompleteNnueUploadResponse]
            Completed NNUE upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nnue/uploads/{encode_path_param(file_id)}/complete",
            method="POST",
            json={
                "uploadId": upload_id,
                "parts": convert_and_respect_annotation_metadata(
                    object_=parts, annotation=typing.Sequence[CompleteNnueUploadRequestPartsItem], direction="write"
                ),
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
                    CompleteNnueUploadResponse,
                    parse_obj_as(
                        type_=CompleteNnueUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def abort_nnue_upload(
        self, file_id: str, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """
        Parameters
        ----------
        file_id : str

        upload_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            Aborted NNUE upload
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nnue/uploads/{encode_path_param(file_id)}/abort",
            method="POST",
            params={
                "uploadId": upload_id,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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

    async def delete_nnue_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[OkResponse]:
        """
        Parameters
        ----------
        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[OkResponse]
            Deleted NNUE file
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"api/nnue/files/{encode_path_param(file_id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    OkResponse,
                    parse_obj_as(
                        type_=OkResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 401:
                raise UnauthorizedError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 503:
                raise ServiceUnavailableError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        ApiErrorResponse,
                        parse_obj_as(
                            type_=ApiErrorResponse,
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
