

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
from ..errors.forbidden_error import ForbiddenError
from ..errors.gone_error import GoneError
from ..errors.internal_server_error import InternalServerError
from ..errors.not_found_error import NotFoundError
from ..types.cursor_page_type_var_customized_path_meta_data_get import CursorPageTypeVarCustomizedPathMetaDataGet
from ..types.envelope_file_upload_complete_future_response import EnvelopeFileUploadCompleteFutureResponse
from ..types.envelope_file_upload_complete_response import EnvelopeFileUploadCompleteResponse
from ..types.envelope_list_dataset_meta_data import EnvelopeListDatasetMetaData
from ..types.envelope_list_file_meta_data_get import EnvelopeListFileMetaDataGet
from ..types.envelope_presigned_link import EnvelopePresignedLink
from ..types.envelope_task_get import EnvelopeTaskGet
from ..types.enveloped_error import EnvelopedError
from ..types.file_location import FileLocation
from ..types.file_upload_completion_body import FileUploadCompletionBody
from ..types.link_type import LinkType
from ..types.search_filters import SearchFilters
from ..types.upload_file_request_file_size import UploadFileRequestFileSize
from .types.get_file_metadata_response import GetFileMetadataResponse
from .types.upload_file_response import UploadFileResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawStorageClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_storage_locations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[typing.List[FileLocation]]:
        """
        Get available storage locations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[typing.List[FileLocation]]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            "v0/storage/locations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileLocation],
                    parse_obj_as(
                        type_=typing.List[FileLocation],
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

    def list_storage_paths(
        self,
        location_id: int,
        *,
        size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        file_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CursorPageTypeVarCustomizedPathMetaDataGet]:
        """
        Lists the files/directories in WorkingDirectory

        Parameters
        ----------
        location_id : int

        size : typing.Optional[int]

        cursor : typing.Optional[str]

        file_filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CursorPageTypeVarCustomizedPathMetaDataGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/paths",
            method="GET",
            params={
                "size": size,
                "cursor": cursor,
                "fileFilter": file_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CursorPageTypeVarCustomizedPathMetaDataGet,
                    parse_obj_as(
                        type_=CursorPageTypeVarCustomizedPathMetaDataGet,
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

    def compute_path_size(
        self, location_id: int, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Compute the size of a path

        Parameters
        ----------
        location_id : int

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/paths/{encode_path_param(path)}:size",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    def batch_delete_paths(
        self,
        location_id: int,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Deletes Paths

        Parameters
        ----------
        location_id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/-/paths:batchDelete",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    def list_datasets_metadata(
        self, location_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeListDatasetMetaData]:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListDatasetMetaData]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListDatasetMetaData,
                    parse_obj_as(
                        type_=EnvelopeListDatasetMetaData,
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

    def get_files_metadata(
        self,
        location_id: int,
        *,
        uuid_filter: typing.Optional[str] = None,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListDatasetMetaData]:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        uuid_filter : typing.Optional[str]

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListDatasetMetaData]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/metadata",
            method="GET",
            params={
                "uuid_filter": uuid_filter,
                "expand_dirs": expand_dirs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListDatasetMetaData,
                    parse_obj_as(
                        type_=EnvelopeListDatasetMetaData,
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

    def list_dataset_files_metadata(
        self,
        location_id: int,
        dataset_id: str,
        *,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeListFileMetaDataGet]:
        """
        Get Files Metadata

        Parameters
        ----------
        location_id : int

        dataset_id : str

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeListFileMetaDataGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/datasets/{encode_path_param(dataset_id)}/metadata",
            method="GET",
            params={
                "expand_dirs": expand_dirs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListFileMetaDataGet,
                    parse_obj_as(
                        type_=EnvelopeListFileMetaDataGet,
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

    def get_file_metadata(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[GetFileMetadataResponse]:
        """
        Get File Metadata

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GetFileMetadataResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFileMetadataResponse,
                    parse_obj_as(
                        type_=GetFileMetadataResponse,
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

    def download_file(
        self,
        location_id: int,
        file_id: str,
        *,
        link_type: typing.Optional[LinkType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopePresignedLink]:
        """
        Returns download link for requested file

        Parameters
        ----------
        location_id : int

        file_id : str

        link_type : typing.Optional[LinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopePresignedLink]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "link_type": link_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePresignedLink,
                    parse_obj_as(
                        type_=EnvelopePresignedLink,
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

    def upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        file_size: typing.Optional[UploadFileRequestFileSize] = None,
        link_type: typing.Optional[LinkType] = None,
        is_directory: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[UploadFileResponse]:
        """
        Returns upload link

        Parameters
        ----------
        location_id : int

        file_id : str

        file_size : typing.Optional[UploadFileRequestFileSize]

        link_type : typing.Optional[LinkType]

        is_directory : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[UploadFileResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}",
            method="PUT",
            params={
                "file_size": file_size,
                "link_type": link_type,
                "is_directory": is_directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadFileResponse,
                    parse_obj_as(
                        type_=UploadFileResponse,
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

    def delete_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        Deletes File

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}",
            method="DELETE",
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

    def abort_upload_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[None]:
        """
        aborts an upload if user has the rights to, and reverts
        to the latest version if available, else will delete the file

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}:abort",
            method="POST",
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

    def complete_upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        data: typing.Optional[FileUploadCompletionBody] = OMIT,
        error: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[EnvelopeFileUploadCompleteResponse]:
        """
        completes an upload if the user has the rights to

        Parameters
        ----------
        location_id : int

        file_id : str

        data : typing.Optional[FileUploadCompletionBody]

        error : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeFileUploadCompleteResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}:complete",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Optional[FileUploadCompletionBody], direction="write"
                ),
                "error": error,
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
                    EnvelopeFileUploadCompleteResponse,
                    parse_obj_as(
                        type_=EnvelopeFileUploadCompleteResponse,
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

    def is_completed_upload_file(
        self, location_id: int, file_id: str, future_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeFileUploadCompleteFutureResponse]:
        """
        Check for upload completion

        Parameters
        ----------
        location_id : int

        file_id : str

        future_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeFileUploadCompleteFutureResponse]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}:complete/futures/{encode_path_param(future_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeFileUploadCompleteFutureResponse,
                    parse_obj_as(
                        type_=EnvelopeFileUploadCompleteFutureResponse,
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

    def export_data(
        self, location_id: int, *, paths: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Export data

        Parameters
        ----------
        location_id : int

        paths : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}:export-data",
            method="POST",
            json={
                "paths": paths,
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
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
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

    def search(
        self, location_id: int, *, filters: SearchFilters, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[EnvelopeTaskGet]:
        """
        Starts a files/folders search

        Parameters
        ----------
        location_id : int

        filters : SearchFilters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}:search",
            method="POST",
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=SearchFilters, direction="write"
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
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
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


class AsyncRawStorageClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_storage_locations(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[typing.List[FileLocation]]:
        """
        Get available storage locations

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[typing.List[FileLocation]]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            "v0/storage/locations",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    typing.List[FileLocation],
                    parse_obj_as(
                        type_=typing.List[FileLocation],
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

    async def list_storage_paths(
        self,
        location_id: int,
        *,
        size: typing.Optional[int] = None,
        cursor: typing.Optional[str] = None,
        file_filter: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CursorPageTypeVarCustomizedPathMetaDataGet]:
        """
        Lists the files/directories in WorkingDirectory

        Parameters
        ----------
        location_id : int

        size : typing.Optional[int]

        cursor : typing.Optional[str]

        file_filter : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CursorPageTypeVarCustomizedPathMetaDataGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/paths",
            method="GET",
            params={
                "size": size,
                "cursor": cursor,
                "fileFilter": file_filter,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CursorPageTypeVarCustomizedPathMetaDataGet,
                    parse_obj_as(
                        type_=CursorPageTypeVarCustomizedPathMetaDataGet,
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

    async def compute_path_size(
        self, location_id: int, path: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Compute the size of a path

        Parameters
        ----------
        location_id : int

        path : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/paths/{encode_path_param(path)}:size",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    async def batch_delete_paths(
        self,
        location_id: int,
        *,
        request: typing.Sequence[str],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Deletes Paths

        Parameters
        ----------
        location_id : int

        request : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/-/paths:batchDelete",
            method="POST",
            json=request,
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
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

    async def list_datasets_metadata(
        self, location_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeListDatasetMetaData]:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListDatasetMetaData]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/datasets",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListDatasetMetaData,
                    parse_obj_as(
                        type_=EnvelopeListDatasetMetaData,
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

    async def get_files_metadata(
        self,
        location_id: int,
        *,
        uuid_filter: typing.Optional[str] = None,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListDatasetMetaData]:
        """
        Get datasets metadata

        Parameters
        ----------
        location_id : int

        uuid_filter : typing.Optional[str]

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListDatasetMetaData]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/metadata",
            method="GET",
            params={
                "uuid_filter": uuid_filter,
                "expand_dirs": expand_dirs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListDatasetMetaData,
                    parse_obj_as(
                        type_=EnvelopeListDatasetMetaData,
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

    async def list_dataset_files_metadata(
        self,
        location_id: int,
        dataset_id: str,
        *,
        expand_dirs: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeListFileMetaDataGet]:
        """
        Get Files Metadata

        Parameters
        ----------
        location_id : int

        dataset_id : str

        expand_dirs : typing.Optional[bool]
            Automatic directory expansion. This will be replaced by pagination the future

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeListFileMetaDataGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/datasets/{encode_path_param(dataset_id)}/metadata",
            method="GET",
            params={
                "expand_dirs": expand_dirs,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeListFileMetaDataGet,
                    parse_obj_as(
                        type_=EnvelopeListFileMetaDataGet,
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

    async def get_file_metadata(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[GetFileMetadataResponse]:
        """
        Get File Metadata

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GetFileMetadataResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}/metadata",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    GetFileMetadataResponse,
                    parse_obj_as(
                        type_=GetFileMetadataResponse,
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

    async def download_file(
        self,
        location_id: int,
        file_id: str,
        *,
        link_type: typing.Optional[LinkType] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopePresignedLink]:
        """
        Returns download link for requested file

        Parameters
        ----------
        location_id : int

        file_id : str

        link_type : typing.Optional[LinkType]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopePresignedLink]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}",
            method="GET",
            params={
                "link_type": link_type,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopePresignedLink,
                    parse_obj_as(
                        type_=EnvelopePresignedLink,
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

    async def upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        file_size: typing.Optional[UploadFileRequestFileSize] = None,
        link_type: typing.Optional[LinkType] = None,
        is_directory: typing.Optional[bool] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[UploadFileResponse]:
        """
        Returns upload link

        Parameters
        ----------
        location_id : int

        file_id : str

        file_size : typing.Optional[UploadFileRequestFileSize]

        link_type : typing.Optional[LinkType]

        is_directory : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[UploadFileResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}",
            method="PUT",
            params={
                "file_size": file_size,
                "link_type": link_type,
                "is_directory": is_directory,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    UploadFileResponse,
                    parse_obj_as(
                        type_=UploadFileResponse,
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

    async def delete_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        Deletes File

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}",
            method="DELETE",
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

    async def abort_upload_file(
        self, location_id: int, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[None]:
        """
        aborts an upload if user has the rights to, and reverts
        to the latest version if available, else will delete the file

        Parameters
        ----------
        location_id : int

        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}:abort",
            method="POST",
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

    async def complete_upload_file(
        self,
        location_id: int,
        file_id: str,
        *,
        data: typing.Optional[FileUploadCompletionBody] = OMIT,
        error: typing.Optional[typing.Any] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[EnvelopeFileUploadCompleteResponse]:
        """
        completes an upload if the user has the rights to

        Parameters
        ----------
        location_id : int

        file_id : str

        data : typing.Optional[FileUploadCompletionBody]

        error : typing.Optional[typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeFileUploadCompleteResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}:complete",
            method="POST",
            json={
                "data": convert_and_respect_annotation_metadata(
                    object_=data, annotation=typing.Optional[FileUploadCompletionBody], direction="write"
                ),
                "error": error,
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
                    EnvelopeFileUploadCompleteResponse,
                    parse_obj_as(
                        type_=EnvelopeFileUploadCompleteResponse,
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

    async def is_completed_upload_file(
        self, location_id: int, file_id: str, future_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeFileUploadCompleteFutureResponse]:
        """
        Check for upload completion

        Parameters
        ----------
        location_id : int

        file_id : str

        future_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeFileUploadCompleteFutureResponse]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}/files/{encode_path_param(file_id)}:complete/futures/{encode_path_param(future_id)}",
            method="POST",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    EnvelopeFileUploadCompleteFutureResponse,
                    parse_obj_as(
                        type_=EnvelopeFileUploadCompleteFutureResponse,
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

    async def export_data(
        self, location_id: int, *, paths: typing.Sequence[str], request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Export data

        Parameters
        ----------
        location_id : int

        paths : typing.Sequence[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}:export-data",
            method="POST",
            json={
                "paths": paths,
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
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
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

    async def search(
        self, location_id: int, *, filters: SearchFilters, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[EnvelopeTaskGet]:
        """
        Starts a files/folders search

        Parameters
        ----------
        location_id : int

        filters : SearchFilters

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[EnvelopeTaskGet]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"v0/storage/locations/{encode_path_param(location_id)}:search",
            method="POST",
            json={
                "filters": convert_and_respect_annotation_metadata(
                    object_=filters, annotation=SearchFilters, direction="write"
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
                    EnvelopeTaskGet,
                    parse_obj_as(
                        type_=EnvelopeTaskGet,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 403:
                raise ForbiddenError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 404:
                raise NotFoundError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        typing.Any,
                        parse_obj_as(
                            type_=typing.Any,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 410:
                raise GoneError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
                            object_=_response.json(),
                        ),
                    ),
                )
            if _response.status_code == 500:
                raise InternalServerError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        EnvelopedError,
                        parse_obj_as(
                            type_=EnvelopedError,
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
