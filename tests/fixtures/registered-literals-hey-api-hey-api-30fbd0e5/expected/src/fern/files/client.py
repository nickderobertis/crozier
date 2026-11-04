

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.file_revision_metadata_v2 import FileRevisionMetadataV2
from .raw_client import AsyncRawFilesClient, RawFilesClient


class FilesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawFilesClient
        """
        return self._raw_client

    def query_val_file_by_id(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FileRevisionMetadataV2:
        """
        Get file metadata by file ID

        Parameters
        ----------
        file_id : str
            ID of a file in a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileRevisionMetadataV2
            A File or Directory's Metadata

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.files.query_val_file_by_id(
            file_id="file_id",
        )
        """
        _response = self._raw_client.query_val_file_by_id(file_id, request_options=request_options)
        return _response.data


class AsyncFilesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawFilesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawFilesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawFilesClient
        """
        return self._raw_client

    async def query_val_file_by_id(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> FileRevisionMetadataV2:
        """
        Get file metadata by file ID

        Parameters
        ----------
        file_id : str
            ID of a file in a val

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        FileRevisionMetadataV2
            A File or Directory's Metadata

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.files.query_val_file_by_id(
                file_id="file_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.query_val_file_by_id(file_id, request_options=request_options)
        return _response.data
