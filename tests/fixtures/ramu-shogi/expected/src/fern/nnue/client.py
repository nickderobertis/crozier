

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.complete_nnue_upload_response import CompleteNnueUploadResponse
from ..types.initialize_nnue_upload_response import InitializeNnueUploadResponse
from ..types.list_nnue_files_response import ListNnueFilesResponse
from ..types.ok_response import OkResponse
from ..types.upload_nnue_part_response import UploadNnuePartResponse
from .raw_client import AsyncRawNnueClient, RawNnueClient
from .types.complete_nnue_upload_request_parts_item import CompleteNnueUploadRequestPartsItem


OMIT = typing.cast(typing.Any, ...)


class NnueClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawNnueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawNnueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawNnueClient
        """
        return self._raw_client

    def list_nnue_files(self, *, request_options: typing.Optional[RequestOptions] = None) -> ListNnueFilesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNnueFilesResponse
            List NNUE files

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nnue.list_nnue_files()
        """
        _response = self._raw_client.list_nnue_files(request_options=request_options)
        return _response.data

    def initialize_nnue_upload(
        self,
        *,
        original_filename: str,
        size_bytes: int,
        sha256hex: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InitializeNnueUploadResponse:
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
        InitializeNnueUploadResponse
            Initialized NNUE upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nnue.initialize_nnue_upload(
            original_filename="originalFilename",
            size_bytes=1,
            sha256hex="sha256Hex",
        )
        """
        _response = self._raw_client.initialize_nnue_upload(
            original_filename=original_filename,
            size_bytes=size_bytes,
            sha256hex=sha256hex,
            request_options=request_options,
        )
        return _response.data

    def upload_nnue_part(
        self, file_id: str, part_number: int, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadNnuePartResponse:
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
        UploadNnuePartResponse
            Uploaded NNUE part

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nnue.upload_nnue_part(
            file_id="fileId",
            part_number=1,
            upload_id="uploadId",
        )
        """
        _response = self._raw_client.upload_nnue_part(
            file_id, part_number, upload_id=upload_id, request_options=request_options
        )
        return _response.data

    def complete_nnue_upload(
        self,
        file_id: str,
        *,
        upload_id: str,
        parts: typing.Sequence[CompleteNnueUploadRequestPartsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteNnueUploadResponse:
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
        CompleteNnueUploadResponse
            Completed NNUE upload

        Examples
        --------
        from fern.nnue import CompleteNnueUploadRequestPartsItem

        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nnue.complete_nnue_upload(
            file_id="fileId",
            upload_id="uploadId",
            parts=[
                CompleteNnueUploadRequestPartsItem(
                    part_number=1,
                    etag="etag",
                )
            ],
        )
        """
        _response = self._raw_client.complete_nnue_upload(
            file_id, upload_id=upload_id, parts=parts, request_options=request_options
        )
        return _response.data

    def abort_nnue_upload(
        self, file_id: str, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """
        Parameters
        ----------
        file_id : str

        upload_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            Aborted NNUE upload

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nnue.abort_nnue_upload(
            file_id="fileId",
            upload_id="uploadId",
        )
        """
        _response = self._raw_client.abort_nnue_upload(file_id, upload_id=upload_id, request_options=request_options)
        return _response.data

    def delete_nnue_file(self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> OkResponse:
        """
        Parameters
        ----------
        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            Deleted NNUE file

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.nnue.delete_nnue_file(
            file_id="fileId",
        )
        """
        _response = self._raw_client.delete_nnue_file(file_id, request_options=request_options)
        return _response.data


class AsyncNnueClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawNnueClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawNnueClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawNnueClient
        """
        return self._raw_client

    async def list_nnue_files(
        self, *, request_options: typing.Optional[RequestOptions] = None
    ) -> ListNnueFilesResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        ListNnueFilesResponse
            List NNUE files

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nnue.list_nnue_files()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_nnue_files(request_options=request_options)
        return _response.data

    async def initialize_nnue_upload(
        self,
        *,
        original_filename: str,
        size_bytes: int,
        sha256hex: str,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> InitializeNnueUploadResponse:
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
        InitializeNnueUploadResponse
            Initialized NNUE upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nnue.initialize_nnue_upload(
                original_filename="originalFilename",
                size_bytes=1,
                sha256hex="sha256Hex",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.initialize_nnue_upload(
            original_filename=original_filename,
            size_bytes=size_bytes,
            sha256hex=sha256hex,
            request_options=request_options,
        )
        return _response.data

    async def upload_nnue_part(
        self, file_id: str, part_number: int, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> UploadNnuePartResponse:
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
        UploadNnuePartResponse
            Uploaded NNUE part

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nnue.upload_nnue_part(
                file_id="fileId",
                part_number=1,
                upload_id="uploadId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_nnue_part(
            file_id, part_number, upload_id=upload_id, request_options=request_options
        )
        return _response.data

    async def complete_nnue_upload(
        self,
        file_id: str,
        *,
        upload_id: str,
        parts: typing.Sequence[CompleteNnueUploadRequestPartsItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> CompleteNnueUploadResponse:
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
        CompleteNnueUploadResponse
            Completed NNUE upload

        Examples
        --------
        import asyncio

        from fern.nnue import CompleteNnueUploadRequestPartsItem

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nnue.complete_nnue_upload(
                file_id="fileId",
                upload_id="uploadId",
                parts=[
                    CompleteNnueUploadRequestPartsItem(
                        part_number=1,
                        etag="etag",
                    )
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.complete_nnue_upload(
            file_id, upload_id=upload_id, parts=parts, request_options=request_options
        )
        return _response.data

    async def abort_nnue_upload(
        self, file_id: str, *, upload_id: str, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """
        Parameters
        ----------
        file_id : str

        upload_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            Aborted NNUE upload

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nnue.abort_nnue_upload(
                file_id="fileId",
                upload_id="uploadId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.abort_nnue_upload(
            file_id, upload_id=upload_id, request_options=request_options
        )
        return _response.data

    async def delete_nnue_file(
        self, file_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> OkResponse:
        """
        Parameters
        ----------
        file_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        OkResponse
            Deleted NNUE file

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.nnue.delete_nnue_file(
                file_id="fileId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_nnue_file(file_id, request_options=request_options)
        return _response.data
