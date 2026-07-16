

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawPortfolioAnalysisSharpeRatioClient, RawPortfolioAnalysisSharpeRatioClient
from .types.post_portfolio_analysis_sharpe_ratio_bias_adjusted_request_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_sharpe_ratio_bias_adjusted_response import (
    PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse,
)
from .types.post_portfolio_analysis_sharpe_ratio_confidence_interval_request_confidence_interval_type import (
    PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType,
)
from .types.post_portfolio_analysis_sharpe_ratio_confidence_interval_request_portfolios_item import (
    PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_sharpe_ratio_confidence_interval_response import (
    PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse,
)
from .types.post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_request import (
    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
)
from .types.post_portfolio_analysis_sharpe_ratio_probabilistic_minimum_track_record_length_response import (
    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse,
)
from .types.post_portfolio_analysis_sharpe_ratio_probabilistic_request import (
    PostPortfolioAnalysisSharpeRatioProbabilisticRequest,
)
from .types.post_portfolio_analysis_sharpe_ratio_probabilistic_response import (
    PostPortfolioAnalysisSharpeRatioProbabilisticResponse,
)
from .types.post_portfolio_analysis_sharpe_ratio_request import PostPortfolioAnalysisSharpeRatioRequest
from .types.post_portfolio_analysis_sharpe_ratio_response import PostPortfolioAnalysisSharpeRatioResponse


OMIT = typing.cast(typing.Any, ...)


class PortfolioAnalysisSharpeRatioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawPortfolioAnalysisSharpeRatioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawPortfolioAnalysisSharpeRatioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawPortfolioAnalysisSharpeRatioClient
        """
        return self._raw_client

    def sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioResponse:
        """
        Compute the Sharpe ratio of one or several portfolio(s) from either:
        * Portfolio assets arithmetic returns and assets covariance matrix
        * Portfolio values

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisSharpeRatioRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioRequestAssets,
            PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis_sharpe_ratio.sharpe_ratio(
            request=PostPortfolioAnalysisSharpeRatioRequestAssets(
                assets=2,
                assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                assets_returns=[0.01, 0.05],
                portfolios=[
                    PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem(
                        assets_weights=[1.0, 0.0],
                    ),
                    PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem(
                        assets_weights=[0.0, 1.0],
                    ),
                ],
                risk_free_rate=0.0,
            ),
        )
        """
        _response = self._raw_client.sharpe_ratio(request=request, request_options=request_options)
        return _response.data

    def bias_adjusted_sharpe_ratio(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse:
        """
        Compute the Sharpe ratio of one or several portfolio(s), adjusted for small sample bias.

        References
        * [Opdyke, J., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis_sharpe_ratio.bias_adjusted_sharpe_ratio(
            portfolios=[
                PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.bias_adjusted_sharpe_ratio(
            portfolios=portfolios, risk_free_rate=risk_free_rate, request_options=request_options
        )
        return _response.data

    def sharpe_ratio_confidence_interval(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem],
        risk_free_rate: float,
        confidence_interval_type: typing.Optional[
            PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType
        ] = OMIT,
        confidence_level: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse:
        """
        Build a confidence interval for the Sharpe ratio of one or several portfolio(s).

        References
        * [Opdyke, J.D., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        confidence_interval_type : typing.Optional[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType]
            The type of confidence interval to build

        confidence_level : typing.Optional[float]
            The confidence level of the confidence interval to build, in percentage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType,
            PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis_sharpe_ratio.sharpe_ratio_confidence_interval(
            confidence_interval_type=PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType.TWO_SIDED,
            confidence_level=0.99,
            portfolios=[
                PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem(
                    portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                )
            ],
            risk_free_rate=0.0,
        )
        """
        _response = self._raw_client.sharpe_ratio_confidence_interval(
            portfolios=portfolios,
            risk_free_rate=risk_free_rate,
            confidence_interval_type=confidence_interval_type,
            confidence_level=confidence_level,
            request_options=request_options,
        )
        return _response.data

    def probabilistic_sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioProbabilisticResponse:
        """
        Compute the probabilistic Sharpe ratio of one or several portfolio(s).

        References
        * [Opdyke, J.D., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)
        * [Bailey, David H. and Lopez de Prado, Marcos, The Sharpe Ratio Efficient Frontier (April 1, 2012). Journal of Risk, Vol. 15, No. 2, Winter 2012/13](https://ssrn.com/abstract=1821643)

        Parameters
        ----------
        request : PostPortfolioAnalysisSharpeRatioProbabilisticRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioProbabilisticResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues,
            PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis_sharpe_ratio.probabilistic_sharpe_ratio(
            request=PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues(
                benchmark_values=[100.0, 101.0, 98.0, 102.0, 95.0, 90.0],
                portfolios=[
                    PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
                risk_free_rate=0.0,
            ),
        )
        """
        _response = self._raw_client.probabilistic_sharpe_ratio(request=request, request_options=request_options)
        return _response.data

    def minimum_track_record_length(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse:
        """
        Compute the minimum track record length of one or several portfolio(s).

        References
        * [Bailey, David H. and Lopez de Prado, Marcos, The Sharpe Ratio Efficient Frontier (April 1, 2012). Journal of Risk, Vol. 15, No. 2, Winter 2012/13](https://ssrn.com/abstract=1821643)

        Parameters
        ----------
        request : PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse
            OK

        Examples
        --------
        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues,
            PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.portfolio_analysis_sharpe_ratio.minimum_track_record_length(
            request=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues(
                benchmark_values=[100.0, 101.0, 98.0, 85.0, 75.0, 65.0],
                portfolios=[
                    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
                risk_free_rate=0.0,
            ),
        )
        """
        _response = self._raw_client.minimum_track_record_length(request=request, request_options=request_options)
        return _response.data


class AsyncPortfolioAnalysisSharpeRatioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawPortfolioAnalysisSharpeRatioClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawPortfolioAnalysisSharpeRatioClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawPortfolioAnalysisSharpeRatioClient
        """
        return self._raw_client

    async def sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioResponse:
        """
        Compute the Sharpe ratio of one or several portfolio(s) from either:
        * Portfolio assets arithmetic returns and assets covariance matrix
        * Portfolio values

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisSharpeRatioRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioRequestAssets,
            PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis_sharpe_ratio.sharpe_ratio(
                request=PostPortfolioAnalysisSharpeRatioRequestAssets(
                    assets=2,
                    assets_covariance_matrix=[[0.0025, 0.0005], [0.0005, 0.01]],
                    assets_returns=[0.01, 0.05],
                    portfolios=[
                        PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem(
                            assets_weights=[1.0, 0.0],
                        ),
                        PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem(
                            assets_weights=[0.0, 1.0],
                        ),
                    ],
                    risk_free_rate=0.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sharpe_ratio(request=request, request_options=request_options)
        return _response.data

    async def bias_adjusted_sharpe_ratio(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse:
        """
        Compute the Sharpe ratio of one or several portfolio(s), adjusted for small sample bias.

        References
        * [Opdyke, J., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis_sharpe_ratio.bias_adjusted_sharpe_ratio(
                portfolios=[
                    PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.bias_adjusted_sharpe_ratio(
            portfolios=portfolios, risk_free_rate=risk_free_rate, request_options=request_options
        )
        return _response.data

    async def sharpe_ratio_confidence_interval(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem],
        risk_free_rate: float,
        confidence_interval_type: typing.Optional[
            PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType
        ] = OMIT,
        confidence_level: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse:
        """
        Build a confidence interval for the Sharpe ratio of one or several portfolio(s).

        References
        * [Opdyke, J.D., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        confidence_interval_type : typing.Optional[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType]
            The type of confidence interval to build

        confidence_level : typing.Optional[float]
            The confidence level of the confidence interval to build, in percentage

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType,
            PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis_sharpe_ratio.sharpe_ratio_confidence_interval(
                confidence_interval_type=PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType.TWO_SIDED,
                confidence_level=0.99,
                portfolios=[
                    PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem(
                        portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                    )
                ],
                risk_free_rate=0.0,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.sharpe_ratio_confidence_interval(
            portfolios=portfolios,
            risk_free_rate=risk_free_rate,
            confidence_interval_type=confidence_interval_type,
            confidence_level=confidence_level,
            request_options=request_options,
        )
        return _response.data

    async def probabilistic_sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioProbabilisticResponse:
        """
        Compute the probabilistic Sharpe ratio of one or several portfolio(s).

        References
        * [Opdyke, J.D., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)
        * [Bailey, David H. and Lopez de Prado, Marcos, The Sharpe Ratio Efficient Frontier (April 1, 2012). Journal of Risk, Vol. 15, No. 2, Winter 2012/13](https://ssrn.com/abstract=1821643)

        Parameters
        ----------
        request : PostPortfolioAnalysisSharpeRatioProbabilisticRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioProbabilisticResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues,
            PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis_sharpe_ratio.probabilistic_sharpe_ratio(
                request=PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues(
                    benchmark_values=[100.0, 101.0, 98.0, 102.0, 95.0, 90.0],
                    portfolios=[
                        PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem(
                            portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                        )
                    ],
                    risk_free_rate=0.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.probabilistic_sharpe_ratio(request=request, request_options=request_options)
        return _response.data

    async def minimum_track_record_length(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse:
        """
        Compute the minimum track record length of one or several portfolio(s).

        References
        * [Bailey, David H. and Lopez de Prado, Marcos, The Sharpe Ratio Efficient Frontier (April 1, 2012). Journal of Risk, Vol. 15, No. 2, Winter 2012/13](https://ssrn.com/abstract=1821643)

        Parameters
        ----------
        request : PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse
            OK

        Examples
        --------
        import asyncio

        from fern.portfolio_analysis_sharpe_ratio import (
            PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues,
            PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.portfolio_analysis_sharpe_ratio.minimum_track_record_length(
                request=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues(
                    benchmark_values=[100.0, 101.0, 98.0, 85.0, 75.0, 65.0],
                    portfolios=[
                        PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem(
                            portfolio_values=[100.0, 95.0, 100.0, 90.0, 85.0, 70.0],
                        )
                    ],
                    risk_free_rate=0.0,
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.minimum_track_record_length(request=request, request_options=request_options)
        return _response.data
