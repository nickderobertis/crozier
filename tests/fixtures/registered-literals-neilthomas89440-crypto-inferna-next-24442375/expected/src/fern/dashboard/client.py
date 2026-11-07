

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.dashboard_out import DashboardOut
from .raw_client import AsyncRawDashboardClient, RawDashboardClient


class DashboardClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawDashboardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawDashboardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawDashboardClient
        """
        return self._raw_client

    def dashboard(self, *, request_options: typing.Optional[RequestOptions] = None) -> DashboardOut:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardOut
            Successful Response

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )
        client.dashboard.dashboard()
        """
        _response = self._raw_client.dashboard(request_options=request_options)
        return _response.data


class AsyncDashboardClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawDashboardClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawDashboardClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawDashboardClient
        """
        return self._raw_client

    async def dashboard(self, *, request_options: typing.Optional[RequestOptions] = None) -> DashboardOut:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        DashboardOut
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            token="YOUR_TOKEN",
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.dashboard.dashboard()


        asyncio.run(main())
        """
        _response = await self._raw_client.dashboard(request_options=request_options)
        return _response.data
