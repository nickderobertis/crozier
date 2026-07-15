

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.create_upload_session_response import CreateUploadSessionResponse
from ..types.delete_upload_session_response import DeleteUploadSessionResponse
from ..types.file_size import FileSize
from ..types.get_file_response import GetFileResponse
from ..types.get_upload_session_response import GetUploadSessionResponse
from ..types.parent_folder_id import ParentFolderId
from ..types.update_upload_session_response import UpdateUploadSessionResponse
from .raw_client import AsyncRawUploadSessionsClient, RawUploadSessionsClient


OMIT = typing.cast(typing.Any, ...)


class UploadSessionsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawUploadSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawUploadSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawUploadSessionsClient
        """
        return self._raw_client

    def add(
        self,
        *,
        name: str,
        parent_folder_id: ParentFolderId,
        size: FileSize,
        raw: typing.Optional[bool] = None,
        drive_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUploadSessionResponse:
        """
        Start an Upload Session. Upload sessions are used to upload large files, use the [Upload File](#operation/filesUpload) endpoint to upload smaller files (up to 100MB). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        name : str
            The name of the file.

        parent_folder_id : ParentFolderId

        size : FileSize

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        drive_id : typing.Optional[str]
            ID of the drive to upload to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUploadSessionResponse
            UploadSessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.upload_sessions.add(
            name="Documents",
            parent_folder_id="1234",
            size=1810673,
        )
        """
        _response = self._raw_client.add(
            name=name,
            parent_folder_id=parent_folder_id,
            size=size,
            raw=raw,
            drive_id=drive_id,
            request_options=request_options,
        )
        return _response.data

    def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUploadSessionResponse:
        """
        Get Upload Session. Use the `part_size` to split your file into parts. Upload the parts to the [Upload part of File](#operation/uploadSessionsUpload) endpoint. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUploadSessionResponse
            UploadSessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.upload_sessions.one(
            id="id",
            fields="id,updated_at",
        )
        """
        _response = self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    def upload(
        self,
        id: str,
        *,
        part_number: float,
        request: str,
        raw: typing.Optional[bool] = None,
        digest: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateUploadSessionResponse:
        """
        Upload part of File to Upload Session (max 100MB). Get `part_size` from [Get Upload Session](#operation/uploadSessionsOne) first. Every File part (except the last one) uploaded to this endpoint should have Content-Length equal to `part_size`. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        part_number : float
            Part number of the file part being uploaded.

        request : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        digest : typing.Optional[str]
            The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUploadSessionResponse
            UploadSessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.upload_sessions.upload(
            id="id",
            digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
            part_number=0.0,
            request="<binary string>",
        )
        """
        _response = self._raw_client.upload(
            id, part_number=part_number, request=request, raw=raw, digest=digest, request_options=request_options
        )
        return _response.data

    def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteUploadSessionResponse:
        """
        Abort Upload Session. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteUploadSessionResponse
            UploadSessions

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.upload_sessions.delete(
            id="id",
        )
        """
        _response = self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    def finish(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        digest: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFileResponse:
        """
        Finish Upload Session. Only call this endpoint after all File parts have been uploaded to [Upload part of File](#operation/uploadSessionsUpload). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        digest : typing.Optional[str]
            The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFileResponse
            File

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )
        client.upload_sessions.finish(
            id="id",
            digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
        )
        """
        _response = self._raw_client.finish(id, raw=raw, digest=digest, request_options=request_options)
        return _response.data


class AsyncUploadSessionsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawUploadSessionsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawUploadSessionsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawUploadSessionsClient
        """
        return self._raw_client

    async def add(
        self,
        *,
        name: str,
        parent_folder_id: ParentFolderId,
        size: FileSize,
        raw: typing.Optional[bool] = None,
        drive_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CreateUploadSessionResponse:
        """
        Start an Upload Session. Upload sessions are used to upload large files, use the [Upload File](#operation/filesUpload) endpoint to upload smaller files (up to 100MB). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        name : str
            The name of the file.

        parent_folder_id : ParentFolderId

        size : FileSize

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        drive_id : typing.Optional[str]
            ID of the drive to upload to.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CreateUploadSessionResponse
            UploadSessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload_sessions.add(
                name="Documents",
                parent_folder_id="1234",
                size=1810673,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.add(
            name=name,
            parent_folder_id=parent_folder_id,
            size=size,
            raw=raw,
            drive_id=drive_id,
            request_options=request_options,
        )
        return _response.data

    async def one(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        fields: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetUploadSessionResponse:
        """
        Get Upload Session. Use the `part_size` to split your file into parts. Upload the parts to the [Upload part of File](#operation/uploadSessionsUpload) endpoint. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        fields : typing.Optional[str]
            The 'fields' parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. <br /><br />Example: `fields=name,email,addresses.city`<br /><br />In the example above, the response will only include the fields "name", "email" and "addresses.city". If any other fields are available, they will be excluded.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetUploadSessionResponse
            UploadSessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload_sessions.one(
                id="id",
                fields="id,updated_at",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.one(id, raw=raw, fields=fields, request_options=request_options)
        return _response.data

    async def upload(
        self,
        id: str,
        *,
        part_number: float,
        request: str,
        raw: typing.Optional[bool] = None,
        digest: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> UpdateUploadSessionResponse:
        """
        Upload part of File to Upload Session (max 100MB). Get `part_size` from [Get Upload Session](#operation/uploadSessionsOne) first. Every File part (except the last one) uploaded to this endpoint should have Content-Length equal to `part_size`. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        part_number : float
            Part number of the file part being uploaded.

        request : str

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        digest : typing.Optional[str]
            The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        UpdateUploadSessionResponse
            UploadSessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload_sessions.upload(
                id="id",
                digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
                part_number=0.0,
                request="<binary string>",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload(
            id, part_number=part_number, request=request, raw=raw, digest=digest, request_options=request_options
        )
        return _response.data

    async def delete(
        self, id: str, *, raw: typing.Optional[bool] = None, request_options: typing.Optional[RequestOptions] = None
    ) -> DeleteUploadSessionResponse:
        """
        Abort Upload Session. Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DeleteUploadSessionResponse
            UploadSessions

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload_sessions.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete(id, raw=raw, request_options=request_options)
        return _response.data

    async def finish(
        self,
        id: str,
        *,
        raw: typing.Optional[bool] = None,
        digest: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> GetFileResponse:
        """
        Finish Upload Session. Only call this endpoint after all File parts have been uploaded to [Upload part of File](#operation/uploadSessionsUpload). Note that the base URL is upload.apideck.com instead of unify.apideck.com. For more information on uploads, refer to the [file upload guide](/guides/file-upload).

        Parameters
        ----------
        id : str
            ID of the record you are acting upon.

        raw : typing.Optional[bool]
            Include raw response. Mostly used for debugging purposes

        digest : typing.Optional[str]
            The RFC3230 message digest of the uploaded part. Only required for the Box connector. More information on the Box API docs [here](https://developer.box.com/reference/put-files-upload-sessions-id/#param-digest)

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetFileResponse
            File

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apideck_consumer_id="YOUR_APIDECK_CONSUMER_ID",
            apideck_app_id="YOUR_APIDECK_APP_ID",
            apideck_service_id="YOUR_APIDECK_SERVICE_ID",
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.upload_sessions.finish(
                id="id",
                digest="sha=fpRyg5eVQletdZqEKaFlqwBXJzM=",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.finish(id, raw=raw, digest=digest, request_options=request_options)
        return _response.data
