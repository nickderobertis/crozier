

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_covariance_matrix_effective_rank_response import PostAssetsCovarianceMatrixEffectiveRankResponse
from .types.post_assets_covariance_matrix_exponentially_weighted_request_assets_item import (
    PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem,
)
from .types.post_assets_covariance_matrix_exponentially_weighted_response import (
    PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
)
from .types.post_assets_covariance_matrix_request import PostAssetsCovarianceMatrixRequest
from .types.post_assets_covariance_matrix_response import PostAssetsCovarianceMatrixResponse
from .types.post_assets_covariance_matrix_validation_response import PostAssetsCovarianceMatrixValidationResponse


OMIT = typing.cast(typing.Any, ...)


class RawAssetsCovarianceMatrixClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def covariance_matrix(
        self, *, request: PostAssetsCovarianceMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostAssetsCovarianceMatrixResponse]:
        """
        Compute the covariance matrix of assets from either:
        * The asset correlation matrix and their volatilities (i.e., standard deviations)
        * The asset correlation matrix and their variances
        * The asset returns

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        request : PostAssetsCovarianceMatrixRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCovarianceMatrixResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsCovarianceMatrixRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsCovarianceMatrixResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def covariance_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCovarianceMatrixEffectiveRankResponse]:
        """
        Compute the effective rank of an asset covariance matrix.

        References
        * [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCovarianceMatrixEffectiveRankResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix/effective-rank",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
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
                    PostAssetsCovarianceMatrixEffectiveRankResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixEffectiveRankResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def exponentially_weighted_covariance_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem],
        decay_factor: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCovarianceMatrixExponentiallyWeightedResponse]:
        """
        Compute an exponentially weighted covariance matrix of assets returns.

        References
        * [RiskMetrics Group. Longerstaey, J. (1996). RiskMetrics technical document, Technical Report fourth edition](https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem]

        decay_factor : typing.Optional[float]
            The exponential decay factor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCovarianceMatrixExponentiallyWeightedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix/exponentially-weighted",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem],
                    direction="write",
                ),
                "decayFactor": decay_factor,
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
                    PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    def covariance_matrix_validation(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCovarianceMatrixValidationResponse]:
        """
        Validate whether a matrix is a covariance matrix.

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCovarianceMatrixValidationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix/validation",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
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
                    PostAssetsCovarianceMatrixValidationResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixValidationResponse,
                        object_=_response.json(),
                    ),
                )
                return HttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)


class AsyncRawAssetsCovarianceMatrixClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def covariance_matrix(
        self, *, request: PostAssetsCovarianceMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostAssetsCovarianceMatrixResponse]:
        """
        Compute the covariance matrix of assets from either:
        * The asset correlation matrix and their volatilities (i.e., standard deviations)
        * The asset correlation matrix and their variances
        * The asset returns

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        request : PostAssetsCovarianceMatrixRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCovarianceMatrixResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsCovarianceMatrixRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsCovarianceMatrixResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def covariance_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCovarianceMatrixEffectiveRankResponse]:
        """
        Compute the effective rank of an asset covariance matrix.

        References
        * [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCovarianceMatrixEffectiveRankResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix/effective-rank",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
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
                    PostAssetsCovarianceMatrixEffectiveRankResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixEffectiveRankResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def exponentially_weighted_covariance_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem],
        decay_factor: typing.Optional[float] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCovarianceMatrixExponentiallyWeightedResponse]:
        """
        Compute an exponentially weighted covariance matrix of assets returns.

        References
        * [RiskMetrics Group. Longerstaey, J. (1996). RiskMetrics technical document, Technical Report fourth edition](https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem]

        decay_factor : typing.Optional[float]
            The exponential decay factor

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCovarianceMatrixExponentiallyWeightedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix/exponentially-weighted",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem],
                    direction="write",
                ),
                "decayFactor": decay_factor,
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
                    PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)

    async def covariance_matrix_validation(
        self,
        *,
        assets: int,
        assets_covariance_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCovarianceMatrixValidationResponse]:
        """
        Validate whether a matrix is a covariance matrix.

        References
        * [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_covariance_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCovarianceMatrixValidationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/covariance/matrix/validation",
            method="POST",
            json={
                "assets": assets,
                "assetsCovarianceMatrix": assets_covariance_matrix,
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
                    PostAssetsCovarianceMatrixValidationResponse,
                    parse_obj_as(
                        type_=PostAssetsCovarianceMatrixValidationResponse,
                        object_=_response.json(),
                    ),
                )
                return AsyncHttpResponse(response=_response, data=_data)
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response.text)
        raise ApiError(status_code=_response.status_code, headers=dict(_response.headers), body=_response_json)
