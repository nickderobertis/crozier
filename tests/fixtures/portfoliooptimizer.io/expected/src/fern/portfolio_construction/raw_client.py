

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPortfolioConstructionClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> HttpResponse[PostPortfolioConstructionInvestableResponse]:
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
        HttpResponse[PostPortfolioConstructionInvestableResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/construction/investable",
            method="POST",
            json={
                "assets": assets,
                "assetsGroups": assets_groups,
                "assetsGroupsWeights": assets_groups_weights,
                "assetsMinimumNotionalValues": assets_minimum_notional_values,
                "assetsMinimumPositions": assets_minimum_positions,
                "assetsPrices": assets_prices,
                "assetsSizeLots": assets_size_lots,
                "assetsWeights": assets_weights,
                "maximumAssetsGroupsWeights": maximum_assets_groups_weights,
                "portfolioValue": portfolio_value,
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
                    PostPortfolioConstructionInvestableResponse,
                    parse_obj_as(
                        type_=PostPortfolioConstructionInvestableResponse,
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

    def mimicking_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem],
        benchmark_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioConstructionMimickingRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioConstructionMimickingResponse]:
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
        HttpResponse[PostPortfolioConstructionMimickingResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/construction/mimicking",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem],
                    direction="write",
                ),
                "benchmarkReturns": benchmark_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioConstructionMimickingRequestConstraints,
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
                    PostPortfolioConstructionMimickingResponse,
                    parse_obj_as(
                        type_=PostPortfolioConstructionMimickingResponse,
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

    def random_portfolio(
        self,
        *,
        assets: int,
        constraints: typing.Optional[PostPortfolioConstructionRandomRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioConstructionRandomResponse]:
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
        HttpResponse[PostPortfolioConstructionRandomResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/construction/random",
            method="POST",
            json={
                "assets": assets,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=PostPortfolioConstructionRandomRequestConstraints, direction="write"
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
                    PostPortfolioConstructionRandomResponse,
                    parse_obj_as(
                        type_=PostPortfolioConstructionRandomResponse,
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


class AsyncRawPortfolioConstructionClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

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
    ) -> AsyncHttpResponse[PostPortfolioConstructionInvestableResponse]:
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
        AsyncHttpResponse[PostPortfolioConstructionInvestableResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/construction/investable",
            method="POST",
            json={
                "assets": assets,
                "assetsGroups": assets_groups,
                "assetsGroupsWeights": assets_groups_weights,
                "assetsMinimumNotionalValues": assets_minimum_notional_values,
                "assetsMinimumPositions": assets_minimum_positions,
                "assetsPrices": assets_prices,
                "assetsSizeLots": assets_size_lots,
                "assetsWeights": assets_weights,
                "maximumAssetsGroupsWeights": maximum_assets_groups_weights,
                "portfolioValue": portfolio_value,
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
                    PostPortfolioConstructionInvestableResponse,
                    parse_obj_as(
                        type_=PostPortfolioConstructionInvestableResponse,
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

    async def mimicking_portfolio(
        self,
        *,
        assets: typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem],
        benchmark_returns: typing.Sequence[float],
        constraints: typing.Optional[PostPortfolioConstructionMimickingRequestConstraints] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioConstructionMimickingResponse]:
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
        AsyncHttpResponse[PostPortfolioConstructionMimickingResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/construction/mimicking",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioConstructionMimickingRequestAssetsItem],
                    direction="write",
                ),
                "benchmarkReturns": benchmark_returns,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints,
                    annotation=PostPortfolioConstructionMimickingRequestConstraints,
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
                    PostPortfolioConstructionMimickingResponse,
                    parse_obj_as(
                        type_=PostPortfolioConstructionMimickingResponse,
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

    async def random_portfolio(
        self,
        *,
        assets: int,
        constraints: typing.Optional[PostPortfolioConstructionRandomRequestConstraints] = OMIT,
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioConstructionRandomResponse]:
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
        AsyncHttpResponse[PostPortfolioConstructionRandomResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/construction/random",
            method="POST",
            json={
                "assets": assets,
                "constraints": convert_and_respect_annotation_metadata(
                    object_=constraints, annotation=PostPortfolioConstructionRandomRequestConstraints, direction="write"
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
                    PostPortfolioConstructionRandomResponse,
                    parse_obj_as(
                        type_=PostPortfolioConstructionRandomResponse,
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
