

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDocksClient, RawDocksClient
from .types.get_dock_response import GetDockResponse


class DocksClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDocksClient
        """
        return self._raw_client

    def get_dock(
        self, dock_id_or_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDockResponse:
        """
        Parameters
        ----------
        dock_id_or_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDockResponse
            The dock

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.docks.get_dock(
            dock_id_or_code="dock_id_or_code",
        )
        """
        _response = self._raw_client.get_dock(dock_id_or_code, request_options=request_options)
        return _response.data


class AsyncDocksClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDocksClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDocksClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDocksClient
        """
        return self._raw_client

    async def get_dock(
        self, dock_id_or_code: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> GetDockResponse:
        """
        Parameters
        ----------
        dock_id_or_code : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        GetDockResponse
            The dock

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.docks.get_dock(
                dock_id_or_code="dock_id_or_code",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_dock(dock_id_or_code, request_options=request_options)
        return _response.data
