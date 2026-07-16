

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortfolioConstructionClient, RawPortfolioConstructionClient
from .types.post_portfolio_construction_investable_response import PostPortfolioConstructionInvestableResponse
from .types.post_portfolio_construction_mimicking_request_assets_item import (
    PostPortfolioConstructionMimickingRequestAssetsItem,
)
from .types.post_portfolio_construction_mimicking_request_constraints import (
    PostPortfolioConstructionMimickingRequestConstraints,
)
from .types.post_portfolio_construction_mimicking_response import PostPortfolioConstructionMimickingResponse
from .types.post_portfolio_construction_random_request_constraints import (
    PostPortfolioConstructionRandomRequestConstraints,
)
from .types.post_portfolio_construction_random_response import PostPortfolioConstructionRandomResponse


OMIT = typing.cast(typing.Any, ...)


class PortfolioConstructionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioConstructionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioConstructionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioConstructionClient
        """
        return self._raw_client

    def investable_portfolio(
        self,
        *,
        assets: int,
        assets_prices: typing.Sequence[float],
        portfolio_value: float,
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        assets_groups_weights: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_minimum_notional_values: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_minimum_positions: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_size_lots: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_weights: typing.Optional[typing.Sequence[float]] = OMIT,
        maximum_assets_groups_weights: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioConstructionInvestableResponse:
        """
        Compute an investable portfolio as close as possible, in terms of assets weights, to a desired portfolio, taking into account:
        * The desired assets weights
        * The desired assets groups weights
        * The desired maximum assets groups weights
        * The prices of the assets
        * The portfolio value
        * The requirement to purchase some assets by round lots or by odd lots
        * The possibility to purchase some assets by a fractional quantity of shares
        * The requirement to purchase a minimum number of shares, or a minimum monetary value, for some assets

        References
        * [Steiner, Andreas, Accuracy and Rounding in Portfolio Construction](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2261131)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_prices : typing.Sequence[float]
            assetsPrices[i] is the price of the asset i

        portfolio_value : float
            The monetary value of the portfolio

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        assets_groups_weights : typing.Optional[typing.Sequence[float]]
            assetsGroupsWeights[i] is the desired weight of the assets group k in the portfolio, in percentage (can be null to indicate no specific desire); requires assetsGroups to be present

        assets_minimum_notional_values : typing.Optional[typing.Sequence[float]]
            assetsMinimumNotionalValues[i] is the minimum monetary value that the position in the asset i is required to represent when the asset i is included in the portfolio

        assets_minimum_positions : typing.Optional[typing.Sequence[float]]
            assetsMinimumPositions[i] is the minimum number of shares of the asset i that is required to purchase when the asset i is included in the portfolio (usual values are the same as for assetsSizeLots)

        assets_size_lots : typing.Optional[typing.Sequence[float]]
            assetsSizeLots[i] is the number of shares by which it is required to purchase the asset i (usual values are 1 if the asset needs to be purchased share by share, 100 if the asset needs to be purchased by an integer multiple of 100 shares, and 1/1000000 - e.g. for Robinhood broker - if the asset can be purchased by fractional shares)

        assets_weights : typing.Optional[typing.Sequence[float]]
            assetsWeights[i] is the desired weight of the asset i in the portfolio, in percentage (can be null to indicate no specific desire)

        maximum_assets_groups_weights : typing.Optional[typing.Sequence[float]]
            maximumAssetsGroupsWeights[k] is the maximum desired weight of the assets group k in the portfolio, in percentage (can be null to indicate no specific desire); requires assetsGroups to be present

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioConstructionInvestableResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_construction.investable_portfolio(
            assets=4,
            assets_groups=[[1, 2], [3, 4]],
            assets_groups_weights=[0.4, 0.4],
            assets_prices=[10.0, 25.0, 100.0, 500.0],
            assets_weights=[0.2, 1.1, 1.1, 1.1],
            portfolio_value=10000.0,
        )
        """
        _response = self._raw_client.investable_portfolio(
            assets=assets,
            assets_prices=assets_prices,
            portfolio_value=portfolio_value,
            assets_groups=assets_groups,
            assets_groups_weights=assets_groups_weights,
            assets_minimum_notional_values=assets_minimum_notional_values,
            assets_minimum_positions=assets_minimum_positions,
            assets_size_lots=assets_size_lots,
            assets_weights=assets_weights,
            maximum_assets_groups_weights=maximum_assets_groups_weights,
            request_options=request_options,
        )
        return _response.data

    def mimicking_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem],
        benchmark_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioConstructionMimickingRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioConstructionMimickingResponse:
        """
        Construct a portfolio as close as possible, in terms of returns, to a benchmark, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
        * Konstantinos Benidis, Yiyong Feng, Daniel P. Palomar, Optimization Methods for Financial Index Tracking: From Theory to Practice, now publishers Inc (7 juin 2018)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem]

        benchmark_returns : typing.Sequence[float]
            benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the assetReturns arrays

        constraints : typing.Optional[PostPortfolioConstructionMimickingRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioConstructionMimickingResponse
            OK

        Examples
        --------
        from fern.portfolio_construction import (
            PostPortfolioConstructionMimickingRequestAssetsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_construction.mimicking_portfolio(
            assets=[
                PostPortfolioConstructionMimickingRequestAssetsItem(
                    asset_returns=[0.01, 0.02, 0.03],
                ),
                PostPortfolioConstructionMimickingRequestAssetsItem(
                    asset_returns=[-0.01, -0.02, -0.03],
                ),
            ],
            benchmark_returns=[0.0, 0.0, 0.0],
        )
        """
        _response = self._raw_client.mimicking_portfolio(
            assets=assets, benchmark_returns=benchmark_returns, constraints=constraints, request_options=request_options
        )
        return _response.data

    def random_portfolio(
        self,
        *,
        assets: int,
        constraints: typing.Optional[PostPortfolioConstructionRandomRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioConstructionRandomResponse:
        """
        Construct one or several random portfolio(s), optionally subject to:
        * Minimum and maximum weights constraints
        * Minimum and maximum portfolio exposure constraints

        > Because of the nature of the endpoint, subsequent calls with the same input data will result in different output data.

        References
        * [William Thornton Shaw, Monte Carlo Portfolio Optimization for General Investor Risk-Return Objectives and Arbitrary Return Distributions: A Solution for Long-Only Portfolios](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1680224)

        Parameters
        ----------
        assets : int
            The number of assets

        constraints : typing.Optional[PostPortfolioConstructionRandomRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to construct

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioConstructionRandomResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_construction.random_portfolio(
            assets=3,
            portfolios=2,
        )
        """
        _response = self._raw_client.random_portfolio(
            assets=assets, constraints=constraints, portfolios=portfolios, request_options=request_options
        )
        return _response.data


class AsyncPortfolioConstructionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioConstructionClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioConstructionClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioConstructionClient
        """
        return self._raw_client

    async def investable_portfolio(
        self,
        *,
        assets: int,
        assets_prices: typing.Sequence[float],
        portfolio_value: float,
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        assets_groups_weights: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_minimum_notional_values: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_minimum_positions: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_size_lots: typing.Optional[typing.Sequence[float]] = OMIT,
        assets_weights: typing.Optional[typing.Sequence[float]] = OMIT,
        maximum_assets_groups_weights: typing.Optional[typing.Sequence[float]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioConstructionInvestableResponse:
        """
        Compute an investable portfolio as close as possible, in terms of assets weights, to a desired portfolio, taking into account:
        * The desired assets weights
        * The desired assets groups weights
        * The desired maximum assets groups weights
        * The prices of the assets
        * The portfolio value
        * The requirement to purchase some assets by round lots or by odd lots
        * The possibility to purchase some assets by a fractional quantity of shares
        * The requirement to purchase a minimum number of shares, or a minimum monetary value, for some assets

        References
        * [Steiner, Andreas, Accuracy and Rounding in Portfolio Construction](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2261131)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_prices : typing.Sequence[float]
            assetsPrices[i] is the price of the asset i

        portfolio_value : float
            The monetary value of the portfolio

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        assets_groups_weights : typing.Optional[typing.Sequence[float]]
            assetsGroupsWeights[i] is the desired weight of the assets group k in the portfolio, in percentage (can be null to indicate no specific desire); requires assetsGroups to be present

        assets_minimum_notional_values : typing.Optional[typing.Sequence[float]]
            assetsMinimumNotionalValues[i] is the minimum monetary value that the position in the asset i is required to represent when the asset i is included in the portfolio

        assets_minimum_positions : typing.Optional[typing.Sequence[float]]
            assetsMinimumPositions[i] is the minimum number of shares of the asset i that is required to purchase when the asset i is included in the portfolio (usual values are the same as for assetsSizeLots)

        assets_size_lots : typing.Optional[typing.Sequence[float]]
            assetsSizeLots[i] is the number of shares by which it is required to purchase the asset i (usual values are 1 if the asset needs to be purchased share by share, 100 if the asset needs to be purchased by an integer multiple of 100 shares, and 1/1000000 - e.g. for Robinhood broker - if the asset can be purchased by fractional shares)

        assets_weights : typing.Optional[typing.Sequence[float]]
            assetsWeights[i] is the desired weight of the asset i in the portfolio, in percentage (can be null to indicate no specific desire)

        maximum_assets_groups_weights : typing.Optional[typing.Sequence[float]]
            maximumAssetsGroupsWeights[k] is the maximum desired weight of the assets group k in the portfolio, in percentage (can be null to indicate no specific desire); requires assetsGroups to be present

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioConstructionInvestableResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_construction.investable_portfolio(
                assets=4,
                assets_groups=[[1, 2], [3, 4]],
                assets_groups_weights=[0.4, 0.4],
                assets_prices=[10.0, 25.0, 100.0, 500.0],
                assets_weights=[0.2, 1.1, 1.1, 1.1],
                portfolio_value=10000.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.investable_portfolio(
            assets=assets,
            assets_prices=assets_prices,
            portfolio_value=portfolio_value,
            assets_groups=assets_groups,
            assets_groups_weights=assets_groups_weights,
            assets_minimum_notional_values=assets_minimum_notional_values,
            assets_minimum_positions=assets_minimum_positions,
            assets_size_lots=assets_size_lots,
            assets_weights=assets_weights,
            maximum_assets_groups_weights=maximum_assets_groups_weights,
            request_options=request_options,
        )
        return _response.data

    async def mimicking_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem],
        benchmark_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioConstructionMimickingRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioConstructionMimickingResponse:
        """
        Construct a portfolio as close as possible, in terms of returns, to a benchmark, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraints

        References
        * Konstantinos Benidis, Yiyong Feng, Daniel P. Palomar, Optimization Methods for Financial Index Tracking: From Theory to Practice, now publishers Inc (7 juin 2018)

        Parameters
        ----------
        assets : typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem]

        benchmark_returns : typing.Sequence[float]
            benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the assetReturns arrays

        constraints : typing.Optional[PostPortfolioConstructionMimickingRequestConstraints]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioConstructionMimickingResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_construction import (
            PostPortfolioConstructionMimickingRequestAssetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_construction.mimicking_portfolio(
                assets=[
                    PostPortfolioConstructionMimickingRequestAssetsItem(
                        asset_returns=[0.01, 0.02, 0.03],
                    ),
                    PostPortfolioConstructionMimickingRequestAssetsItem(
                        asset_returns=[-0.01, -0.02, -0.03],
                    ),
                ],
                benchmark_returns=[0.0, 0.0, 0.0],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.mimicking_portfolio(
            assets=assets, benchmark_returns=benchmark_returns, constraints=constraints, request_options=request_options
        )
        return _response.data

    async def random_portfolio(
        self,
        *,
        assets: int,
        constraints: typing.Optional[PostPortfolioConstructionRandomRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioConstructionRandomResponse:
        """
        Construct one or several random portfolio(s), optionally subject to:
        * Minimum and maximum weights constraints
        * Minimum and maximum portfolio exposure constraints

        > Because of the nature of the endpoint, subsequent calls with the same input data will result in different output data.

        References
        * [William Thornton Shaw, Monte Carlo Portfolio Optimization for General Investor Risk-Return Objectives and Arbitrary Return Distributions: A Solution for Long-Only Portfolios](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1680224)

        Parameters
        ----------
        assets : int
            The number of assets

        constraints : typing.Optional[PostPortfolioConstructionRandomRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to construct

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioConstructionRandomResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_construction.random_portfolio(
                assets=3,
                portfolios=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.random_portfolio(
            assets=assets, constraints=constraints, portfolios=portfolios, request_options=request_options
        )
        return _response.data
