

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_portfolio_analysis_alpha_request import PostPortfolioAnalysisAlphaRequest
from .types.post_portfolio_analysis_alpha_response import PostPortfolioAnalysisAlphaResponse
from .types.post_portfolio_analysis_beta_request import PostPortfolioAnalysisBetaRequest
from .types.post_portfolio_analysis_beta_response import PostPortfolioAnalysisBetaResponse
from .types.post_portfolio_analysis_conditional_value_at_risk_request_portfolios_item import (
    PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_conditional_value_at_risk_response import (
    PostPortfolioAnalysisConditionalValueAtRiskResponse,
)
from .types.post_portfolio_analysis_contributions_return_request_portfolios_item import (
    PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_contributions_return_response import (
    PostPortfolioAnalysisContributionsReturnResponse,
)
from .types.post_portfolio_analysis_contributions_risk_request_portfolios_item import (
    PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_contributions_risk_response import PostPortfolioAnalysisContributionsRiskResponse
from .types.post_portfolio_analysis_correlation_spectrum_request import PostPortfolioAnalysisCorrelationSpectrumRequest
from .types.post_portfolio_analysis_correlation_spectrum_response import (
    PostPortfolioAnalysisCorrelationSpectrumResponse,
)
from .types.post_portfolio_analysis_diversification_ratio_request import (
    PostPortfolioAnalysisDiversificationRatioRequest,
)
from .types.post_portfolio_analysis_diversification_ratio_response import (
    PostPortfolioAnalysisDiversificationRatioResponse,
)
from .types.post_portfolio_analysis_drawdowns_request_portfolios_item import (
    PostPortfolioAnalysisDrawdownsRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_drawdowns_response import PostPortfolioAnalysisDrawdownsResponse
from .types.post_portfolio_analysis_effective_number_of_bets_request_factors_extraction_method import (
    PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod,
)
from .types.post_portfolio_analysis_effective_number_of_bets_request_portfolios_item import (
    PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_effective_number_of_bets_response import (
    PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
)
from .types.post_portfolio_analysis_factors_exposures_request_factors_item import (
    PostPortfolioAnalysisFactorsExposuresRequestFactorsItem,
)
from .types.post_portfolio_analysis_factors_exposures_request_portfolios_item import (
    PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_factors_exposures_response import PostPortfolioAnalysisFactorsExposuresResponse
from .types.post_portfolio_analysis_mean_variance_efficient_frontier_request_constraints import (
    PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
)
from .types.post_portfolio_analysis_mean_variance_efficient_frontier_response import (
    PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
)
from .types.post_portfolio_analysis_mean_variance_minimum_variance_frontier_request_constraints import (
    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
)
from .types.post_portfolio_analysis_mean_variance_minimum_variance_frontier_response import (
    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
)
from .types.post_portfolio_analysis_return_request import PostPortfolioAnalysisReturnRequest
from .types.post_portfolio_analysis_return_response import PostPortfolioAnalysisReturnResponse
from .types.post_portfolio_analysis_returns_average_request_portfolios_item import (
    PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_returns_average_response import PostPortfolioAnalysisReturnsAverageResponse
from .types.post_portfolio_analysis_tracking_error_request_portfolios_item import (
    PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_tracking_error_response import PostPortfolioAnalysisTrackingErrorResponse
from .types.post_portfolio_analysis_ulcer_index_request_portfolios_item import (
    PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_ulcer_index_response import PostPortfolioAnalysisUlcerIndexResponse
from .types.post_portfolio_analysis_ulcer_performance_index_request_portfolios_item import (
    PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_ulcer_performance_index_response import (
    PostPortfolioAnalysisUlcerPerformanceIndexResponse,
)
from .types.post_portfolio_analysis_value_at_risk_request_portfolios_item import (
    PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem,
)
from .types.post_portfolio_analysis_value_at_risk_response import PostPortfolioAnalysisValueAtRiskResponse
from .types.post_portfolio_analysis_volatility_request import PostPortfolioAnalysisVolatilityRequest
from .types.post_portfolio_analysis_volatility_response import PostPortfolioAnalysisVolatilityResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPortfolioAnalysisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def alpha(
        self, *, request: PostPortfolioAnalysisAlphaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostPortfolioAnalysisAlphaResponse]:
        """
        Compute the Jensen’s alpha of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisAlphaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisAlphaResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/alpha",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisAlphaRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisAlphaResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisAlphaResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def beta(
        self, *, request: PostPortfolioAnalysisBetaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostPortfolioAnalysisBetaResponse]:
        """
        Compute the beta of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisBetaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisBetaResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/beta",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisBetaRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisBetaResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisBetaResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def conditional_value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisConditionalValueAtRiskResponse]:
        """
        Compute the conditional value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The conditional value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisConditionalValueAtRiskResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/conditional-value-at-risk",
            method="POST",
            json={
                "alpha": alpha,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisConditionalValueAtRiskResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisConditionalValueAtRiskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def return_contributions(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisContributionsReturnResponse]:
        """
        Perform a return contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisContributionsReturnResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/contributions/return",
            method="POST",
            json={
                "assets": assets,
                "assetsGroups": assets_groups,
                "assetsReturns": assets_returns,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisContributionsReturnResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisContributionsReturnResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def risk_contributions(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisContributionsRiskResponse]:
        """
        Perform a risk contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisContributionsRiskResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/contributions/risk",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsGroups": assets_groups,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisContributionsRiskResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisContributionsRiskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def correlation_spectrum(
        self,
        *,
        request: PostPortfolioAnalysisCorrelationSpectrumRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisCorrelationSpectrumResponse]:
        """
        Compute the correlation spectrum of one or several portfolio(s).

        References
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisCorrelationSpectrumRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisCorrelationSpectrumResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/correlation-spectrum",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisCorrelationSpectrumRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisCorrelationSpectrumResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisCorrelationSpectrumResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def diversification_ratio(
        self,
        *,
        request: PostPortfolioAnalysisDiversificationRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisDiversificationRatioResponse]:
        """
        Compute the diversification ratio of one or several portfolio(s).

        References
        * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisDiversificationRatioRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisDiversificationRatioResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/diversification-ratio",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisDiversificationRatioRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisDiversificationRatioResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisDiversificationRatioResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def drawdowns(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisDrawdownsResponse]:
        """
        Compute the drawdown function - also called the underwater equity curve -, as well as the worst 10 drawdowns of one or several portfolio(s).

        References
        * [Wikipedia, Drawdown](https://en.wikipedia.org/wiki/Drawdown_(economics))

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisDrawdownsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/drawdowns",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisDrawdownsResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisDrawdownsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def effective_number_of_bets(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem],
        factors_extraction_method: typing.Optional[
            PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisEffectiveNumberOfBetsResponse]:
        """
        Compute the effective number of bets of one or several portfolio(s).

        References
        * [Meucci, Attilio and Santangelo, Alberto and Deguest, Romain, Risk Budgeting and Diversification Based on Optimized Uncorrelated Factors (November 10, 2015)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2276632)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem]

        factors_extraction_method : typing.Optional[PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod]
            The method used to extract the uncorrelated risk factors from the asset covariance matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisEffectiveNumberOfBetsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/effective-number-of-bets",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "factorsExtractionMethod": factors_extraction_method,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def factor_exposures(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem],
        factors: typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisFactorsExposuresResponse]:
        """
        Compute the exposures of one or several portfolio(s) to a set of factors, using a returns-based linear regression analysis.

        References
        * [Measuring Factor Exposures: Uses and Abuses, Ronen Israel and Adrienne Ross, The Journal of Alternative Investments Summer 2017, 20 (1) 10-25](https://jai.pm-research.com/content/20/1/10.short)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem]

        factors : typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisFactorsExposuresResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/factors/exposures",
            method="POST",
            json={
                "factors": convert_and_respect_annotation_metadata(
                    object_=factors,
                    annotation=typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem],
                    direction="write",
                ),
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisFactorsExposuresResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisFactorsExposuresResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mean_variance_efficient_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse]:
        """
        Compute the discretized mean-variance efficient frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance efficient frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/mean-variance/efficient-frontier",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
                    direction="write",
                ),
                "portfolios": portfolios,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def mean_variance_minimum_variance_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse]:
        """
        Compute the discretized mean-variance minimum variance frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        > This endpoint is similar to the endpoint [`/portfolio/analysis/mean-variance/efficient-frontier`](#post-/portfolio/analysis/mean-variance/efficient-frontier), because the mean-variance efficient frontier is the "top" portion of the mean-variance minimum variance frontier.

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance minimum variance frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/mean-variance/minimum-variance-frontier",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
                    direction="write",
                ),
                "portfolios": portfolios,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def arithmetic_return(
        self, *, request: PostPortfolioAnalysisReturnRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostPortfolioAnalysisReturnResponse]:
        """
        Compute the arithmetic return of one or several portfolio(s) from either:
        * Portfolio assets arithmetic returns
        * Portfolio values

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisReturnRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisReturnResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/return",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisReturnRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisReturnResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisReturnResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def arithmetic_average_return(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisReturnsAverageResponse]:
        """
        Compute the arithmetic average of the arithmetic return(s) of one or several portfolio(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisReturnsAverageResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/returns/average",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisReturnsAverageResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisReturnsAverageResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def tracking_error(
        self,
        *,
        benchmark_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisTrackingErrorResponse]:
        """
        Compute the tracking error between a benchmark and one or several portfolio(s).

        References
        * [Wikipedia, Tracking error](https://en.wikipedia.org/wiki/Tracking_error)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        benchmark_returns : typing.Sequence[float]
            benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays

        portfolios : typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisTrackingErrorResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/tracking-error",
            method="POST",
            json={
                "benchmarkReturns": benchmark_returns,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisTrackingErrorResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisTrackingErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ulcer_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisUlcerIndexResponse]:
        """
        Compute the Ulcer Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisUlcerIndexResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/ulcer-index",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem],
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisUlcerIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisUlcerIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def ulcer_performance_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisUlcerPerformanceIndexResponse]:
        """
        Compute the Ulcer Performance Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisUlcerPerformanceIndexResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/ulcer-performance-index",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem],
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisUlcerPerformanceIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisUlcerPerformanceIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisValueAtRiskResponse]:
        """
        Compute the value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisValueAtRiskResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/value-at-risk",
            method="POST",
            json={
                "alpha": alpha,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisValueAtRiskResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisValueAtRiskResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def volatility(
        self,
        *,
        request: PostPortfolioAnalysisVolatilityRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisVolatilityResponse]:
        """
        Compute the volatility (i.e., standard deviation) of one or several portfolio(s) from either:
        * Portfolio assets covariance matrix
        * Portfolio values

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Finance)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostPortfolioAnalysisVolatilityResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/volatility",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisVolatilityRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisVolatilityResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisVolatilityResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPortfolioAnalysisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def alpha(
        self, *, request: PostPortfolioAnalysisAlphaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostPortfolioAnalysisAlphaResponse]:
        """
        Compute the Jensen’s alpha of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisAlphaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisAlphaResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/alpha",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisAlphaRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisAlphaResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisAlphaResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def beta(
        self, *, request: PostPortfolioAnalysisBetaRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostPortfolioAnalysisBetaResponse]:
        """
        Compute the beta of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        request : PostPortfolioAnalysisBetaRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisBetaResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/beta",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisBetaRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisBetaResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisBetaResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def conditional_value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisConditionalValueAtRiskResponse]:
        """
        Compute the conditional value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The conditional value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisConditionalValueAtRiskResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/conditional-value-at-risk",
            method="POST",
            json={
                "alpha": alpha,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisConditionalValueAtRiskResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisConditionalValueAtRiskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def return_contributions(
        self,
        *,
        assets: int,
        assets_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisContributionsReturnResponse]:
        """
        Perform a return contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisContributionsReturnResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/contributions/return",
            method="POST",
            json={
                "assets": assets,
                "assetsGroups": assets_groups,
                "assetsReturns": assets_returns,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisContributionsReturnResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisContributionsReturnResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def risk_contributions(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem],
        assets_groups: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisContributionsRiskResponse]:
        """
        Perform a risk contribution analysis of one or several portfolio(s), optionally using groups of assets.

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem]

        assets_groups : typing.Optional[typing.Sequence[typing.Sequence[int]]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisContributionsRiskResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/contributions/risk",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsGroups": assets_groups,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisContributionsRiskResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisContributionsRiskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def correlation_spectrum(
        self,
        *,
        request: PostPortfolioAnalysisCorrelationSpectrumRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisCorrelationSpectrumResponse]:
        """
        Compute the correlation spectrum of one or several portfolio(s).

        References
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisCorrelationSpectrumRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisCorrelationSpectrumResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/correlation-spectrum",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisCorrelationSpectrumRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisCorrelationSpectrumResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisCorrelationSpectrumResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def diversification_ratio(
        self,
        *,
        request: PostPortfolioAnalysisDiversificationRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisDiversificationRatioResponse]:
        """
        Compute the diversification ratio of one or several portfolio(s).

        References
        * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)
        * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)

        Parameters
        ----------
        request : PostPortfolioAnalysisDiversificationRatioRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisDiversificationRatioResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/diversification-ratio",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisDiversificationRatioRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisDiversificationRatioResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisDiversificationRatioResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def drawdowns(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisDrawdownsResponse]:
        """
        Compute the drawdown function - also called the underwater equity curve -, as well as the worst 10 drawdowns of one or several portfolio(s).

        References
        * [Wikipedia, Drawdown](https://en.wikipedia.org/wiki/Drawdown_(economics))

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisDrawdownsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/drawdowns",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisDrawdownsResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisDrawdownsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def effective_number_of_bets(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        portfolios: typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem],
        factors_extraction_method: typing.Optional[
            PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisEffectiveNumberOfBetsResponse]:
        """
        Compute the effective number of bets of one or several portfolio(s).

        References
        * [Meucci, Attilio and Santangelo, Alberto and Deguest, Romain, Risk Budgeting and Diversification Based on Optimized Uncorrelated Factors (November 10, 2015)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2276632)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        portfolios : typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem]

        factors_extraction_method : typing.Optional[PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod]
            The method used to extract the uncorrelated risk factors from the asset covariance matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisEffectiveNumberOfBetsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/effective-number-of-bets",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "factorsExtractionMethod": factors_extraction_method,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisEffectiveNumberOfBetsResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def factor_exposures(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem],
        factors: typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisFactorsExposuresResponse]:
        """
        Compute the exposures of one or several portfolio(s) to a set of factors, using a returns-based linear regression analysis.

        References
        * [Measuring Factor Exposures: Uses and Abuses, Ronen Israel and Adrienne Ross, The Journal of Alternative Investments Summer 2017, 20 (1) 10-25](https://jai.pm-research.com/content/20/1/10.short)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem]

        factors : typing.Optional[typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisFactorsExposuresResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/factors/exposures",
            method="POST",
            json={
                "factors": convert_and_respect_annotation_metadata(
                    object_=factors,
                    annotation=typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem],
                    direction="write",
                ),
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisFactorsExposuresResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisFactorsExposuresResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mean_variance_efficient_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse]:
        """
        Compute the discretized mean-variance efficient frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance efficient frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/mean-variance/efficient-frontier",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints,
                    direction="write",
                ),
                "portfolios": portfolios,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def mean_variance_minimum_variance_frontier(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse]:
        """
        Compute the discretized mean-variance minimum variance frontier associated to a list of assets, optionally subject to:
        * Minimum and maximum weights constraints
        * Maximum group weights constraints
        * Minimum and maximum portfolio exposure constraint

        > This endpoint is similar to the endpoint [`/portfolio/analysis/mean-variance/efficient-frontier`](#post-/portfolio/analysis/mean-variance/efficient-frontier), because the mean-variance efficient frontier is the "top" portion of the mean-variance minimum variance frontier.

        References
         * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the arithmetic return of asset i

        constraints : typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints]

        portfolios : typing.Optional[int]
            The number of portfolios to compute on the mean-variance minimum variance frontier

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/mean-variance/minimum-variance-frontier",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints,
                    direction="write",
                ),
                "portfolios": portfolios,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def arithmetic_return(
        self, *, request: PostPortfolioAnalysisReturnRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostPortfolioAnalysisReturnResponse]:
        """
        Compute the arithmetic return of one or several portfolio(s) from either:
        * Portfolio assets arithmetic returns
        * Portfolio values

        References
        * [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisReturnRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisReturnResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/return",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisReturnRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisReturnResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisReturnResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def arithmetic_average_return(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisReturnsAverageResponse]:
        """
        Compute the arithmetic average of the arithmetic return(s) of one or several portfolio(s).

        References
        * [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisReturnsAverageResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/returns/average",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisReturnsAverageResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisReturnsAverageResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def tracking_error(
        self,
        *,
        benchmark_returns: typing.Sequence[float],
        portfolios: typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisTrackingErrorResponse]:
        """
        Compute the tracking error between a benchmark and one or several portfolio(s).

        References
        * [Wikipedia, Tracking error](https://en.wikipedia.org/wiki/Tracking_error)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution

        Parameters
        ----------
        benchmark_returns : typing.Sequence[float]
            benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays

        portfolios : typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisTrackingErrorResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/tracking-error",
            method="POST",
            json={
                "benchmarkReturns": benchmark_returns,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisTrackingErrorResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisTrackingErrorResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ulcer_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisUlcerIndexResponse]:
        """
        Compute the Ulcer Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisUlcerIndexResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/ulcer-index",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem],
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisUlcerIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisUlcerIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def ulcer_performance_index(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisUlcerPerformanceIndexResponse]:
        """
        Compute the Ulcer Performance Index of one or several portfolio(s).

        References
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)

        Parameters
        ----------
        portfolios : typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem]

        risk_free_rate : float
            The risk free rate

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisUlcerPerformanceIndexResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/ulcer-performance-index",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem],
                    direction="write",
                ),
                "riskFreeRate": risk_free_rate,
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisUlcerPerformanceIndexResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisUlcerPerformanceIndexResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def value_at_risk(
        self,
        *,
        alpha: float,
        portfolios: typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisValueAtRiskResponse]:
        """
        Compute the value at risk of one or several portfolio(s) from portfolio values.

        References
        * [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
        * [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)

        Parameters
        ----------
        alpha : float
            The value at risk level

        portfolios : typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisValueAtRiskResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/value-at-risk",
            method="POST",
            json={
                "alpha": alpha,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem],
                    direction="write",
                ),
            },
            headers={
                "content-type": "application/json",
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisValueAtRiskResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisValueAtRiskResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def volatility(
        self,
        *,
        request: PostPortfolioAnalysisVolatilityRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisVolatilityResponse]:
        """
        Compute the volatility (i.e., standard deviation) of one or several portfolio(s) from either:
        * Portfolio assets covariance matrix
        * Portfolio values

        References
        * [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Finance)
        * Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
        * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.

        Parameters
        ----------
        request : PostPortfolioAnalysisVolatilityRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostPortfolioAnalysisVolatilityResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/volatility",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisVolatilityRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisVolatilityResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisVolatilityResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        except ValidationError as e:
            raise ParsingError(
                status_code=_response.status_code, headers=dict(_response.headers), body=_response.json(), cause=e
            )
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
