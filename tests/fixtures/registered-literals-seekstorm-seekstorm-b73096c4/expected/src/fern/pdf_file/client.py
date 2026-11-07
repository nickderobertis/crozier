

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPdfFileClient, RawPdfFileClient


OMIT = typing.cast(typing.Any, ...)


class PdfFileClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPdfFileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPdfFileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPdfFileClient
        """
        return self._raw_client

    def index_pdf_file(
        self,
        index_id: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Index PDF file (byte array) to the index with the specified apikey and index_id, and return the number of indexed docs.
        - Converts PDF to a JSON document with "title", "body", "url" and "date" fields and indexes it.
        - extracts title from metatag, or first line of text, or from filename
        - extracts creation date from metatag, or from file creation date (Unix timestamp: the number of seconds since 1 January 1970)
        - copies all ingested pdf files to "files" subdirectory in index

        Parameters
        ----------
        index_id : int
            index id

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            PDF file indexed, returns the number of indexed documents
        """
        _response = self._raw_client.index_pdf_file(index_id, request=request, request_options=request_options)
        return _response.data

    def get_pdf_file(
        self, index_id: int, document_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.Iterator[bytes]:
        """
        Get PDF file from index with index_id
        ⚠️ Use search or get_iterator first to obtain s valid doc_id. Document IDs are not guaranteed to be continuous and gapless!

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.Iterator[bytes]
            PDF file found, returns the PDF file as byte array

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            apikey="YOUR_APIKEY",
        )
        client.pdf_file.get_pdf_file(
            index_id=1000000,
            document_id=1000000,
        )
        """
        with self._raw_client.get_pdf_file(index_id, document_id, request_options=request_options) as r:
            yield from r.data


class AsyncPdfFileClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPdfFileClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPdfFileClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPdfFileClient
        """
        return self._raw_client

    async def index_pdf_file(
        self,
        index_id: int,
        *,
        request: typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Index PDF file (byte array) to the index with the specified apikey and index_id, and return the number of indexed docs.
        - Converts PDF to a JSON document with "title", "body", "url" and "date" fields and indexes it.
        - extracts title from metatag, or first line of text, or from filename
        - extracts creation date from metatag, or from file creation date (Unix timestamp: the number of seconds since 1 January 1970)
        - copies all ingested pdf files to "files" subdirectory in index

        Parameters
        ----------
        index_id : int
            index id

        request : typing.Union[bytes, typing.Iterator[bytes], typing.AsyncIterator[bytes]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            PDF file indexed, returns the number of indexed documents
        """
        _response = await self._raw_client.index_pdf_file(index_id, request=request, request_options=request_options)
        return _response.data

    async def get_pdf_file(
        self, index_id: int, document_id: int, *, request_options: typing.Optional[RequestOptions] = None
    ) -> typing.AsyncIterator[bytes]:
        """
        Get PDF file from index with index_id
        ⚠️ Use search or get_iterator first to obtain s valid doc_id. Document IDs are not guaranteed to be continuous and gapless!

        Parameters
        ----------
        index_id : int
            index id

        document_id : int
            document id

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.

        Returns
        -------
        typing.AsyncIterator[bytes]
            PDF file found, returns the PDF file as byte array

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            apikey="YOUR_APIKEY",
        )


        async def main() -> None:
            await client.pdf_file.get_pdf_file(
                index_id=1000000,
                document_id=1000000,
            )


        asyncio.run(main())
        """
        async with self._raw_client.get_pdf_file(index_id, document_id, request_options=request_options) as r:
            async for _chunk in r.data:
                yield _chunk
