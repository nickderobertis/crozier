

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsReturnsSimulationClient, RawAssetsReturnsSimulationClient
from .types.post_assets_returns_simulation_bootstrap_request_assets_item import (
    PostAssetsReturnsSimulationBootstrapRequestAssetsItem,
)
from .types.post_assets_returns_simulation_bootstrap_request_bootstrap_method import (
    PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod,
)
from .types.post_assets_returns_simulation_bootstrap_response import PostAssetsReturnsSimulationBootstrapResponse


OMIT = typing.cast(typing.Any, ...)


class AssetsReturnsSimulationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsReturnsSimulationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsReturnsSimulationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsReturnsSimulationClient
        """
        return self._raw_client

    def bootstrap(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem],
        bootstrap_average_block_length: typing.Optional[float] = OMIT,
        bootstrap_block_length: typing.Optional[int] = OMIT,
        bootstrap_method: typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod] = OMIT,
        simulations: typing.Optional[int] = OMIT,
        simulations_length: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsReturnsSimulationBootstrapResponse:
        """
        Simulate the return(s) of one or several asset(s) for one or several time period(s) using a bootstrap method.

        References
        * [Efron, B. (1979), Bootstrap methods: Another look at the jackknife, The Annals of Statistics 7, 1-26](https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full)
        * [Politis, D. N. and Romano, J. P., A circular block resampling procedure for stationary data, in R. Lepage and L. Billard, eds, Exploring the Limits of Bootstrap, Wiley, New York, pp. 263-270](https://statistics.stanford.edu/technical-reports/circular-block-resampling-procedure-stationary-data)
        * [Politis, D. N. and Romano, J. P., The stationary bootstrap, Journal of the American Statistical Association 89, 1303-1313](https://www.jstor.org/stable/2290993)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem]

        bootstrap_average_block_length : typing.Optional[float]
            The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3

        bootstrap_block_length : typing.Optional[int]
            The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]

        bootstrap_method : typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod]
            The bootstrap method to use

        simulations : typing.Optional[int]
            The number of simulations to perform

        simulations_length : typing.Optional[int]
            The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsReturnsSimulationBootstrapResponse
            OK

        Examples
        --------
        from fern.assets_returns_simulation import (
            PostAssetsReturnsSimulationBootstrapRequestAssetsItem,
            PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_returns_simulation.bootstrap(
            assets=[
                PostAssetsReturnsSimulationBootstrapRequestAssetsItem(
                    asset_returns=[0.1, -0.05, 0.01, 0.025, -0.1],
                ),
                PostAssetsReturnsSimulationBootstrapRequestAssetsItem(
                    asset_returns=[0.0, 0.01, 0.02, -0.01, 0.05],
                ),
            ],
            bootstrap_block_length=2,
            bootstrap_method=PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod.CIRCULAR_BLOCK,
            simulations=5,
            simulations_length=4,
        )
        """
        _response = self._raw_client.bootstrap(
            assets=assets,
            bootstrap_average_block_length=bootstrap_average_block_length,
            bootstrap_block_length=bootstrap_block_length,
            bootstrap_method=bootstrap_method,
            simulations=simulations,
            simulations_length=simulations_length,
            request_options=request_options,
        )
        return _response.data


class AsyncAssetsReturnsSimulationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsReturnsSimulationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsReturnsSimulationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsReturnsSimulationClient
        """
        return self._raw_client

    async def bootstrap(
        self,
        *,
        assets: typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem],
        bootstrap_average_block_length: typing.Optional[float] = OMIT,
        bootstrap_block_length: typing.Optional[int] = OMIT,
        bootstrap_method: typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod] = OMIT,
        simulations: typing.Optional[int] = OMIT,
        simulations_length: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsReturnsSimulationBootstrapResponse:
        """
        Simulate the return(s) of one or several asset(s) for one or several time period(s) using a bootstrap method.

        References
        * [Efron, B. (1979), Bootstrap methods: Another look at the jackknife, The Annals of Statistics 7, 1-26](https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full)
        * [Politis, D. N. and Romano, J. P., A circular block resampling procedure for stationary data, in R. Lepage and L. Billard, eds, Exploring the Limits of Bootstrap, Wiley, New York, pp. 263-270](https://statistics.stanford.edu/technical-reports/circular-block-resampling-procedure-stationary-data)
        * [Politis, D. N. and Romano, J. P., The stationary bootstrap, Journal of the American Statistical Association 89, 1303-1313](https://www.jstor.org/stable/2290993)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsReturnsSimulationBootstrapRequestAssetsItem]

        bootstrap_average_block_length : typing.Optional[float]
            The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3

        bootstrap_block_length : typing.Optional[int]
            The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]

        bootstrap_method : typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod]
            The bootstrap method to use

        simulations : typing.Optional[int]
            The number of simulations to perform

        simulations_length : typing.Optional[int]
            The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostAssetsReturnsSimulationBootstrapResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_returns_simulation import (
            PostAssetsReturnsSimulationBootstrapRequestAssetsItem,
            PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_returns_simulation.bootstrap(
                assets=[
                    PostAssetsReturnsSimulationBootstrapRequestAssetsItem(
                        asset_returns=[0.1, -0.05, 0.01, 0.025, -0.1],
                    ),
                    PostAssetsReturnsSimulationBootstrapRequestAssetsItem(
                        asset_returns=[0.0, 0.01, 0.02, -0.01, 0.05],
                    ),
                ],
                bootstrap_block_length=2,
                bootstrap_method=PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod.CIRCULAR_BLOCK,
                simulations=5,
                simulations_length=4,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bootstrap(
            assets=assets,
            bootstrap_average_block_length=bootstrap_average_block_length,
            bootstrap_block_length=bootstrap_block_length,
            bootstrap_method=bootstrap_method,
            simulations=simulations,
            simulations_length=simulations_length,
            request_options=request_options,
        )
        return _response.data
