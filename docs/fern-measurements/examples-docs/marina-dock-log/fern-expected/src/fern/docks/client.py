

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawDocksClient, RawDocksClient


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

    def export_dock_log(
        self,
        dock_id: str,
        *,
        columns: typing.Optional[str] = None,
        compact: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        dock_id : str

        columns : typing.Optional[str]

        compact : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The log as CSV text

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.docks.export_dock_log(
            dock_id="dock_id",
        )
        """
        _response = self._raw_client.export_dock_log(
            dock_id, columns=columns, compact=compact, request_options=request_options
        )
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

    async def export_dock_log(
        self,
        dock_id: str,
        *,
        columns: typing.Optional[str] = None,
        compact: typing.Optional[str] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> str:
        """
        Parameters
        ----------
        dock_id : str

        columns : typing.Optional[str]

        compact : typing.Optional[str]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        str
            The log as CSV text

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.docks.export_dock_log(
                dock_id="dock_id",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.export_dock_log(
            dock_id, columns=columns, compact=compact, request_options=request_options
        )
        return _response.data
