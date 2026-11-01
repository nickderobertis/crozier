

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDraftFilingsClient, RawDraftFilingsClient


class DraftFilingsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDraftFilingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDraftFilingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDraftFilingsClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Draft filings.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_filings.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data

    def read(self, filing_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        filing_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One draft filing.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.draft_filings.read(
            filing_id="filingId",
        )
        """
        _response = self._raw_client.read(filing_id, request_options=request_options)
        return _response.data


class AsyncDraftFilingsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDraftFilingsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDraftFilingsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDraftFilingsClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            Draft filings.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_filings.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data

    async def read(self, filing_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> str:
        """
        Parameters
        ----------
        filing_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            One draft filing.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.draft_filings.read(
                filing_id="filingId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.read(filing_id, request_options=request_options)
        return _response.data
