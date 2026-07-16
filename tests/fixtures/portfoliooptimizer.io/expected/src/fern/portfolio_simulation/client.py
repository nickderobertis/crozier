

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortfolioSimulationClient, RawPortfolioSimulationClient
from .types.post_portfolio_simulation_rebalancing_drift_weight_request_assets_item import (
    PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem,
)
from .types.post_portfolio_simulation_rebalancing_drift_weight_request_portfolios_item import (
    PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem,
)
from .types.post_portfolio_simulation_rebalancing_drift_weight_response import (
    PostPortfolioSimulationRebalancingDriftWeightResponse,
)
from .types.post_portfolio_simulation_rebalancing_fixed_weight_request_assets_item import (
    PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem,
)
from .types.post_portfolio_simulation_rebalancing_fixed_weight_request_portfolios_item import (
    PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem,
)
from .types.post_portfolio_simulation_rebalancing_fixed_weight_response import (
    PostPortfolioSimulationRebalancingFixedWeightResponse,
)
from .types.post_portfolio_simulation_rebalancing_random_weight_request_assets_item import (
    PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem,
)
from .types.post_portfolio_simulation_rebalancing_random_weight_response import (
    PostPortfolioSimulationRebalancingRandomWeightResponse,
)


OMIT = typing.cast(typing.Any, ...)


class PortfolioSimulationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioSimulationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioSimulationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioSimulationClient
        """
        return self._raw_client

    def drift_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioSimulationRebalancingDriftWeightResponse:
        """
        Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being never rebalanced (a.k.a. buy and hold).

        References
        * [Hillion, Pierre, The Ex-Ante Rebalancing Premium (March 11, 2016). INSEAD Working Paper No. 2016/15/FIN](https://ssrn.com/abstract=2746471)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem]

        portfolios : typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioSimulationRebalancingDriftWeightResponse
            OK

        Examples
        --------
        from fern.portfolio_simulation import (
            PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem,
            PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_simulation.drift_weight_portfolio_rebalancing(
            assets=[
                PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
                    asset_prices=[100.0, 105.0, 110.0],
                ),
                PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
                    asset_prices=[15.0, 12.5, 11.25],
                ),
                PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
                    asset_prices=[0.5, 0.51, 0.49],
                ),
            ],
            portfolios=[
                PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
                    assets_weights=[1.0, 0.0, 0.0],
                ),
                PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
                    assets_weights=[0.0, 1.0, 0.0],
                ),
                PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
                    assets_weights=[0.0, 0.0, 1.0],
                ),
            ],
        )
        """
        _response = self._raw_client.drift_weight_portfolio_rebalancing(
            assets=assets, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    def fixed_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioSimulationRebalancingFixedWeightResponse:
        """
        Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being rebalanced toward fixed weights at the beginning of each time period.

        References
        * [Hillion, Pierre, The Ex-Ante Rebalancing Premium (March 11, 2016). INSEAD Working Paper No. 2016/15/FIN](https://ssrn.com/abstract=2746471)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem]

        portfolios : typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioSimulationRebalancingFixedWeightResponse
            OK

        Examples
        --------
        from fern.portfolio_simulation import (
            PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem,
            PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_simulation.fixed_weight_portfolio_rebalancing(
            assets=[
                PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
                    asset_prices=[100.0, 105.0, 110.0],
                ),
                PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
                    asset_prices=[15.0, 12.5, 11.25],
                ),
                PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
                    asset_prices=[0.5, 0.51, 0.49],
                ),
            ],
            portfolios=[
                PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
                    assets_weights=[0.5, 0.5, 0.0],
                ),
                PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
                    assets_weights=[0.0, 0.5, 0.5],
                ),
                PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
                    assets_weights=[0.5, 0.0, 0.5],
                ),
            ],
        )
        """
        _response = self._raw_client.fixed_weight_portfolio_rebalancing(
            assets=assets, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    def random_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem],
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioSimulationRebalancingRandomWeightResponse:
        """
        Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being rebalanced toward random weights at the beginning of each time period.

        References
        * [R Stein, Not fooled by randomness: Using random portfolios to analyse investment funds, Investment Analysts Journal, 43:79, 1-15, DOI: 10.1080/10293523.2014.11082564](https://www.tandfonline.com/doi/abs/10.1080/10293523.2014.11082564)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem]

        portfolios : typing.Optional[int]
            The number of portfolios to simulate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioSimulationRebalancingRandomWeightResponse
            OK

        Examples
        --------
        from fern.portfolio_simulation import (
            PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_simulation.random_weight_portfolio_rebalancing(
            assets=[
                PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
                    asset_prices=[100.0, 105.0, 110.0],
                ),
                PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
                    asset_prices=[15.0, 12.5, 11.25],
                ),
                PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
                    asset_prices=[0.5, 0.51, 0.49],
                ),
            ],
            portfolios=2,
        )
        """
        _response = self._raw_client.random_weight_portfolio_rebalancing(
            assets=assets, portfolios=portfolios, request_options=request_options
        )
        return _response.data


class AsyncPortfolioSimulationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioSimulationClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioSimulationClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioSimulationClient
        """
        return self._raw_client

    async def drift_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioSimulationRebalancingDriftWeightResponse:
        """
        Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being never rebalanced (a.k.a. buy and hold).

        References
        * [Hillion, Pierre, The Ex-Ante Rebalancing Premium (March 11, 2016). INSEAD Working Paper No. 2016/15/FIN](https://ssrn.com/abstract=2746471)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem]

        portfolios : typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioSimulationRebalancingDriftWeightResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_simulation import (
            PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem,
            PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_simulation.drift_weight_portfolio_rebalancing(
                assets=[
                    PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
                        asset_prices=[100.0, 105.0, 110.0],
                    ),
                    PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
                        asset_prices=[15.0, 12.5, 11.25],
                    ),
                    PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
                        asset_prices=[0.5, 0.51, 0.49],
                    ),
                ],
                portfolios=[
                    PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
                        assets_weights=[1.0, 0.0, 0.0],
                    ),
                    PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
                        assets_weights=[0.0, 1.0, 0.0],
                    ),
                    PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
                        assets_weights=[0.0, 0.0, 1.0],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.drift_weight_portfolio_rebalancing(
            assets=assets, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    async def fixed_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioSimulationRebalancingFixedWeightResponse:
        """
        Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being rebalanced toward fixed weights at the beginning of each time period.

        References
        * [Hillion, Pierre, The Ex-Ante Rebalancing Premium (March 11, 2016). INSEAD Working Paper No. 2016/15/FIN](https://ssrn.com/abstract=2746471)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem]

        portfolios : typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioSimulationRebalancingFixedWeightResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_simulation import (
            PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem,
            PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_simulation.fixed_weight_portfolio_rebalancing(
                assets=[
                    PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
                        asset_prices=[100.0, 105.0, 110.0],
                    ),
                    PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
                        asset_prices=[15.0, 12.5, 11.25],
                    ),
                    PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
                        asset_prices=[0.5, 0.51, 0.49],
                    ),
                ],
                portfolios=[
                    PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
                        assets_weights=[0.5, 0.5, 0.0],
                    ),
                    PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
                        assets_weights=[0.0, 0.5, 0.5],
                    ),
                    PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
                        assets_weights=[0.5, 0.0, 0.5],
                    ),
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.fixed_weight_portfolio_rebalancing(
            assets=assets, portfolios=portfolios, request_options=request_options
        )
        return _response.data

    async def random_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem],
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioSimulationRebalancingRandomWeightResponse:
        """
        Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being rebalanced toward random weights at the beginning of each time period.

        References
        * [R Stein, Not fooled by randomness: Using random portfolios to analyse investment funds, Investment Analysts Journal, 43:79, 1-15, DOI: 10.1080/10293523.2014.11082564](https://www.tandfonline.com/doi/abs/10.1080/10293523.2014.11082564)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem]

        portfolios : typing.Optional[int]
            The number of portfolios to simulate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioSimulationRebalancingRandomWeightResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_simulation import (
            PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_simulation.random_weight_portfolio_rebalancing(
                assets=[
                    PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
                        asset_prices=[100.0, 105.0, 110.0],
                    ),
                    PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
                        asset_prices=[15.0, 12.5, 11.25],
                    ),
                    PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
                        asset_prices=[0.5, 0.51, 0.49],
                    ),
                ],
                portfolios=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.random_weight_portfolio_rebalancing(
            assets=assets, portfolios=portfolios, request_options=request_options
        )
        return _response.data
