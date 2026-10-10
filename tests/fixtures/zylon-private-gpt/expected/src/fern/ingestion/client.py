

import typing

from .. import core
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.ingest_response import IngestResponse
from .raw_client import AsyncRawIngestionClient, RawIngestionClient


OMIT = typing.cast(typing.Any, ...)


class IngestionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawIngestionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawIngestionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawIngestionClient
        """
        return self._raw_client

    def ingest(self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None) -> IngestResponse:
        """
        Ingests and processes a file.

        Deprecated. Use ingest/file instead.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingestion.ingest()
        """
        _response = self._raw_client.ingest(file=file, request_options=request_options)
        return _response.data

    def ingest_file(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> IngestResponse:
        """
        Ingests and processes a file, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Most common document
        formats are supported, but you may be prompted to install an extra dependency to
        manage a specific file type.

        A file can generate different Documents (for example a PDF generates one Document
        per page). All Documents IDs are returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). Those IDs
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingestion.ingest_file()
        """
        _response = self._raw_client.ingest_file(file=file, request_options=request_options)
        return _response.data

    def ingest_text(
        self, *, file_name: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IngestResponse:
        """
        Ingests and processes a text, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        A Document will be generated with the given text. The Document
        ID is returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). That ID
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file_name : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingestion.ingest_text(
            file_name="Avatar: The Last Airbender",
            text="Avatar is set in an Asian and Arctic-inspired world in which some people can telekinetically manipulate one of the four elements—water, earth, fire or air—through practices known as 'bending', inspired by Chinese martial arts.",
        )
        """
        _response = self._raw_client.ingest_text(file_name=file_name, text=text, request_options=request_options)
        return _response.data

    def list_ingested(self, *, request_options: typing.Optional[RequestOptions] = None) -> IngestResponse:
        """
        Lists already ingested Documents including their Document ID and metadata.

        Those IDs can be used to filter the context used to create responses
        in `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingestion.list_ingested()
        """
        _response = self._raw_client.list_ingested(request_options=request_options)
        return _response.data

    def delete_ingested(self, doc_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> typing.Any:
        """
        Delete the specified ingested Document.

        The `doc_id` can be obtained from the `GET /ingest/list` endpoint.
        The document will be effectively deleted from your storage context.

        Parameters
        ----------
        doc_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.ingestion.delete_ingested(
            doc_id="doc_id",
        )
        """
        _response = self._raw_client.delete_ingested(doc_id, request_options=request_options)
        return _response.data


class AsyncIngestionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawIngestionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawIngestionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawIngestionClient
        """
        return self._raw_client

    async def ingest(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> IngestResponse:
        """
        Ingests and processes a file.

        Deprecated. Use ingest/file instead.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingestion.ingest()


        asyncio.run(main())
        """
        _response = await self._raw_client.ingest(file=file, request_options=request_options)
        return _response.data

    async def ingest_file(
        self, *, file: core.File, request_options: typing.Optional[RequestOptions] = None
    ) -> IngestResponse:
        """
        Ingests and processes a file, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Most common document
        formats are supported, but you may be prompted to install an extra dependency to
        manage a specific file type.

        A file can generate different Documents (for example a PDF generates one Document
        per page). All Documents IDs are returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). Those IDs
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file : core.File
            See core.File for more documentation

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingestion.ingest_file()


        asyncio.run(main())
        """
        _response = await self._raw_client.ingest_file(file=file, request_options=request_options)
        return _response.data

    async def ingest_text(
        self, *, file_name: str, text: str, request_options: typing.Optional[RequestOptions] = None
    ) -> IngestResponse:
        """
        Ingests and processes a text, storing its chunks to be used as context.

        The context obtained from files is later used in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        A Document will be generated with the given text. The Document
        ID is returned in the response, together with the
        extracted Metadata (which is later used to improve context retrieval). That ID
        can be used to filter the context used to create responses in
        `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        file_name : str

        text : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingestion.ingest_text(
                file_name="Avatar: The Last Airbender",
                text="Avatar is set in an Asian and Arctic-inspired world in which some people can telekinetically manipulate one of the four elements—water, earth, fire or air—through practices known as 'bending', inspired by Chinese martial arts.",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.ingest_text(file_name=file_name, text=text, request_options=request_options)
        return _response.data

    async def list_ingested(self, *, request_options: typing.Optional[RequestOptions] = None) -> IngestResponse:
        """
        Lists already ingested Documents including their Document ID and metadata.

        Those IDs can be used to filter the context used to create responses
        in `/chat/completions`, `/completions`, and `/chunks` APIs.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        IngestResponse
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingestion.list_ingested()


        asyncio.run(main())
        """
        _response = await self._raw_client.list_ingested(request_options=request_options)
        return _response.data

    async def delete_ingested(
        self, doc_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Any:
        """
        Delete the specified ingested Document.

        The `doc_id` can be obtained from the `GET /ingest/list` endpoint.
        The document will be effectively deleted from your storage context.

        Parameters
        ----------
        doc_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Any
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.ingestion.delete_ingested(
                doc_id="doc_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.delete_ingested(doc_id, request_options=request_options)
        return _response.data
