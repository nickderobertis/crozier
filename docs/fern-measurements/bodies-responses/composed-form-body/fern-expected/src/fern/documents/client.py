

import typing

from .. import core
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

    def upload_document(
        self,
        request_id: str,
        *,
        file: core.File,
        parent_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request_id : str

        file : core.File
            See core.File for more documentation

        parent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.documents.upload_document(
            request_id="requestId",
        )
        """
        _response = self._raw_client.upload_document(
            request_id, file=file, parent_id=parent_id, request_options=request_options
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

    async def upload_document(
        self,
        request_id: str,
        *,
        file: core.File,
        parent_id: typing.Optional[str] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> None:
        """
        Parameters
        ----------
        request_id : str

        file : core.File
            See core.File for more documentation

        parent_id : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        None

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.documents.upload_document(
                request_id="requestId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.upload_document(
            request_id, file=file, parent_id=parent_id, request_options=request_options
        )
        return _response.data
