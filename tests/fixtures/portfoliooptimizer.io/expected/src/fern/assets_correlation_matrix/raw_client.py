

import typing
from json.decoder import JSONDecodeError

from ..core.api_error import ApiError
from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.http_response import AsyncHttpResponse, HttpResponse
from ..core.parse_error import ParsingError
from ..core.pydantic_utilities import parse_obj_as
from ..core.request_options import RequestOptions
from ..core.serialization import convert_and_respect_annotation_metadata
from .types.post_assets_correlation_matrix_bounds_response import PostAssetsCorrelationMatrixBoundsResponse
from .types.post_assets_correlation_matrix_denoised_request_denoising_method import (
    PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod,
)
from .types.post_assets_correlation_matrix_denoised_response import PostAssetsCorrelationMatrixDenoisedResponse
from .types.post_assets_correlation_matrix_distance_request_distance_metric import (
    PostAssetsCorrelationMatrixDistanceRequestDistanceMetric,
)
from .types.post_assets_correlation_matrix_distance_response import PostAssetsCorrelationMatrixDistanceResponse
from .types.post_assets_correlation_matrix_effective_rank_response import (
    PostAssetsCorrelationMatrixEffectiveRankResponse,
)
from .types.post_assets_correlation_matrix_informativeness_request_distance_metric import (
    PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric,
)
from .types.post_assets_correlation_matrix_informativeness_response import (
    PostAssetsCorrelationMatrixInformativenessResponse,
)
from .types.post_assets_correlation_matrix_nearest_response import PostAssetsCorrelationMatrixNearestResponse
from .types.post_assets_correlation_matrix_random_response import PostAssetsCorrelationMatrixRandomResponse
from .types.post_assets_correlation_matrix_request import PostAssetsCorrelationMatrixRequest
from .types.post_assets_correlation_matrix_response import PostAssetsCorrelationMatrixResponse
from .types.post_assets_correlation_matrix_shrinkage_request import PostAssetsCorrelationMatrixShrinkageRequest
from .types.post_assets_correlation_matrix_shrinkage_response import PostAssetsCorrelationMatrixShrinkageResponse
from .types.post_assets_correlation_matrix_theory_implied_request_assets_item import (
    PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem,
)
from .types.post_assets_correlation_matrix_theory_implied_request_clustering_method import (
    PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod,
)
from .types.post_assets_correlation_matrix_theory_implied_response import (
    PostAssetsCorrelationMatrixTheoryImpliedResponse,
)
from .types.post_assets_correlation_matrix_validation_response import PostAssetsCorrelationMatrixValidationResponse
from pydantic import ValidationError


OMIT = typing.cast(typing.Any, ...)


class RawAssetsCorrelationMatrixClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def correlation_matrix(
        self, *, request: PostAssetsCorrelationMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostAssetsCorrelationMatrixResponse]:
        """
        Compute the Pearson asset correlation matrix from either:
        * The asset returns
        * The asset covariance matrix

        References
        * [Wikipedia, Correlation and Dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices)

        Parameters
        ----------
        request : PostAssetsCorrelationMatrixRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsCorrelationMatrixRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsCorrelationMatrixResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixResponse,
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

    def correlation_matrix_bounds(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_group: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixBoundsResponse]:
        """
        Compute the lower bounds and the upper bounds of an asset correlation matrix associated to a given group of assets.

         References
         * [Kawee Numpacharoen & Kornkanok Bunwong (2013) Boundaries of Correlation Adjustment with Applications to Financial Risk Management, Applied Mathematical Finance, 20:4, 403-414](http://dx.doi.org/10.1080/1350486X.2012.723517).

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        assets_group : typing.Sequence[int]
            assetsGroup[k] is the indexes of the assets belonging to the assets group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixBoundsResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/bounds",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsGroup": assets_group,
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
                    PostAssetsCorrelationMatrixBoundsResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixBoundsResponse,
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

    def denoised_correlation_matrix(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_correlation_matrix_aspect_ratio: float,
        denoising_method: typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixDenoisedResponse]:
        """
        Compute a denoised asset correlation matrix, using one of the following methods:
         * The eigenvalues clipping method, described in the first reference, which is based on random matrix theory

         References
         * [Laurent Laloux, Pierre Cizeau, Jean-Philippe Bouchaud, and Marc Potters, Noise Dressing of Financial Correlation Matrices, Phys. Rev. Lett. 83, 1467](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.83.1467)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        assets_correlation_matrix_aspect_ratio : float
            The aspect ratio of the asset correlation matrix, defined as the number of assets divided by the number of asset returns per asset used to compute the asset correlation matrix

        denoising_method : typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod]
            The method used to denoise the asset correlation matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixDenoisedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/denoised",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsCorrelationMatrixAspectRatio": assets_correlation_matrix_aspect_ratio,
                "denoisingMethod": denoising_method,
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
                    PostAssetsCorrelationMatrixDenoisedResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixDenoisedResponse,
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

    def correlation_matrix_distance(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        reference_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixDistanceResponse]:
        """
        Compute the distance between an asset correlation matrix and a reference correlation matrix, using one of the following distance metrics:
        * Euclidean distance (default), which is the distance induced by [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)
        * Correlation matrix distance, defined in the first reference, which corresponds to [the cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) between the two vectorized asset correlation matrices
        * Bures distance, defined in the second reference

         References
         * [M. Herdin, N. Czink, H. Ozcelik and E. Bonek, Correlation matrix distance, a meaningful measure for evaluation of non-stationary MIMO channels, 2005 IEEE 61st Vehicular Technology Conference, 2005, pp. 136-140 Vol. 1](https://ieeexplore.ieee.org/document/1543265)
         * [Rajendra Bhatia, Tanvi Jain, Yongdo Lim, On the Bures–Wasserstein distance between positive definite matrices, Expositiones Mathematicae, Volume 37, Issue 2, 2019](https://www.sciencedirect.com/science/article/pii/S0723086918300021)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        reference_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            referenceCorrelationMatrix[i][j] is the reference correlation between the asset i and the asset j

        distance_metric : typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric]
            The distance metric to use to compute the distance between the asset correlation matrix and the reference correlation matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixDistanceResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/distance",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "distanceMetric": distance_metric,
                "referenceCorrelationMatrix": reference_correlation_matrix,
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
                    PostAssetsCorrelationMatrixDistanceResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixDistanceResponse,
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

    def correlation_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixEffectiveRankResponse]:
        """
        Compute the effective rank of an asset correlation matrix.

        References
        * [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixEffectiveRankResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/effective-rank",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
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
                    PostAssetsCorrelationMatrixEffectiveRankResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixEffectiveRankResponse,
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

    def correlation_matrix_informativeness(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixInformativenessResponse]:
        """
        Compute the informativeness of an asset correlation matrix, using one of the following distance metrics:
        * Euclidean distance (default), which is the distance induced by [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)
        * Correlation matrix distance, defined in the second reference, which corresponds to [the cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) between the two vectorized asset correlation matrices
        * Bures distance, defined in the third reference

         References
         * [Austin J. Brockmeier and Tingting Mu and Sophia Ananiadou and John Y. Goulermas, Quantifying the Informativeness of Similarity Measurements, Journal of Machine Learning Research, 2017](http://jmlr.org/papers/v18/16-296.html)
         * [M. Herdin, N. Czink, H. Ozcelik and E. Bonek, Correlation matrix distance, a meaningful measure for evaluation of non-stationary MIMO channels, 2005 IEEE 61st Vehicular Technology Conference, 2005, pp. 136-140 Vol. 1](https://ieeexplore.ieee.org/document/1543265)
         * [Rajendra Bhatia, Tanvi Jain, Yongdo Lim, On the Bures–Wasserstein distance between positive definite matrices, Expositiones Mathematicae, Volume 37, Issue 2, 2019](https://www.sciencedirect.com/science/article/pii/S0723086918300021)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        distance_metric : typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric]
            The distance metric to use to compute the informativeness of the asset correlation matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixInformativenessResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/informativeness",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "distanceMetric": distance_metric,
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
                    PostAssetsCorrelationMatrixInformativenessResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixInformativenessResponse,
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

    def nearest_correlation_matrix(
        self,
        *,
        assets: int,
        assets_approximate_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_fixed_correlations: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixNearestResponse]:
        """
        Compute the _closest_ - in terms of [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm) - asset correlation matrix to an approximate asset correlation matrix, optionally keeping a selected number of correlations fixed.

        References
        * [Nicholas J. Higham, Computing the Nearest Correlation Matrix—A Problem from Finance, IMA J. Numer. Anal. 22, 329–343, 2002.](http://www.maths.manchester.ac.uk/~higham/narep/narep369.pdf)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_approximate_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsApproximateCorrelationMatrix[i][i] is the approximate correlation between the asset i and the asset j

        assets_fixed_correlations : typing.Optional[typing.Sequence[typing.Sequence[int]]]
            assetsFixedCorrelations[k] is the couple of indices (i,j) of the assets i and j for which to keep the approximate correlation assetsApproximateCorrelationMatrix[i][j] fixed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixNearestResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/nearest",
            method="POST",
            json={
                "assets": assets,
                "assetsApproximateCorrelationMatrix": assets_approximate_correlation_matrix,
                "assetsFixedCorrelations": assets_fixed_correlations,
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
                    PostAssetsCorrelationMatrixNearestResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixNearestResponse,
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

    def random_correlation_matrix(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> HttpResponse[PostAssetsCorrelationMatrixRandomResponse]:
        """
        Generate an asset correlation matrix uniformly at random over the space of positive definite correlation matrices.

        References
        * [Joe, H., Generating random correlation matrices based on partial correlations. Journal of Multivariate Analysis, 2006, 97, 2177-2189](https://www.sciencedirect.com/science/article/pii/S0047259X05000886)

        Parameters
        ----------
        assets : int
            The number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixRandomResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/random",
            method="POST",
            json={
                "assets": assets,
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
                    PostAssetsCorrelationMatrixRandomResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixRandomResponse,
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

    def correlation_matrix_shrinkage(
        self,
        *,
        request: PostAssetsCorrelationMatrixShrinkageRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixShrinkageResponse]:
        """
        Compute an asset correlation matrix as a convex linear combination of an asset correlation matrix and a target correlation matrix, the target correlation matrix being either:
         * An equicorrelation matrix made of 1
         * An equicorrelation matrix made of 0
         * An equicorrelation matrix made of -1/(n-1), with n the number of assets
         * A provided correlation matrix

         References
         * [Steiner, Andreas, Manipulating Valid Correlation Matrices](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1878165)

        Parameters
        ----------
        request : PostAssetsCorrelationMatrixShrinkageRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixShrinkageResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/shrinkage",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsCorrelationMatrixShrinkageRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsCorrelationMatrixShrinkageResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixShrinkageResponse,
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

    def theory_implied_correlation_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem],
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        clustering_method: typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixTheoryImpliedResponse]:
        """
        Compute the theory-implied asset correlation matrix associated with:
        * A hierarchical classification of a universe of assets
        * An asset correlation matrix

        References
        * [Lopez de Prado, Marcos Estimation of Theory-Implied Correlation Matrices (November 9, 2019)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3484152)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem]

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        clustering_method : typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod]
            The hierarchical clustering method to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixTheoryImpliedResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/theory-implied",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem],
                    direction="write",
                ),
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "clusteringMethod": clustering_method,
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
                    PostAssetsCorrelationMatrixTheoryImpliedResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixTheoryImpliedResponse,
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

    def correlation_matrix_validation(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> HttpResponse[PostAssetsCorrelationMatrixValidationResponse]:
        """
        Validate whether a matrix is an asset correlation matrix.

        References
        * [Wikipedia, Correlation and Dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        HttpResponse[PostAssetsCorrelationMatrixValidationResponse]
            OK
        """
        _response = self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/validation",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
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
                    PostAssetsCorrelationMatrixValidationResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixValidationResponse,
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


class AsyncRawAssetsCorrelationMatrixClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def correlation_matrix(
        self, *, request: PostAssetsCorrelationMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixResponse]:
        """
        Compute the Pearson asset correlation matrix from either:
        * The asset returns
        * The asset covariance matrix

        References
        * [Wikipedia, Correlation and Dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices)

        Parameters
        ----------
        request : PostAssetsCorrelationMatrixRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsCorrelationMatrixRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsCorrelationMatrixResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixResponse,
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

    async def correlation_matrix_bounds(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_group: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixBoundsResponse]:
        """
        Compute the lower bounds and the upper bounds of an asset correlation matrix associated to a given group of assets.

         References
         * [Kawee Numpacharoen & Kornkanok Bunwong (2013) Boundaries of Correlation Adjustment with Applications to Financial Risk Management, Applied Mathematical Finance, 20:4, 403-414](http://dx.doi.org/10.1080/1350486X.2012.723517).

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        assets_group : typing.Sequence[int]
            assetsGroup[k] is the indexes of the assets belonging to the assets group

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixBoundsResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/bounds",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsGroup": assets_group,
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
                    PostAssetsCorrelationMatrixBoundsResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixBoundsResponse,
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

    async def denoised_correlation_matrix(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_correlation_matrix_aspect_ratio: float,
        denoising_method: typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixDenoisedResponse]:
        """
        Compute a denoised asset correlation matrix, using one of the following methods:
         * The eigenvalues clipping method, described in the first reference, which is based on random matrix theory

         References
         * [Laurent Laloux, Pierre Cizeau, Jean-Philippe Bouchaud, and Marc Potters, Noise Dressing of Financial Correlation Matrices, Phys. Rev. Lett. 83, 1467](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.83.1467)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        assets_correlation_matrix_aspect_ratio : float
            The aspect ratio of the asset correlation matrix, defined as the number of assets divided by the number of asset returns per asset used to compute the asset correlation matrix

        denoising_method : typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod]
            The method used to denoise the asset correlation matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixDenoisedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/denoised",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "assetsCorrelationMatrixAspectRatio": assets_correlation_matrix_aspect_ratio,
                "denoisingMethod": denoising_method,
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
                    PostAssetsCorrelationMatrixDenoisedResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixDenoisedResponse,
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

    async def correlation_matrix_distance(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        reference_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixDistanceResponse]:
        """
        Compute the distance between an asset correlation matrix and a reference correlation matrix, using one of the following distance metrics:
        * Euclidean distance (default), which is the distance induced by [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)
        * Correlation matrix distance, defined in the first reference, which corresponds to [the cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) between the two vectorized asset correlation matrices
        * Bures distance, defined in the second reference

         References
         * [M. Herdin, N. Czink, H. Ozcelik and E. Bonek, Correlation matrix distance, a meaningful measure for evaluation of non-stationary MIMO channels, 2005 IEEE 61st Vehicular Technology Conference, 2005, pp. 136-140 Vol. 1](https://ieeexplore.ieee.org/document/1543265)
         * [Rajendra Bhatia, Tanvi Jain, Yongdo Lim, On the Bures–Wasserstein distance between positive definite matrices, Expositiones Mathematicae, Volume 37, Issue 2, 2019](https://www.sciencedirect.com/science/article/pii/S0723086918300021)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        reference_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            referenceCorrelationMatrix[i][j] is the reference correlation between the asset i and the asset j

        distance_metric : typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric]
            The distance metric to use to compute the distance between the asset correlation matrix and the reference correlation matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixDistanceResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/distance",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "distanceMetric": distance_metric,
                "referenceCorrelationMatrix": reference_correlation_matrix,
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
                    PostAssetsCorrelationMatrixDistanceResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixDistanceResponse,
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

    async def correlation_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixEffectiveRankResponse]:
        """
        Compute the effective rank of an asset correlation matrix.

        References
        * [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixEffectiveRankResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/effective-rank",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
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
                    PostAssetsCorrelationMatrixEffectiveRankResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixEffectiveRankResponse,
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

    async def correlation_matrix_informativeness(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixInformativenessResponse]:
        """
        Compute the informativeness of an asset correlation matrix, using one of the following distance metrics:
        * Euclidean distance (default), which is the distance induced by [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)
        * Correlation matrix distance, defined in the second reference, which corresponds to [the cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) between the two vectorized asset correlation matrices
        * Bures distance, defined in the third reference

         References
         * [Austin J. Brockmeier and Tingting Mu and Sophia Ananiadou and John Y. Goulermas, Quantifying the Informativeness of Similarity Measurements, Journal of Machine Learning Research, 2017](http://jmlr.org/papers/v18/16-296.html)
         * [M. Herdin, N. Czink, H. Ozcelik and E. Bonek, Correlation matrix distance, a meaningful measure for evaluation of non-stationary MIMO channels, 2005 IEEE 61st Vehicular Technology Conference, 2005, pp. 136-140 Vol. 1](https://ieeexplore.ieee.org/document/1543265)
         * [Rajendra Bhatia, Tanvi Jain, Yongdo Lim, On the Bures–Wasserstein distance between positive definite matrices, Expositiones Mathematicae, Volume 37, Issue 2, 2019](https://www.sciencedirect.com/science/article/pii/S0723086918300021)

        Parameters
        ----------
        assets : int

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        distance_metric : typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric]
            The distance metric to use to compute the informativeness of the asset correlation matrix

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixInformativenessResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/informativeness",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "distanceMetric": distance_metric,
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
                    PostAssetsCorrelationMatrixInformativenessResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixInformativenessResponse,
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

    async def nearest_correlation_matrix(
        self,
        *,
        assets: int,
        assets_approximate_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_fixed_correlations: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixNearestResponse]:
        """
        Compute the _closest_ - in terms of [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm) - asset correlation matrix to an approximate asset correlation matrix, optionally keeping a selected number of correlations fixed.

        References
        * [Nicholas J. Higham, Computing the Nearest Correlation Matrix—A Problem from Finance, IMA J. Numer. Anal. 22, 329–343, 2002.](http://www.maths.manchester.ac.uk/~higham/narep/narep369.pdf)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_approximate_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsApproximateCorrelationMatrix[i][i] is the approximate correlation between the asset i and the asset j

        assets_fixed_correlations : typing.Optional[typing.Sequence[typing.Sequence[int]]]
            assetsFixedCorrelations[k] is the couple of indices (i,j) of the assets i and j for which to keep the approximate correlation assetsApproximateCorrelationMatrix[i][j] fixed

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixNearestResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/nearest",
            method="POST",
            json={
                "assets": assets,
                "assetsApproximateCorrelationMatrix": assets_approximate_correlation_matrix,
                "assetsFixedCorrelations": assets_fixed_correlations,
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
                    PostAssetsCorrelationMatrixNearestResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixNearestResponse,
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

    async def random_correlation_matrix(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixRandomResponse]:
        """
        Generate an asset correlation matrix uniformly at random over the space of positive definite correlation matrices.

        References
        * [Joe, H., Generating random correlation matrices based on partial correlations. Journal of Multivariate Analysis, 2006, 97, 2177-2189](https://www.sciencedirect.com/science/article/pii/S0047259X05000886)

        Parameters
        ----------
        assets : int
            The number of assets

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixRandomResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/random",
            method="POST",
            json={
                "assets": assets,
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
                    PostAssetsCorrelationMatrixRandomResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixRandomResponse,
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

    async def correlation_matrix_shrinkage(
        self,
        *,
        request: PostAssetsCorrelationMatrixShrinkageRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixShrinkageResponse]:
        """
        Compute an asset correlation matrix as a convex linear combination of an asset correlation matrix and a target correlation matrix, the target correlation matrix being either:
         * An equicorrelation matrix made of 1
         * An equicorrelation matrix made of 0
         * An equicorrelation matrix made of -1/(n-1), with n the number of assets
         * A provided correlation matrix

         References
         * [Steiner, Andreas, Manipulating Valid Correlation Matrices](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1878165)

        Parameters
        ----------
        request : PostAssetsCorrelationMatrixShrinkageRequest

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixShrinkageResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/shrinkage",
            method="POST",
            json=convert_and_respect_annotation_metadata(
                object_=request, annotation=PostAssetsCorrelationMatrixShrinkageRequest, direction="write"
            ),
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                _data = typing.cast(
                    PostAssetsCorrelationMatrixShrinkageResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixShrinkageResponse,
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

    async def theory_implied_correlation_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem],
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        clustering_method: typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixTheoryImpliedResponse]:
        """
        Compute the theory-implied asset correlation matrix associated with:
        * A hierarchical classification of a universe of assets
        * An asset correlation matrix

        References
        * [Lopez de Prado, Marcos Estimation of Theory-Implied Correlation Matrices (November 9, 2019)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3484152)

        Parameters
        ----------
        assets : typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem]

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        clustering_method : typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod]
            The hierarchical clustering method to use

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixTheoryImpliedResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/theory-implied",
            method="POST",
            json={
                "assets": convert_and_respect_annotation_metadata(
                    object_=assets,
                    annotation=typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem],
                    direction="write",
                ),
                "assetsCorrelationMatrix": assets_correlation_matrix,
                "clusteringMethod": clustering_method,
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
                    PostAssetsCorrelationMatrixTheoryImpliedResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixTheoryImpliedResponse,
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

    async def correlation_matrix_validation(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> AsyncHttpResponse[PostAssetsCorrelationMatrixValidationResponse]:
        """
        Validate whether a matrix is an asset correlation matrix.

        References
        * [Wikipedia, Correlation and Dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices)

        Parameters
        ----------
        assets : int
            The number of assets

        assets_correlation_matrix : typing.Sequence[typing.Sequence[float]]
            assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        AsyncHttpResponse[PostAssetsCorrelationMatrixValidationResponse]
            OK
        """
        _response = await self._client_wrapper.httpx_client.request(
            "assets/correlation/matrix/validation",
            method="POST",
            json={
                "assets": assets,
                "assetsCorrelationMatrix": assets_correlation_matrix,
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
                    PostAssetsCorrelationMatrixValidationResponse,
                    parse_obj_as(
                        type_=PostAssetsCorrelationMatrixValidationResponse,
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
