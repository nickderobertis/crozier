

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_analysis_absorption_ratio_request_assets_covariance_matrix_eigenvectors import (
    PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors,
)
from .types.post_assets_analysis_absorption_ratio_response import PostAssetsAnalysisAbsorptionRatioResponse
from .types.post_assets_analysis_turbulence_index_response import PostAssetsAnalysisTurbulenceIndexResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssetsAnalysisClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def absorption_ratio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_covariance_matrix_eigenvectors: typing.Optional[
            PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsAnalysisAbsorptionRatioResponse]:
        """
        Compute the absorption ratio associated to a universe of assets.

        References
        * [Mark Kritzman, Yuanzhen Li, Sebastien Page and Roberto Rigobon, Principal Components as a Measure of Systemic Risk, The Journal of Portfolio Management Summer 2011, 37 (4) 112-126](https://jpm.pm-research.com/content/37/4/112)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_covariance_matrix_eigenvectors : typing.Optional[PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsAnalysisAbsorptionRatioResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/analysis/absorption-ratio",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsCovarianceMatrixEigenvectors": convert_and_respect_annotation_metadata(
                    object_=assets_covariance_matrix_eigenvectors,
                    annotation=PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors,
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
                    PostAssetsAnalysisAbsorptionRatioResponse,
                    parse_obj_as(
                        type_=PostAssetsAnalysisAbsorptionRatioResponse,
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

    def turbulence_index(
        self,
        *,
        assets: int,
        assets_average_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsAnalysisTurbulenceIndexResponse]:
        """
        Compute the turbulence index associated to a universe of assets.

        References
        * [M. Kritzman, Y. Li, Skulls, Financial Turbulence, and Risk Management,Financial Analysts Journal, Volume 66, Number 5, Pages 30-41, Year 2010](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n5.3)
        * [Kinlaw, W., Turkington, D. Correlation surprise. J Asset Manag 14, 385–399 (2013)](https://link.springer.com/article/10.1057/jam.2013.27)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_average_returns : typing.Sequence[float]
            assetsAverageReturns[i] is the average return of asset i over an historical reference period

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j over an historical reference period

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the return of asset i over a period different from the historical reference period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsAnalysisTurbulenceIndexResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/analysis/turbulence-index",
            method="POST",
            json={
                "assets": assets,
                "assetsAverageReturns": assets_average_returns,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
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
                    PostAssetsAnalysisTurbulenceIndexResponse,
                    parse_obj_as(
                        type_=PostAssetsAnalysisTurbulenceIndexResponse,
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


class AsyncRawAssetsAnalysisClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def absorption_ratio(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_covariance_matrix_eigenvectors: typing.Optional[
            PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors
        ] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsAnalysisAbsorptionRatioResponse]:
        """
        Compute the absorption ratio associated to a universe of assets.

        References
        * [Mark Kritzman, Yuanzhen Li, Sebastien Page and Roberto Rigobon, Principal Components as a Measure of Systemic Risk, The Journal of Portfolio Management Summer 2011, 37 (4) 112-126](https://jpm.pm-research.com/content/37/4/112)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        assets_covariance_matrix_eigenvectors : typing.Optional[PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors]

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsAnalysisAbsorptionRatioResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/analysis/absorption-ratio",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsCovarianceMatrixEigenvectors": convert_and_respect_annotation_metadata(
                    object_=assets_covariance_matrix_eigenvectors,
                    annotation=PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors,
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
                    PostAssetsAnalysisAbsorptionRatioResponse,
                    parse_obj_as(
                        type_=PostAssetsAnalysisAbsorptionRatioResponse,
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

    async def turbulence_index(
        self,
        *,
        assets: int,
        assets_average_returns: typing.Sequence[float],
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        assets_returns: typing.Sequence[float],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsAnalysisTurbulenceIndexResponse]:
        """
        Compute the turbulence index associated to a universe of assets.

        References
        * [M. Kritzman, Y. Li, Skulls, Financial Turbulence, and Risk Management,Financial Analysts Journal, Volume 66, Number 5, Pages 30-41, Year 2010](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n5.3)
        * [Kinlaw, W., Turkington, D. Correlation surprise. J Asset Manag 14, 385–399 (2013)](https://link.springer.com/article/10.1057/jam.2013.27)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_average_returns : typing.Sequence[float]
            assetsAverageReturns[i] is the average return of asset i over an historical reference period

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j over an historical reference period

        assets_returns : typing.Sequence[float]
            assetsReturns[i] is the return of asset i over a period different from the historical reference period

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsAnalysisTurbulenceIndexResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/analysis/turbulence-index",
            method="POST",
            json={
                "assets": assets,
                "assetsAverageReturns": assets_average_returns,
                "assetsCovarianceMatrix": assets_covariance_matrix,
                "assetsReturns": assets_returns,
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
                    PostAssetsAnalysisTurbulenceIndexResponse,
                    parse_obj_as(
                        type_=PostAssetsAnalysisTurbulenceIndexResponse,
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
