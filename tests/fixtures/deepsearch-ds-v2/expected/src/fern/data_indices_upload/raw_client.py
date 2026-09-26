

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
from ..errors.unprocessable_entity_error import UnprocessableEntityError
from ..types.api_server_fastapi_server_public_models_data_indices_upload_models_http_source import (
    ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource,
)
from ..types.attachment_upload_data import AttachmentUploadData
from ..types.cps_task import CpsTask
from ..types.document_meta import DocumentMeta
from ..types.http_validation_error import HttpValidationError
from ..types.s3document_source import S3DocumentSource
from ..types.target_conversion_parameters import TargetConversionParameters
from .types.convert_documents_request_body_conversion_settings import ConvertDocumentsRequestBodyConversionSettings
from .types.convert_documents_request_body_without_operations_item import (
    ConvertDocumentsRequestBodyWithoutOperationsItem,
)
from .types.convert_upload_documents_request_body_conversion_settings import (
    ConvertUploadDocumentsRequestBodyConversionSettings,
)
from .types.data_index_upload_file_source_conversion_settings import DataIndexUploadFileSourceConversionSettings
from .types.data_index_upload_file_source_urls import DataIndexUploadFileSourceUrls
from .types.upload_elastic_request_body_with_operations_item import UploadElasticRequestBodyWithOperationsItem
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawDataIndicesUploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def upload_project_data_index_file(
        self, proj_key: str, index_key: str, *, file_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[CpsTask]:
        """
        Upload a file to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/upload",
            method="POST",
            json={
                "file_url": file_url,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def upload_register_project_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CpsTask]:
        """
        Upload and register documents to be converted later.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/upload_register_documents",
            method="POST",
            json={
                "file_url": file_url,
                "http_source": convert_and_respect_annotation_metadata(
                    object_=http_source,
                    annotation=typing.Optional[
                        typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
                    ],
                    direction="write",
                ),
                "s3_source": convert_and_respect_annotation_metadata(
                    object_=s3source, annotation=typing.Optional[S3DocumentSource], direction="write"
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def load_project_data_index_files_elastic(
        self,
        proj_key: str,
        index_key: str,
        *,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        with_operations: typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CpsTask]:
        """
        Load file(s) in a project data index to elastic.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        with_operations : typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/load_elastic",
            method="POST",
            json={
                "document_hashes": document_hashes,
                "with_operations": with_operations,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def ccs_convert_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        conversion_settings: typing.Optional[ConvertDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        without_operations: typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CpsTask]:
        """
        Convert files via CCS previously registered and in a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        conversion_settings : typing.Optional[ConvertDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        without_operations : typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

        upload_to_elastic : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/ccs_convert",
            method="POST",
            json={
                "conversion_settings": convert_and_respect_annotation_metadata(
                    object_=conversion_settings,
                    annotation=typing.Optional[ConvertDocumentsRequestBodyConversionSettings],
                    direction="write",
                ),
                "target_settings": convert_and_respect_annotation_metadata(
                    object_=target_settings, annotation=typing.Optional[TargetConversionParameters], direction="write"
                ),
                "document_hashes": document_hashes,
                "without_operations": without_operations,
                "upload_to_elastic": upload_to_elastic,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def ccs_convert_upload_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        meta: typing.Optional[DocumentMeta] = OMIT,
        conversion_settings: typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CpsTask]:
        """
        Convert files via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

        upload_to_elastic : typing.Optional[bool]

        meta : typing.Optional[DocumentMeta]

        conversion_settings : typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/ccs_convert_upload",
            method="POST",
            json={
                "file_url": file_url,
                "http_source": convert_and_respect_annotation_metadata(
                    object_=http_source,
                    annotation=typing.Optional[
                        typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
                    ],
                    direction="write",
                ),
                "s3_source": convert_and_respect_annotation_metadata(
                    object_=s3source, annotation=typing.Optional[S3DocumentSource], direction="write"
                ),
                "upload_to_elastic": upload_to_elastic,
                "meta": convert_and_respect_annotation_metadata(
                    object_=meta, annotation=typing.Optional[DocumentMeta], direction="write"
                ),
                "conversion_settings": convert_and_respect_annotation_metadata(
                    object_=conversion_settings,
                    annotation=typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings],
                    direction="write",
                ),
                "target_settings": convert_and_respect_annotation_metadata(
                    object_=target_settings, annotation=typing.Optional[TargetConversionParameters], direction="write"
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def html_print_convert_upload(
        self,
        proj_key: str,
        index_key: str,
        *,
        urls: DataIndexUploadFileSourceUrls,
        conversion_settings: typing.Optional[DataIndexUploadFileSourceConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CpsTask]:
        """
        Convert a list of HTML pages to PDF, convert them via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        urls : DataIndexUploadFileSourceUrls
            List of URLs to be printed to PDF, converted and uploaded to the data index.

        conversion_settings : typing.Optional[DataIndexUploadFileSourceConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        headers : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CpsTask]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/html_print_convert_upload",
            method="POST",
            json={
                "conversion_settings": convert_and_respect_annotation_metadata(
                    object_=conversion_settings,
                    annotation=typing.Optional[DataIndexUploadFileSourceConversionSettings],
                    direction="write",
                ),
                "target_settings": convert_and_respect_annotation_metadata(
                    object_=target_settings, annotation=typing.Optional[TargetConversionParameters], direction="write"
                ),
                "urls": convert_and_respect_annotation_metadata(
                    object_=urls, annotation=DataIndexUploadFileSourceUrls, direction="write"
                ),
                "headers": headers,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def get_attachment_upload_data(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[AttachmentUploadData]:
        """
        Get url and path to upload an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AttachmentUploadData]
            Successful Response
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(index_item_id)}/attachment_url/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttachmentUploadData,
                    parse_obj_as(
                        type_=AttachmentUploadData,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    def register_attachment(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        *,
        attachment_path: str,
        attachment_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[None]:
        """
        Notify upload completion of an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        attachment_path : str

        attachment_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[None]
        """
        _response = self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(index_item_id)}/attachment",
            method="POST",
            json={
                "attachment_path": attachment_path,
                "attachment_key": attachment_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return HttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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


class AsyncRawDataIndicesUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def upload_project_data_index_file(
        self, proj_key: str, index_key: str, *, file_url: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Upload a file to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/upload",
            method="POST",
            json={
                "file_url": file_url,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def upload_register_project_documents(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Upload and register documents to be converted later.

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/upload_register_documents",
            method="POST",
            json={
                "file_url": file_url,
                "http_source": convert_and_respect_annotation_metadata(
                    object_=http_source,
                    annotation=typing.Optional[
                        typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
                    ],
                    direction="write",
                ),
                "s3_source": convert_and_respect_annotation_metadata(
                    object_=s3source, annotation=typing.Optional[S3DocumentSource], direction="write"
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def load_project_data_index_files_elastic(
        self,
        proj_key: str,
        index_key: str,
        *,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        with_operations: typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Load file(s) in a project data index to elastic.

        Parameters
        ----------
        proj_key : str

        index_key : str

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        with_operations : typing.Optional[typing.Sequence[UploadElasticRequestBodyWithOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/load_elastic",
            method="POST",
            json={
                "document_hashes": document_hashes,
                "with_operations": with_operations,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def ccs_convert_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        conversion_settings: typing.Optional[ConvertDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        document_hashes: typing.Optional[typing.Sequence[str]] = OMIT,
        without_operations: typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Convert files via CCS previously registered and in a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        conversion_settings : typing.Optional[ConvertDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        document_hashes : typing.Optional[typing.Sequence[str]]
            List of document hashes to be used as filter.

        without_operations : typing.Optional[typing.Sequence[ConvertDocumentsRequestBodyWithoutOperationsItem]]
            List of Operation Status documents don't have to be used as filter.

        upload_to_elastic : typing.Optional[bool]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/ccs_convert",
            method="POST",
            json={
                "conversion_settings": convert_and_respect_annotation_metadata(
                    object_=conversion_settings,
                    annotation=typing.Optional[ConvertDocumentsRequestBodyConversionSettings],
                    direction="write",
                ),
                "target_settings": convert_and_respect_annotation_metadata(
                    object_=target_settings, annotation=typing.Optional[TargetConversionParameters], direction="write"
                ),
                "document_hashes": document_hashes,
                "without_operations": without_operations,
                "upload_to_elastic": upload_to_elastic,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def ccs_convert_upload_file_project_data_index(
        self,
        proj_key: str,
        index_key: str,
        *,
        file_url: typing.Optional[typing.Sequence[str]] = OMIT,
        http_source: typing.Optional[
            typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
        ] = OMIT,
        s3source: typing.Optional[S3DocumentSource] = OMIT,
        upload_to_elastic: typing.Optional[bool] = OMIT,
        meta: typing.Optional[DocumentMeta] = OMIT,
        conversion_settings: typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Convert files via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        file_url : typing.Optional[typing.Sequence[str]]
            List of File's URL to be converted and uploaded to the data index.

        http_source : typing.Optional[typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]]
            List of Internal File's URLs to be converted and uploaded to the data index.

        s3source : typing.Optional[S3DocumentSource]
            Coordinates to object store to get files to convert. Can specify which files with object keys.

        upload_to_elastic : typing.Optional[bool]

        meta : typing.Optional[DocumentMeta]

        conversion_settings : typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/ccs_convert_upload",
            method="POST",
            json={
                "file_url": file_url,
                "http_source": convert_and_respect_annotation_metadata(
                    object_=http_source,
                    annotation=typing.Optional[
                        typing.Sequence[ApiServerFastapiServerPublicModelsDataIndicesUploadModelsHttpSource]
                    ],
                    direction="write",
                ),
                "s3_source": convert_and_respect_annotation_metadata(
                    object_=s3source, annotation=typing.Optional[S3DocumentSource], direction="write"
                ),
                "upload_to_elastic": upload_to_elastic,
                "meta": convert_and_respect_annotation_metadata(
                    object_=meta, annotation=typing.Optional[DocumentMeta], direction="write"
                ),
                "conversion_settings": convert_and_respect_annotation_metadata(
                    object_=conversion_settings,
                    annotation=typing.Optional[ConvertUploadDocumentsRequestBodyConversionSettings],
                    direction="write",
                ),
                "target_settings": convert_and_respect_annotation_metadata(
                    object_=target_settings, annotation=typing.Optional[TargetConversionParameters], direction="write"
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def html_print_convert_upload(
        self,
        proj_key: str,
        index_key: str,
        *,
        urls: DataIndexUploadFileSourceUrls,
        conversion_settings: typing.Optional[DataIndexUploadFileSourceConversionSettings] = OMIT,
        target_settings: typing.Optional[TargetConversionParameters] = OMIT,
        headers: typing.Optional[typing.Dict[str, typing.Any]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CpsTask]:
        """
        Convert a list of HTML pages to PDF, convert them via CCS and upload to a project data index (only for indices with 'deepsearch-doc' schema).

        Parameters
        ----------
        proj_key : str

        index_key : str

        urls : DataIndexUploadFileSourceUrls
            List of URLs to be printed to PDF, converted and uploaded to the data index.

        conversion_settings : typing.Optional[DataIndexUploadFileSourceConversionSettings]
            Specify the conversion settings to use.

        target_settings : typing.Optional[TargetConversionParameters]
            Specify the target settings to use.

        headers : typing.Optional[typing.Dict[str, typing.Any]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CpsTask]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/actions/html_print_convert_upload",
            method="POST",
            json={
                "conversion_settings": convert_and_respect_annotation_metadata(
                    object_=conversion_settings,
                    annotation=typing.Optional[DataIndexUploadFileSourceConversionSettings],
                    direction="write",
                ),
                "target_settings": convert_and_respect_annotation_metadata(
                    object_=target_settings, annotation=typing.Optional[TargetConversionParameters], direction="write"
                ),
                "urls": convert_and_respect_annotation_metadata(
                    object_=urls, annotation=DataIndexUploadFileSourceUrls, direction="write"
                ),
                "headers": headers,
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
                    CpsTask,
                    parse_obj_as(
                        type_=CpsTask,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def get_attachment_upload_data(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        filename: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[AttachmentUploadData]:
        """
        Get url and path to upload an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        filename : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AttachmentUploadData]
            Successful Response
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(index_item_id)}/attachment_url/{encode_path_param(filename)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    AttachmentUploadData,
                    parse_obj_as(
                        type_=AttachmentUploadData,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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

    async def register_attachment(
        self,
        proj_key: str,
        index_key: str,
        index_item_id: str,
        *,
        attachment_path: str,
        attachment_key: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[None]:
        """
        Notify upload completion of an attachment to a project data index.

        Parameters
        ----------
        proj_key : str

        index_key : str

        index_item_id : str

        attachment_path : str

        attachment_key : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[None]
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"project/{encode_path_param(proj_key)}/data_indices/{encode_path_param(index_key)}/documents/{encode_path_param(index_item_id)}/attachment",
            method="POST",
            json={
                "attachment_path": attachment_path,
                "attachment_key": attachment_key,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return AsyncHttpResponse(response=_response, data=None)
            if _response.status_code == 422:
                raise UnprocessableEntityError(
                    headers=dict(_response.headers),
                    body=typing.cast(
                        HttpValidationError,
                        parse_obj_as(
                            type_=HttpValidationError,
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
