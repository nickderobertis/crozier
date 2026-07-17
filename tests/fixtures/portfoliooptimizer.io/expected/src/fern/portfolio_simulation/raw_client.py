

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawPortfolioSimulationClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def drift_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioSimulationRebalancingDriftWeightResponse]:
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
        HttpResponse[PostPortfolioSimulationRebalancingDriftWeightResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/simulation/rebalancing/drift-weight",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem],
                    direction="write",
                ),
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem],
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
                    PostPortfolioSimulationRebalancingDriftWeightResponse,
                    parse_obj_as(
                        type_=PostPortfolioSimulationRebalancingDriftWeightResponse,
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

    def fixed_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioSimulationRebalancingFixedWeightResponse]:
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
        HttpResponse[PostPortfolioSimulationRebalancingFixedWeightResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/simulation/rebalancing/fixed-weight",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem],
                    direction="write",
                ),
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem],
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
                    PostPortfolioSimulationRebalancingFixedWeightResponse,
                    parse_obj_as(
                        type_=PostPortfolioSimulationRebalancingFixedWeightResponse,
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

    def random_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem],
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioSimulationRebalancingRandomWeightResponse]:
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
        HttpResponse[PostPortfolioSimulationRebalancingRandomWeightResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/simulation/rebalancing/random-weight",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem],
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
                    PostPortfolioSimulationRebalancingRandomWeightResponse,
                    parse_obj_as(
                        type_=PostPortfolioSimulationRebalancingRandomWeightResponse,
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


class AsyncRawPortfolioSimulationClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def drift_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioSimulationRebalancingDriftWeightResponse]:
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
        AsyncHttpResponse[PostPortfolioSimulationRebalancingDriftWeightResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/simulation/rebalancing/drift-weight",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem],
                    direction="write",
                ),
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem],
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
                    PostPortfolioSimulationRebalancingDriftWeightResponse,
                    parse_obj_as(
                        type_=PostPortfolioSimulationRebalancingDriftWeightResponse,
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

    async def fixed_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem],
        portfolios: typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioSimulationRebalancingFixedWeightResponse]:
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
        AsyncHttpResponse[PostPortfolioSimulationRebalancingFixedWeightResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/simulation/rebalancing/fixed-weight",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem],
                    direction="write",
                ),
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem],
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
                    PostPortfolioSimulationRebalancingFixedWeightResponse,
                    parse_obj_as(
                        type_=PostPortfolioSimulationRebalancingFixedWeightResponse,
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

    async def random_weight_portfolio_rebalancing(
        self,
        *,
        assets: typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem],
        portfolios: typing.Optional[int] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioSimulationRebalancingRandomWeightResponse]:
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
        AsyncHttpResponse[PostPortfolioSimulationRebalancingRandomWeightResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/simulation/rebalancing/random-weight",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem],
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
                    PostPortfolioSimulationRebalancingRandomWeightResponse,
                    parse_obj_as(
                        type_=PostPortfolioSimulationRebalancingRandomWeightResponse,
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
