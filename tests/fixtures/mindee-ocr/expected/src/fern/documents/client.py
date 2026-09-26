

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDocumentsClient, RawDocumentsClient


OMIT = typing.cast(typing.Any, ...)


class DocumentsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocumentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDocumentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocumentsClient
        """
        return self._raw_client

    def get_document(
        self,
        account: str,
        product: str,
        version: str,
        document_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve a previously parsed document by ID.

        Parameters
        ----------
        account : str

        product : str

        version : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Document details.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.documents.get_document(
            account="account",
            product="product",
            version="version",
            document_id="document_id",
        )
        """
        _response = self._raw_client.get_document(
            account, product, version, document_id, request_options=request_options
        )
        return _response.data

    def send_document_feedback(
        self,
        document_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Submit feedback for a parsed document.

        Parameters
        ----------
        document_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
        )
        client.documents.send_document_feedback(
            document_id="document_id",
            request={"key": "value"},
        )
        """
        _response = self._raw_client.send_document_feedback(
            document_id, request=request, request_options=request_options
        )
        return _response.data


class AsyncDocumentsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocumentsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDocumentsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocumentsClient
        """
        return self._raw_client

    async def get_document(
        self,
        account: str,
        product: str,
        version: str,
        document_id: str,
        *,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.Dict[str, typing.Any]:
        """
        Retrieve a previously parsed document by ID.

        Parameters
        ----------
        account : str

        product : str

        version : str

        document_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.Dict[str, typing.Any]
            Document details.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.documents.get_document(
                account="account",
                product="product",
                version="version",
                document_id="document_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_document(
            account, product, version, document_id, request_options=request_options
        )
        return _response.data

    async def send_document_feedback(
        self,
        document_id: str,
        *,
        request: typing.Dict[str, typing.Any],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Submit feedback for a parsed document.

        Parameters
        ----------
        document_id : str

        request : typing.Dict[str, typing.Any]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.documents.send_document_feedback(
                document_id="document_id",
                request={"key": "value"},
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.send_document_feedback(
            document_id, request=request, request_options=request_options
        )
        return _response.data
