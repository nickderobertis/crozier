

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawClientApiFileUploadClient, RawClientApiFileUploadClient
from .types.post_client_workspace_id_storage_response import PostClientWorkspaceIdStorageResponse


OMIT = typing.cast(typing.Any, ...)


class ClientApiFileUploadClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawClientApiFileUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawClientApiFileUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawClientApiFileUploadClient
        """
        return self._raw_client

    def upload_private_file(
        self,
        workspace_id: str,
        *,
        survey_id: str,
        file_name: str,
        file_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostClientWorkspaceIdStorageResponse:
        """
        API endpoint for uploading private files. Uploaded files are kept private so that only users with access to the specified Workspace can retrieve them. The endpoint validates the survey ID, file name, and file type from the request body, and returns a signed URL for S3 uploads along with a local upload URL. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        survey_id : str
            The ID of the survey associated with the file.

        file_name : str
            The name of the file to be uploaded.

        file_type : str
            The MIME type of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostClientWorkspaceIdStorageResponse
            OK - Returns the signed URL, presigned fields, updated file name, and file URL.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.client_api_file_upload.upload_private_file(
            workspace_id="workspaceId",
            survey_id="cm7pr0x2y004o192zmit8cjvb",
            file_name="example.jpg",
            file_type="image/jpeg",
        )
        """
        _response = self._raw_client.upload_private_file(
            workspace_id, survey_id=survey_id, file_name=file_name, file_type=file_type, request_options=request_options
        )
        return _response.data


class AsyncClientApiFileUploadClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawClientApiFileUploadClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawClientApiFileUploadClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawClientApiFileUploadClient
        """
        return self._raw_client

    async def upload_private_file(
        self,
        workspace_id: str,
        *,
        survey_id: str,
        file_name: str,
        file_type: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostClientWorkspaceIdStorageResponse:
        """
        API endpoint for uploading private files. Uploaded files are kept private so that only users with access to the specified Workspace can retrieve them. The endpoint validates the survey ID, file name, and file type from the request body, and returns a signed URL for S3 uploads along with a local upload URL. Note - Environments are deprecated. Use Workspace/workspaceId terminology.

        Parameters
        ----------
        workspace_id : str
            The ID of the Workspace. Deprecated alias `environmentId`.

        survey_id : str
            The ID of the survey associated with the file.

        file_name : str
            The name of the file to be uploaded.

        file_type : str
            The MIME type of the file.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostClientWorkspaceIdStorageResponse
            OK - Returns the signed URL, presigned fields, updated file name, and file URL.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.client_api_file_upload.upload_private_file(
                workspace_id="workspaceId",
                survey_id="cm7pr0x2y004o192zmit8cjvb",
                file_name="example.jpg",
                file_type="image/jpeg",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_private_file(
            workspace_id, survey_id=survey_id, file_name=file_name, file_type=file_type, request_options=request_options
        )
        return _response.data
