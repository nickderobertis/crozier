

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.road_operators import RoadOperators
from .raw_client import AsyncRawRoadOperatorsV2Client, RawRoadOperatorsV2Client


class RoadOperatorsV2Client:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawRoadOperatorsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawRoadOperatorsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawRoadOperatorsV2Client
        """
        return self._raw_client

    def get_road_operators(self, *, request_options: typing.Optional[RequestOptions] = None) -> RoadOperators:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoadOperators
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi()
        client.road_operators_v2.get_road_operators()
        """
        _response = self._raw_client.get_road_operators(request_options=request_options)
        return _response.data


class AsyncRoadOperatorsV2Client:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawRoadOperatorsV2Client(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawRoadOperatorsV2Client:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawRoadOperatorsV2Client
        """
        return self._raw_client

    async def get_road_operators(self, *, request_options: typing.Optional[RequestOptions] = None) -> RoadOperators:
        """
        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        RoadOperators
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi()


        async def main() -> None:
            await client.road_operators_v2.get_road_operators()


        asyncio.run(main())
        """
        _response = await self._raw_client.get_road_operators(request_options=request_options)
        return _response.data
