

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from ..types.empire_configuration import EmpireConfiguration
from ..types.falcon_configuration import FalconConfiguration
from .raw_client import AsyncRawOddsCalculationsClient, RawOddsCalculationsClient


OMIT = typing.cast(typing.Any, ...)


class OddsCalculationsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawOddsCalculationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawOddsCalculationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawOddsCalculationsClient
        """
        return self._raw_client

    def odds(
        self,
        *,
        empire_config: EmpireConfiguration,
        falcon_config: typing.Optional[FalconConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> float:
        """
        Parameters
        ----------
        empire_config : EmpireConfiguration

        falcon_config : typing.Optional[FalconConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful Response

        Examples
        --------
        from fern import BountyHunters, EmpireConfiguration, FernApi

        client = FernApi(
            base_url="https://yourhost.com/path/to/api",
        )
        client.odds_calculations.odds(
            empire_config=EmpireConfiguration(
                countdown=1,
                bounty_hunters=[
                    BountyHunters(
                        day=1,
                        planet="planet",
                    )
                ],
            ),
        )
        """
        _response = self._raw_client.odds(
            empire_config=empire_config, falcon_config=falcon_config, request_options=request_options
        )
        return _response.data


class AsyncOddsCalculationsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawOddsCalculationsClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawOddsCalculationsClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawOddsCalculationsClient
        """
        return self._raw_client

    async def odds(
        self,
        *,
        empire_config: EmpireConfiguration,
        falcon_config: typing.Optional[FalconConfiguration] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> float:
        """
        Parameters
        ----------
        empire_config : EmpireConfiguration

        falcon_config : typing.Optional[FalconConfiguration]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        float
            Successful Response

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi, BountyHunters, EmpireConfiguration

        client = AsyncFernApi(
            base_url="https://yourhost.com/path/to/api",
        )


        async def main() -> None:
            await client.odds_calculations.odds(
                empire_config=EmpireConfiguration(
                    countdown=1,
                    bounty_hunters=[
                        BountyHunters(
                            day=1,
                            planet="planet",
                        )
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.odds(
            empire_config=empire_config, falcon_config=falcon_config, request_options=request_options
        )
        return _response.data
