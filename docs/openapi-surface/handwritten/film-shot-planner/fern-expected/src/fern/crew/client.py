

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawCrewClient, RawCrewClient
from .types.call_sheet_crew_response import CallSheetCrewResponse


class CrewClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawCrewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawCrewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawCrewClient
        """
        return self._raw_client

    def call_sheet(self, *, request_options: typing.Optional[RequestOptions] = None) -> CallSheetCrewResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallSheetCrewResponse
            The crew's call sheet.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.crew.call_sheet()
        """
        _response = self._raw_client.call_sheet(request_options=request_options)
        return _response.data


class AsyncCrewClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawCrewClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawCrewClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawCrewClient
        """
        return self._raw_client

    async def call_sheet(self, *, request_options: typing.Optional[RequestOptions] = None) -> CallSheetCrewResponse:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        CallSheetCrewResponse
            The crew's call sheet.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.crew.call_sheet()


        asyncio.run(main())
        """
        _response = await self._raw_client.call_sheet(request_options=request_options)
        return _response.data
