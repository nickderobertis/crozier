

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawUploadsClient, RawUploadsClient
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


class UploadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadsClient
        """
        return self._raw_client

    def create_upload(
        self,
        *,
        type: CreateUploadRequestType,
        file: typing.Optional[typing.Any] = OMIT,
        synchronous: typing.Optional[bool] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUploadResponse:
        """
        Parameters
        ----------
        type : CreateUploadRequestType

        file : typing.Optional[typing.Any]

        synchronous : typing.Optional[bool]
            Use this flag to return an id and url

        user_id : typing.Optional[int]
            required if uploading an avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUploadResponse
            file uploaded

        Examples
        --------
        from fern.uploads import CreateUploadRequestType

        from fern import FernApi

        client = FernApi()
        client.uploads.create_upload(
            type=CreateUploadRequestType.AVATAR,
        )
        """
        _response = self._raw_client.create_upload(
            type=type, file=file, synchronous=synchronous, user_id=user_id, request_options=request_options
        )
        return _response.data

    def abort_multipart(
        self, *, external_upload_identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AbortMultipartResponse:
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
        AbortMultipartResponse
            external upload initialized

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.uploads.abort_multipart(
            external_upload_identifier="84x83tmxy398t3y._Q_z8CoJYVr69bE6D7f8J6Oo0434QquLFoYdGVerWFx9X5HDEI_TP_95c34n853495x35345394.d.ghQ",
        )
        """
        _response = self._raw_client.abort_multipart(
            external_upload_identifier=external_upload_identifier, request_options=request_options
        )
        return _response.data

    def batch_presign_multipart_parts(
        self,
        *,
        part_numbers: typing.Sequence[typing.Any],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchPresignMultipartPartsResponse:
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
        part_numbers : typing.Sequence[typing.Any]
            The part numbers to generate the presigned URLs for,
            must be between 1 and 10000.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchPresignMultipartPartsResponse
            external upload initialized

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.uploads.batch_presign_multipart_parts(
            part_numbers=[1, 2, 3],
            unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
        )
        """
        _response = self._raw_client.batch_presign_multipart_parts(
            part_numbers=part_numbers, unique_identifier=unique_identifier, request_options=request_options
        )
        return _response.data

    def complete_external_upload(
        self,
        *,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = OMIT,
        for_site_setting: typing.Optional[str] = OMIT,
        pasted: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteExternalUploadResponse:
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
        CompleteExternalUploadResponse
            external upload initialized

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.uploads.complete_external_upload(
            unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
        )
        """
        _response = self._raw_client.complete_external_upload(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
            request_options=request_options,
        )
        return _response.data

    def complete_multipart(
        self,
        *,
        parts: typing.Sequence[typing.Any],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteMultipartResponse:
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
        parts : typing.Sequence[typing.Any]
            All of the part numbers and their corresponding ETags
            that have been uploaded must be provided.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompleteMultipartResponse
            external upload initialized

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.uploads.complete_multipart(
            parts=[
                {"etag": "0c376dcfcc2606f4335bbc732de93344", "part_number": 1},
                {"etag": "09ert8cfcc2606f4335bbc732de91122", "part_number": 2},
            ],
            unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
        )
        """
        _response = self._raw_client.complete_multipart(
            parts=parts, unique_identifier=unique_identifier, request_options=request_options
        )
        return _response.data

    def create_multipart_upload(
        self,
        *,
        file_name: str,
        file_size: int,
        upload_type: CreateMultipartUploadRequestUploadType,
        metadata: typing.Optional[CreateMultipartUploadRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMultipartUploadResponse:
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
        CreateMultipartUploadResponse
            external upload initialized

        Examples
        --------
        from fern.uploads import CreateMultipartUploadRequestUploadType

        from fern import FernApi

        client = FernApi()
        client.uploads.create_multipart_upload(
            file_name="IMG_2021.jpeg",
            file_size=4096,
            upload_type=CreateMultipartUploadRequestUploadType.AVATAR,
        )
        """
        _response = self._raw_client.create_multipart_upload(
            file_name=file_name,
            file_size=file_size,
            upload_type=upload_type,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    def generate_presigned_put(
        self,
        *,
        file_name: str,
        file_size: int,
        type: GeneratePresignedPutRequestType,
        metadata: typing.Optional[GeneratePresignedPutRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GeneratePresignedPutResponse:
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
        GeneratePresignedPutResponse
            external upload initialized

        Examples
        --------
        from fern.uploads import GeneratePresignedPutRequestType

        from fern import FernApi

        client = FernApi()
        client.uploads.generate_presigned_put(
            file_name="IMG_2021.jpeg",
            file_size=4096,
            type=GeneratePresignedPutRequestType.AVATAR,
        )
        """
        _response = self._raw_client.generate_presigned_put(
            file_name=file_name, file_size=file_size, type=type, metadata=metadata, request_options=request_options
        )
        return _response.data


class AsyncUploadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadsClient
        """
        return self._raw_client

    async def create_upload(
        self,
        *,
        type: CreateUploadRequestType,
        file: typing.Optional[typing.Any] = OMIT,
        synchronous: typing.Optional[bool] = OMIT,
        user_id: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUploadResponse:
        """
        Parameters
        ----------
        type : CreateUploadRequestType

        file : typing.Optional[typing.Any]

        synchronous : typing.Optional[bool]
            Use this flag to return an id and url

        user_id : typing.Optional[int]
            required if uploading an avatar

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUploadResponse
            file uploaded

        Examples
        --------
        import asyncio

        from fern.uploads import CreateUploadRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.create_upload(
                type=CreateUploadRequestType.AVATAR,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_upload(
            type=type, file=file, synchronous=synchronous, user_id=user_id, request_options=request_options
        )
        return _response.data

    async def abort_multipart(
        self, *, external_upload_identifier: str, request_options: typing.Optional[RequestOptions] = None
    ) -> AbortMultipartResponse:
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
        AbortMultipartResponse
            external upload initialized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.abort_multipart(
                external_upload_identifier="84x83tmxy398t3y._Q_z8CoJYVr69bE6D7f8J6Oo0434QquLFoYdGVerWFx9X5HDEI_TP_95c34n853495x35345394.d.ghQ",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort_multipart(
            external_upload_identifier=external_upload_identifier, request_options=request_options
        )
        return _response.data

    async def batch_presign_multipart_parts(
        self,
        *,
        part_numbers: typing.Sequence[typing.Any],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> BatchPresignMultipartPartsResponse:
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
        part_numbers : typing.Sequence[typing.Any]
            The part numbers to generate the presigned URLs for,
            must be between 1 and 10000.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        BatchPresignMultipartPartsResponse
            external upload initialized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.batch_presign_multipart_parts(
                part_numbers=[1, 2, 3],
                unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.batch_presign_multipart_parts(
            part_numbers=part_numbers, unique_identifier=unique_identifier, request_options=request_options
        )
        return _response.data

    async def complete_external_upload(
        self,
        *,
        unique_identifier: str,
        for_private_message: typing.Optional[str] = OMIT,
        for_site_setting: typing.Optional[str] = OMIT,
        pasted: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteExternalUploadResponse:
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
        CompleteExternalUploadResponse
            external upload initialized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.complete_external_upload(
                unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_external_upload(
            unique_identifier=unique_identifier,
            for_private_message=for_private_message,
            for_site_setting=for_site_setting,
            pasted=pasted,
            request_options=request_options,
        )
        return _response.data

    async def complete_multipart(
        self,
        *,
        parts: typing.Sequence[typing.Any],
        unique_identifier: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteMultipartResponse:
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
        parts : typing.Sequence[typing.Any]
            All of the part numbers and their corresponding ETags
            that have been uploaded must be provided.

        unique_identifier : str
            The unique identifier returned in the original /create-multipart
            request.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CompleteMultipartResponse
            external upload initialized

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.complete_multipart(
                parts=[
                    {"etag": "0c376dcfcc2606f4335bbc732de93344", "part_number": 1},
                    {"etag": "09ert8cfcc2606f4335bbc732de91122", "part_number": 2},
                ],
                unique_identifier="66e86218-80d9-4bda-b4d5-2b6def968705",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_multipart(
            parts=parts, unique_identifier=unique_identifier, request_options=request_options
        )
        return _response.data

    async def create_multipart_upload(
        self,
        *,
        file_name: str,
        file_size: int,
        upload_type: CreateMultipartUploadRequestUploadType,
        metadata: typing.Optional[CreateMultipartUploadRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateMultipartUploadResponse:
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
        CreateMultipartUploadResponse
            external upload initialized

        Examples
        --------
        import asyncio

        from fern.uploads import CreateMultipartUploadRequestUploadType

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.create_multipart_upload(
                file_name="IMG_2021.jpeg",
                file_size=4096,
                upload_type=CreateMultipartUploadRequestUploadType.AVATAR,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.create_multipart_upload(
            file_name=file_name,
            file_size=file_size,
            upload_type=upload_type,
            metadata=metadata,
            request_options=request_options,
        )
        return _response.data

    async def generate_presigned_put(
        self,
        *,
        file_name: str,
        file_size: int,
        type: GeneratePresignedPutRequestType,
        metadata: typing.Optional[GeneratePresignedPutRequestMetadata] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GeneratePresignedPutResponse:
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
        GeneratePresignedPutResponse
            external upload initialized

        Examples
        --------
        import asyncio

        from fern.uploads import GeneratePresignedPutRequestType

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.uploads.generate_presigned_put(
                file_name="IMG_2021.jpeg",
                file_size=4096,
                type=GeneratePresignedPutRequestType.AVATAR,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.generate_presigned_put(
            file_name=file_name, file_size=file_size, type=type, metadata=metadata, request_options=request_options
        )
        return _response.data
