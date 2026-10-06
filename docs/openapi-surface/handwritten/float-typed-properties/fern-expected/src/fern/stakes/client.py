

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.stake import Stake
from .raw_client import AsyncRawStakesClient, RawStakesClient


OMIT = typing.cast(typing.Any, ...)


class StakesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawStakesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawStakesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawStakesClient
        """
        return self._raw_client

    def record_stake(
        self,
        *,
        ablation: float,
        tolerance: typing.Optional[float] = None,
        albedo: typing.Optional[float] = OMIT,
        readings: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Stake:
        """
        Parameters
        ----------
        ablation : float

        tolerance : typing.Optional[float]

        albedo : typing.Optional[float]

        readings : typing.Optional[typing.Sequence[float]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stake
            The stake reading was recorded.

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.stakes.record_stake(
            ablation=1.1,
        )
        """
        _response = self._raw_client.record_stake(
            ablation=ablation, tolerance=tolerance, albedo=albedo, readings=readings, request_options=request_options
        )
        return _response.data


class AsyncStakesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawStakesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawStakesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawStakesClient
        """
        return self._raw_client

    async def record_stake(
        self,
        *,
        ablation: float,
        tolerance: typing.Optional[float] = None,
        albedo: typing.Optional[float] = OMIT,
        readings: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Stake:
        """
        Parameters
        ----------
        ablation : float

        tolerance : typing.Optional[float]

        albedo : typing.Optional[float]

        readings : typing.Optional[typing.Sequence[float]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Stake
            The stake reading was recorded.

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.stakes.record_stake(
                ablation=1.1,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.record_stake(
            ablation=ablation, tolerance=tolerance, albedo=albedo, readings=readings, request_options=request_options
        )
        return _response.data
