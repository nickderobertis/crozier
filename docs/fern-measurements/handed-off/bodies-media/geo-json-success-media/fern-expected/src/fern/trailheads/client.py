

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.trailhead_feature import TrailheadFeature
from .raw_client import AsyncRawTrailheadsClient, RawTrailheadsClient


class TrailheadsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawTrailheadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawTrailheadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawTrailheadsClient
        """
        return self._raw_client

    def get_trailhead(
        self, trailhead_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrailheadFeature:
        """
        Parameters
        ----------
        trailhead_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrailheadFeature
            The trailhead feature.

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.trailheads.get_trailhead(
            trailhead_id="trailheadId",
        )
        """
        _response = self._raw_client.get_trailhead(trailhead_id, request_options=request_options)
        return _response.data


class AsyncTrailheadsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawTrailheadsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawTrailheadsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawTrailheadsClient
        """
        return self._raw_client

    async def get_trailhead(
        self, trailhead_id: str, *, request_options: typing.Optional[RequestOptions] = None
    ) -> TrailheadFeature:
        """
        Parameters
        ----------
        trailhead_id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        TrailheadFeature
            The trailhead feature.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.trailheads.get_trailhead(
                trailhead_id="trailheadId",
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.get_trailhead(trailhead_id, request_options=request_options)
        return _response.data
