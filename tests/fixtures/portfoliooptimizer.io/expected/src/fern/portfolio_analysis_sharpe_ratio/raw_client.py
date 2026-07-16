

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
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


class RawPortfolioAnalysisSharpeRatioClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisSharpeRatioResponse]:
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
        HttpResponse[PostPortfolioAnalysisSharpeRatioResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisSharpeRatioRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisSharpeRatioResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def bias_adjusted_sharpe_ratio(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse]:
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
        HttpResponse[PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/bias-adjusted",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem],
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
                    PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> HttpResponse[PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse]:
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
        HttpResponse[PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/confidence-interval",
            method="POST",
            json={
                "confidenceIntervalType": confidence_interval_type,
                "confidenceLevel": confidence_level,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem],
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
                    PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def probabilistic_sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticResponse]:
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
        HttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/probabilistic",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisSharpeRatioProbabilisticRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisSharpeRatioProbabilisticResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioProbabilisticResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def minimum_track_record_length(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse]:
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
        HttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/probabilistic/minimum-track-record-length",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawPortfolioAnalysisSharpeRatioClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioResponse]:
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
        AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisSharpeRatioRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisSharpeRatioResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def bias_adjusted_sharpe_ratio(
        self,
        *,
        portfolios: typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem],
        risk_free_rate: float,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse]:
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
        AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/bias-adjusted",
            method="POST",
            json={
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem],
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
                    PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

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
    ) -> AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse]:
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
        AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/confidence-interval",
            method="POST",
            json={
                "confidenceIntervalType": confidence_interval_type,
                "confidenceLevel": confidence_level,
                "portfolios": convert_and_respect_annotation_metadata(
                    object_=portfolios,
                    annotation=typing.Sequence[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem],
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
                    PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def probabilistic_sharpe_ratio(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticResponse]:
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
        AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/probabilistic",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostPortfolioAnalysisSharpeRatioProbabilisticRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisSharpeRatioProbabilisticResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioProbabilisticResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def minimum_track_record_length(
        self,
        *,
        request: PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse]:
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
        AsyncHttpResponse[PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "portfolio/analysis/sharpe-ratio/probabilistic/minimum-track-record-length",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request,
                annotation=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest,
                direction="write",
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse,
                    parse_obj_as(
                        type_=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
