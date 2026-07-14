

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.abort_multipart_response import AbortMultipartResponse
from .types.batch_presign_multipart_parts_response import BatchPresignMultipartPartsResponse
from .types.complete_external_upload_response import CompleteExternalUploadResponse
from .types.complete_multipart_response import CompleteMultipartResponse
from .types.create_multipart_upload_request_metadata import CreateMultipartUploadRequestMetadata
from .types.create_multipart_upload_request_upload_type import CreateMultipartUploadRequestUploadType
from .types.create_multipart_upload_response import CreateMultipartUploadResponse
from .types.create_upload_request_type import CreateUploadRequestType
from .types.create_upload_response import CreateUploadResponse
from .types.generate_presigned_put_request_metadata import GeneratePresignedPutRequestMetadata
from .types.generate_presigned_put_request_type import GeneratePresignedPutRequestType
from .types.generate_presigned_put_response import GeneratePresignedPutResponse


OMIT = typing.cast(typing.Any, ...)


class RawUploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def create_upload(
        self,
        *,
        type: CreateUploadRequestType,
        file: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        synchronous: typing.Optional[bool] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateUploadResponse]:
        """
        Parameters
        ----------
        type : CreateUploadRequestType

        file : typing.Optional[typing.Optional[typing.Any]]

        synchronous : typing.Optional[bool]
            Use this flag to return an id and url

        user_id : typing.Optional[int]
            required if uploading an avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateUploadResponse]
            file uploaded
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads.json",
            method="POST",
            data={
                "file": file,
                "synchronous": synchronous,
                "type": type,
                "user_id": user_id,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateUploadResponse,
                    parse_obj_as(
                        type_=CreateUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def abort_multipart(
        self, *, external_upload_identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[AbortMultipartResponse]:
        """
        This endpoint aborts the multipart upload initiated with /create-multipart.
        This should be used when cancelling the upload. It does not matter if parts
        were already uploaded into the external storage provider.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        external_upload_identifier : str
            The identifier of the multipart upload in the external
            storage provider. This is the multipart upload_id in AWS S3.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[AbortMultipartResponse]
            external upload initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/abort-multipart.json",
            method="POST",
            json={
                "external_upload_identifier": external_upload_identifier,
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
                    AbortMultipartResponse,
                    parse_obj_as(
                        type_=AbortMultipartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def batch_presign_multipart_parts(
        self,
        *,
        part_numbers: typing.Sequence[typing.Optional[typing.Any]],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[BatchPresignMultipartPartsResponse]:
        """
        Multipart uploads are uploaded in chunks or parts to individual presigned
        URLs, similar to the one generated by /generate-presigned-put. The part
        numbers provided must be between 1 and 10000. The total number of parts
        will depend on the chunk size in bytes that you intend to use to upload
        each chunk. For example a 12MB file may have 2 5MB chunks and a final
        2MB chunk, for part numbers 1, 2, and 3.

        This endpoint will return a presigned URL for each part number provided,
        which you can then use to send PUT requests for the binary chunk corresponding
        to that part. When the part is uploaded, the provider should return an
        ETag for the part, and this should be stored along with the part number,
        because this is needed to complete the multipart upload.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        part_numbers : typing.Sequence[typing.Optional[typing.Any]]
            The part numbers to generate the presigned URLs for,
            must be between 1 and 10000.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[BatchPresignMultipartPartsResponse]
            external upload initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/batch-presign-multipart-parts.json",
            method="POST",
            json={
                "part_numbers": part_numbers,
                "unique_identifier": unique_identifier,
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
                    BatchPresignMultipartPartsResponse,
                    parse_obj_as(
                        type_=BatchPresignMultipartPartsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def complete_external_upload(
        self,
        *,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = OMIT,
        for_site_setting: typing.Optional[str] = OMIT,
        pasted: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompleteExternalUploadResponse]:
        """
        Completes an external upload initialized with /get-presigned-put. The
        file will be moved from its temporary location in external storage to
        a final destination in the S3 bucket. An Upload record will also be
        created in the database in most cases.

        If a sha1-checksum was provided in the initial request it will also
        be compared with the uploaded file in storage to make sure the same
        file was uploaded. The file size will be compared for the same reason.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        unique_identifier : str
            The unique identifier returned in the original /generate-presigned-put
            request.

        for_private_message : typing.Optional[str]
            Optionally set this to true if the upload is for a
            private message.

        for_site_setting : typing.Optional[str]
            Optionally set this to true if the upload is for a
            site setting.

        pasted : typing.Optional[str]
            Optionally set this to true if the upload was pasted
            into the upload area. This will convert PNG files to JPEG.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompleteExternalUploadResponse]
            external upload initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/complete-external-upload.json",
            method="POST",
            json={
                "for_private_message": for_private_message,
                "for_site_setting": for_site_setting,
                "pasted": pasted,
                "unique_identifier": unique_identifier,
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
                    CompleteExternalUploadResponse,
                    parse_obj_as(
                        type_=CompleteExternalUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def complete_multipart(
        self,
        *,
        parts: typing.Sequence[typing.Optional[typing.Any]],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CompleteMultipartResponse]:
        """
        Completes the multipart upload in the external store, and copies the
        file from its temporary location to its final location in the store.
        All of the parts must have been uploaded to the external storage provider.
        An Upload record will be completed in most cases once the file is copied
        to its final location.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        parts : typing.Sequence[typing.Optional[typing.Any]]
            All of the part numbers and their corresponding ETags
            that have been uploaded must be provided.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CompleteMultipartResponse]
            external upload initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/complete-multipart.json",
            method="POST",
            json={
                "parts": parts,
                "unique_identifier": unique_identifier,
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
                    CompleteMultipartResponse,
                    parse_obj_as(
                        type_=CompleteMultipartResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def create_multipart_upload(
        self,
        *,
        file_name: str,
        file_size: int,
        upload_type: CreateMultipartUploadRequestUploadType,
        metadata: typing.Optional[CreateMultipartUploadRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[CreateMultipartUploadResponse]:
        """
        Creates a multipart upload in the external storage provider, storing
        a temporary reference to the external upload similar to /get-presigned-put.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        file_name : str

        file_size : int
            File size should be represented in bytes.

        upload_type : CreateMultipartUploadRequestUploadType

        metadata : typing.Optional[CreateMultipartUploadRequestMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[CreateMultipartUploadResponse]
            external upload initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/create-multipart.json",
            method="POST",
            json={
                "file_name": file_name,
                "file_size": file_size,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=CreateMultipartUploadRequestMetadata, direction="write"
                ),
                "upload_type": upload_type,
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
                    CreateMultipartUploadResponse,
                    parse_obj_as(
                        type_=CreateMultipartUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def generate_presigned_put(
        self,
        *,
        file_name: str,
        file_size: int,
        type: GeneratePresignedPutRequestType,
        metadata: typing.Optional[GeneratePresignedPutRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[GeneratePresignedPutResponse]:
        """
        Direct external uploads bypass the usual method of creating uploads
        via the POST /uploads route, and upload directly to an external provider,
        which by default is S3. This route begins the process, and will return
        a unique identifier for the external upload as well as a presigned URL
        which is where the file binary blob should be uploaded to.

        Once the upload is complete to the external service, you must call the
        POST /complete-external-upload route using the unique identifier returned
        by this route, which will create any required Upload record in the Discourse
        database and also move file from its temporary location to the final
        destination in the external storage service.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        file_name : str

        file_size : int
            File size should be represented in bytes.

        type : GeneratePresignedPutRequestType

        metadata : typing.Optional[GeneratePresignedPutRequestMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[GeneratePresignedPutResponse]
            external upload initialized
        """
        _response = self._client_wrapper.httpx_client.request(
            "uploads/generate-presigned-put.json",
            method="POST",
            json={
                "file_name": file_name,
                "file_size": file_size,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=GeneratePresignedPutRequestMetadata, direction="write"
                ),
                "type": type,
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
                    GeneratePresignedPutResponse,
                    parse_obj_as(
                        type_=GeneratePresignedPutResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawUploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def create_upload(
        self,
        *,
        type: CreateUploadRequestType,
        file: typing.Optional[typing.Optional[typing.Any]] = OMIT,
        synchronous: typing.Optional[bool] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateUploadResponse]:
        """
        Parameters
        ----------
        type : CreateUploadRequestType

        file : typing.Optional[typing.Optional[typing.Any]]

        synchronous : typing.Optional[bool]
            Use this flag to return an id and url

        user_id : typing.Optional[int]
            required if uploading an avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateUploadResponse]
            file uploaded
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads.json",
            method="POST",
            data={
                "file": file,
                "synchronous": synchronous,
                "type": type,
                "user_id": user_id,
            },
            files={},
            request_options=request_options,
            omit=OMIT,
            force_multipart=True,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    CreateUploadResponse,
                    parse_obj_as(
                        type_=CreateUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def abort_multipart(
        self, *, external_upload_identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[AbortMultipartResponse]:
        """
        This endpoint aborts the multipart upload initiated with /create-multipart.
        This should be used when cancelling the upload. It does not matter if parts
        were already uploaded into the external storage provider.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        external_upload_identifier : str
            The identifier of the multipart upload in the external
            storage provider. This is the multipart upload_id in AWS S3.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[AbortMultipartResponse]
            external upload initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/abort-multipart.json",
            method="POST",
            json={
                "external_upload_identifier": external_upload_identifier,
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
                    AbortMultipartResponse,
                    parse_obj_as(
                        type_=AbortMultipartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def batch_presign_multipart_parts(
        self,
        *,
        part_numbers: typing.Sequence[typing.Optional[typing.Any]],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[BatchPresignMultipartPartsResponse]:
        """
        Multipart uploads are uploaded in chunks or parts to individual presigned
        URLs, similar to the one generated by /generate-presigned-put. The part
        numbers provided must be between 1 and 10000. The total number of parts
        will depend on the chunk size in bytes that you intend to use to upload
        each chunk. For example a 12MB file may have 2 5MB chunks and a final
        2MB chunk, for part numbers 1, 2, and 3.

        This endpoint will return a presigned URL for each part number provided,
        which you can then use to send PUT requests for the binary chunk corresponding
        to that part. When the part is uploaded, the provider should return an
        ETag for the part, and this should be stored along with the part number,
        because this is needed to complete the multipart upload.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        part_numbers : typing.Sequence[typing.Optional[typing.Any]]
            The part numbers to generate the presigned URLs for,
            must be between 1 and 10000.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[BatchPresignMultipartPartsResponse]
            external upload initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/batch-presign-multipart-parts.json",
            method="POST",
            json={
                "part_numbers": part_numbers,
                "unique_identifier": unique_identifier,
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
                    BatchPresignMultipartPartsResponse,
                    parse_obj_as(
                        type_=BatchPresignMultipartPartsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def complete_external_upload(
        self,
        *,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = OMIT,
        for_site_setting: typing.Optional[str] = OMIT,
        pasted: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompleteExternalUploadResponse]:
        """
        Completes an external upload initialized with /get-presigned-put. The
        file will be moved from its temporary location in external storage to
        a final destination in the S3 bucket. An Upload record will also be
        created in the database in most cases.

        If a sha1-checksum was provided in the initial request it will also
        be compared with the uploaded file in storage to make sure the same
        file was uploaded. The file size will be compared for the same reason.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        unique_identifier : str
            The unique identifier returned in the original /generate-presigned-put
            request.

        for_private_message : typing.Optional[str]
            Optionally set this to true if the upload is for a
            private message.

        for_site_setting : typing.Optional[str]
            Optionally set this to true if the upload is for a
            site setting.

        pasted : typing.Optional[str]
            Optionally set this to true if the upload was pasted
            into the upload area. This will convert PNG files to JPEG.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompleteExternalUploadResponse]
            external upload initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/complete-external-upload.json",
            method="POST",
            json={
                "for_private_message": for_private_message,
                "for_site_setting": for_site_setting,
                "pasted": pasted,
                "unique_identifier": unique_identifier,
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
                    CompleteExternalUploadResponse,
                    parse_obj_as(
                        type_=CompleteExternalUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def complete_multipart(
        self,
        *,
        parts: typing.Sequence[typing.Optional[typing.Any]],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CompleteMultipartResponse]:
        """
        Completes the multipart upload in the external store, and copies the
        file from its temporary location to its final location in the store.
        All of the parts must have been uploaded to the external storage provider.
        An Upload record will be completed in most cases once the file is copied
        to its final location.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        parts : typing.Sequence[typing.Optional[typing.Any]]
            All of the part numbers and their corresponding ETags
            that have been uploaded must be provided.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CompleteMultipartResponse]
            external upload initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/complete-multipart.json",
            method="POST",
            json={
                "parts": parts,
                "unique_identifier": unique_identifier,
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
                    CompleteMultipartResponse,
                    parse_obj_as(
                        type_=CompleteMultipartResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def create_multipart_upload(
        self,
        *,
        file_name: str,
        file_size: int,
        upload_type: CreateMultipartUploadRequestUploadType,
        metadata: typing.Optional[CreateMultipartUploadRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[CreateMultipartUploadResponse]:
        """
        Creates a multipart upload in the external storage provider, storing
        a temporary reference to the external upload similar to /get-presigned-put.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        file_name : str

        file_size : int
            File size should be represented in bytes.

        upload_type : CreateMultipartUploadRequestUploadType

        metadata : typing.Optional[CreateMultipartUploadRequestMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[CreateMultipartUploadResponse]
            external upload initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/create-multipart.json",
            method="POST",
            json={
                "file_name": file_name,
                "file_size": file_size,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=CreateMultipartUploadRequestMetadata, direction="write"
                ),
                "upload_type": upload_type,
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
                    CreateMultipartUploadResponse,
                    parse_obj_as(
                        type_=CreateMultipartUploadResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def generate_presigned_put(
        self,
        *,
        file_name: str,
        file_size: int,
        type: GeneratePresignedPutRequestType,
        metadata: typing.Optional[GeneratePresignedPutRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[GeneratePresignedPutResponse]:
        """
        Direct external uploads bypass the usual method of creating uploads
        via the POST /uploads route, and upload directly to an external provider,
        which by default is S3. This route begins the process, and will return
        a unique identifier for the external upload as well as a presigned URL
        which is where the file binary blob should be uploaded to.

        Once the upload is complete to the external service, you must call the
        POST /complete-external-upload route using the unique identifier returned
        by this route, which will create any required Upload record in the Discourse
        database and also move file from its temporary location to the final
        destination in the external storage service.

        You must have the correct permissions and CORS settings configured in your
        external provider. We support AWS S3 as the default. See:

        https://meta.discourse.org/t/-/210469#s3-multipart-direct-uploads-4.

        An external file store must be set up and `enable_direct_s3_uploads` must
        be set to true for this endpoint to function.

        Parameters
        ----------
        file_name : str

        file_size : int
            File size should be represented in bytes.

        type : GeneratePresignedPutRequestType

        metadata : typing.Optional[GeneratePresignedPutRequestMetadata]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[GeneratePresignedPutResponse]
            external upload initialized
        """
        _response = await self._client_wrapper.httpx_client.request(
            "uploads/generate-presigned-put.json",
            method="POST",
            json={
                "file_name": file_name,
                "file_size": file_size,
                "metadata": convert_and_respect_annotation_metadata(
                    object_=metadata, annotation=GeneratePresignedPutRequestMetadata, direction="write"
                ),
                "type": type,
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
                    GeneratePresignedPutResponse,
                    parse_obj_as(
                        type_=GeneratePresignedPutResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
