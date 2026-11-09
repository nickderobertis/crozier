

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.launch import Launch
from .raw_client import AsyncRawLaunchesClient, RawLaunchesClient


class LaunchesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawLaunchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawLaunchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawLaunchesClient
        """
        return self._raw_client

    def fetch_launch(self, launch_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Launch:
        """
        Parameters
        ----------
        launch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Launch
            The launch.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.launches.fetch_launch(
            launch_id="launchId",
        )
        """
        _response = self._raw_client.fetch_launch(launch_id, request_options=request_options)
        return _response.data


class AsyncLaunchesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawLaunchesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawLaunchesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawLaunchesClient
        """
        return self._raw_client

    async def fetch_launch(self, launch_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Launch:
        """
        Parameters
        ----------
        launch_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Launch
            The launch.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.launches.fetch_launch(
                launch_id="launchId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_launch(launch_id, request_options=request_options)
        return _response.data
