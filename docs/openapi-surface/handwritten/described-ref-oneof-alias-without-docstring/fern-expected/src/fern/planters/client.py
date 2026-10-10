

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.planter import Planter
from .raw_client import AsyncRawPlantersClient, RawPlantersClient


class PlantersClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPlantersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPlantersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPlantersClient
        """
        return self._raw_client

    def fetch_planter(self, planter_id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Planter:
        """
        Parameters
        ----------
        planter_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Planter
            The planter on that rack.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.planters.fetch_planter(
            planter_id="planterId",
        )
        """
        _response = self._raw_client.fetch_planter(planter_id, request_options=request_options)
        return _response.data


class AsyncPlantersClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPlantersClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPlantersClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPlantersClient
        """
        return self._raw_client

    async def fetch_planter(
        self, planter_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> Planter:
        """
        Parameters
        ----------
        planter_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Planter
            The planter on that rack.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.planters.fetch_planter(
                planter_id="planterId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fetch_planter(planter_id, request_options=request_options)
        return _response.data
