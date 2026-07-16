

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawAssetsCorrelationMatrixClient, RawAssetsCorrelationMatrixClient
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


OMIT = typing.cast(typing.Any, ...)


class AssetsCorrelationMatrixClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawAssetsCorrelationMatrixClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawAssetsCorrelationMatrixClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawAssetsCorrelationMatrixClient
        """
        return self._raw_client

    def correlation_matrix(
        self, *, request: PostAssetsCorrelationMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsCorrelationMatrixResponse:
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
        PostAssetsCorrelationMatrixResponse
            OK

        Examples
        --------
        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix(
            request=PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix(
                assets=2,
                assets_covariance_matrix=[[0.01, -0.0025], [-0.0025, 0.0025]],
            ),
        )
        """
        _response = self._raw_client.correlation_matrix(request=request, request_options=request_options)
        return _response.data

    def correlation_matrix_bounds(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_group: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixBoundsResponse:
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
        PostAssetsCorrelationMatrixBoundsResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix_bounds(
            assets=4,
            assets_correlation_matrix=[
                [1.0, -0.55, -0.15, -0.1],
                [-0.55, 1.0, 0.4, 0.3],
                [-0.15, 0.4, 1.0, 0.5],
                [-0.1, 0.3, 0.5, 1.0],
            ],
            assets_group=[2, 3, 4],
        )
        """
        _response = self._raw_client.correlation_matrix_bounds(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_group=assets_group,
            request_options=request_options,
        )
        return _response.data

    def denoised_correlation_matrix(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_correlation_matrix_aspect_ratio: float,
        denoising_method: typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixDenoisedResponse:
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
        PostAssetsCorrelationMatrixDenoisedResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.denoised_correlation_matrix(
            assets=3,
            assets_correlation_matrix=[
                [1.0, 0.5, 0.9],
                [0.5, 1.0, 0.7],
                [0.9, 0.7, 1.0],
            ],
            assets_correlation_matrix_aspect_ratio=0.5,
        )
        """
        _response = self._raw_client.denoised_correlation_matrix(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_correlation_matrix_aspect_ratio=assets_correlation_matrix_aspect_ratio,
            denoising_method=denoising_method,
            request_options=request_options,
        )
        return _response.data

    def correlation_matrix_distance(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        reference_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixDistanceResponse:
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
        PostAssetsCorrelationMatrixDistanceResponse
            OK

        Examples
        --------
        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixDistanceRequestDistanceMetric,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix_distance(
            assets=3,
            assets_correlation_matrix=[
                [1.0, 0.5, 0.9],
                [0.5, 1.0, 0.7],
                [0.9, 0.7, 1.0],
            ],
            distance_metric=PostAssetsCorrelationMatrixDistanceRequestDistanceMetric.CORRELATION_MATRIX,
            reference_correlation_matrix=[
                [1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0],
                [1.0, 1.0, 1.0],
            ],
        )
        """
        _response = self._raw_client.correlation_matrix_distance(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            reference_correlation_matrix=reference_correlation_matrix,
            distance_metric=distance_metric,
            request_options=request_options,
        )
        return _response.data

    def correlation_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixEffectiveRankResponse:
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
        PostAssetsCorrelationMatrixEffectiveRankResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix_effective_rank(
            assets=2,
            assets_correlation_matrix=[[1.0, 0.0], [0.0, 1.0]],
        )
        """
        _response = self._raw_client.correlation_matrix_effective_rank(
            assets=assets, assets_correlation_matrix=assets_correlation_matrix, request_options=request_options
        )
        return _response.data

    def correlation_matrix_informativeness(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixInformativenessResponse:
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
        PostAssetsCorrelationMatrixInformativenessResponse
            OK

        Examples
        --------
        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix_informativeness(
            assets=3,
            assets_correlation_matrix=[
                [1.0, 0.5, 0.9],
                [0.5, 1.0, 0.7],
                [0.9, 0.7, 1.0],
            ],
            distance_metric=PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric.BURES,
        )
        """
        _response = self._raw_client.correlation_matrix_informativeness(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            distance_metric=distance_metric,
            request_options=request_options,
        )
        return _response.data

    def nearest_correlation_matrix(
        self,
        *,
        assets: int,
        assets_approximate_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_fixed_correlations: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixNearestResponse:
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
        PostAssetsCorrelationMatrixNearestResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.nearest_correlation_matrix(
            assets=3,
            assets_approximate_correlation_matrix=[
                [1.0, 1.0, 0.0],
                [1.0, 1.0, 1.0],
                [0.0, 1.0, 1.0],
            ],
        )
        """
        _response = self._raw_client.nearest_correlation_matrix(
            assets=assets,
            assets_approximate_correlation_matrix=assets_approximate_correlation_matrix,
            assets_fixed_correlations=assets_fixed_correlations,
            request_options=request_options,
        )
        return _response.data

    def random_correlation_matrix(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsCorrelationMatrixRandomResponse:
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
        PostAssetsCorrelationMatrixRandomResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.random_correlation_matrix(
            assets=2,
        )
        """
        _response = self._raw_client.random_correlation_matrix(assets=assets, request_options=request_options)
        return _response.data

    def correlation_matrix_shrinkage(
        self,
        *,
        request: PostAssetsCorrelationMatrixShrinkageRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixShrinkageResponse:
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
        PostAssetsCorrelationMatrixShrinkageResponse
            OK

        Examples
        --------
        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix_shrinkage(
            request=PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix(
                assets=3,
                assets_correlation_matrix=[
                    [1.0, 0.5, 0.9],
                    [0.5, 1.0, 0.7],
                    [0.9, 0.7, 1.0],
                ],
                shrinkage_factor=0.5,
                target_correlation_matrix=[
                    [1.0, 0.0, 0.0],
                    [0.0, 1.0, 0.0],
                    [0.0, 0.0, 1.0],
                ],
            ),
        )
        """
        _response = self._raw_client.correlation_matrix_shrinkage(request=request, request_options=request_options)
        return _response.data

    def theory_implied_correlation_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem],
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        clustering_method: typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixTheoryImpliedResponse:
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
        PostAssetsCorrelationMatrixTheoryImpliedResponse
            OK

        Examples
        --------
        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem,
        )

        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.theory_implied_correlation_matrix(
            assets=[
                PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(
                    asset_hierarchical_classification=[35, 3510, 351010, 35101010],
                ),
                PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(
                    asset_hierarchical_classification=[20, 2030, 203020, 20302010],
                ),
            ],
            assets_correlation_matrix=[[1.0, -0.00035], [-0.00035, 1.0]],
        )
        """
        _response = self._raw_client.theory_implied_correlation_matrix(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            clustering_method=clustering_method,
            request_options=request_options,
        )
        return _response.data

    def correlation_matrix_validation(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixValidationResponse:
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
        PostAssetsCorrelationMatrixValidationResponse
            OK

        Examples
        --------
        from fern import FernApi

        client = FernApi(
            api_key="YOUR_API_KEY",
        )
        client.assets_correlation_matrix.correlation_matrix_validation(
            assets=2,
            assets_correlation_matrix=[[1.0, -0.00035], [-0.00035, 1.0]],
        )
        """
        _response = self._raw_client.correlation_matrix_validation(
            assets=assets, assets_correlation_matrix=assets_correlation_matrix, request_options=request_options
        )
        return _response.data


class AsyncAssetsCorrelationMatrixClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawAssetsCorrelationMatrixClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawAssetsCorrelationMatrixClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawAssetsCorrelationMatrixClient
        """
        return self._raw_client

    async def correlation_matrix(
        self, *, request: PostAssetsCorrelationMatrixRequest, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsCorrelationMatrixResponse:
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
        PostAssetsCorrelationMatrixResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix(
                request=PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix(
                    assets=2,
                    assets_covariance_matrix=[[0.01, -0.0025], [-0.0025, 0.0025]],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix(request=request, request_options=request_options)
        return _response.data

    async def correlation_matrix_bounds(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_group: typing.Sequence[int],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixBoundsResponse:
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
        PostAssetsCorrelationMatrixBoundsResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix_bounds(
                assets=4,
                assets_correlation_matrix=[
                    [1.0, -0.55, -0.15, -0.1],
                    [-0.55, 1.0, 0.4, 0.3],
                    [-0.15, 0.4, 1.0, 0.5],
                    [-0.1, 0.3, 0.5, 1.0],
                ],
                assets_group=[2, 3, 4],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix_bounds(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_group=assets_group,
            request_options=request_options,
        )
        return _response.data

    async def denoised_correlation_matrix(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_correlation_matrix_aspect_ratio: float,
        denoising_method: typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixDenoisedResponse:
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
        PostAssetsCorrelationMatrixDenoisedResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.denoised_correlation_matrix(
                assets=3,
                assets_correlation_matrix=[
                    [1.0, 0.5, 0.9],
                    [0.5, 1.0, 0.7],
                    [0.9, 0.7, 1.0],
                ],
                assets_correlation_matrix_aspect_ratio=0.5,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.denoised_correlation_matrix(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            assets_correlation_matrix_aspect_ratio=assets_correlation_matrix_aspect_ratio,
            denoising_method=denoising_method,
            request_options=request_options,
        )
        return _response.data

    async def correlation_matrix_distance(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        reference_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixDistanceResponse:
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
        PostAssetsCorrelationMatrixDistanceResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixDistanceRequestDistanceMetric,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix_distance(
                assets=3,
                assets_correlation_matrix=[
                    [1.0, 0.5, 0.9],
                    [0.5, 1.0, 0.7],
                    [0.9, 0.7, 1.0],
                ],
                distance_metric=PostAssetsCorrelationMatrixDistanceRequestDistanceMetric.CORRELATION_MATRIX,
                reference_correlation_matrix=[
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                    [1.0, 1.0, 1.0],
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix_distance(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            reference_correlation_matrix=reference_correlation_matrix,
            distance_metric=distance_metric,
            request_options=request_options,
        )
        return _response.data

    async def correlation_matrix_effective_rank(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixEffectiveRankResponse:
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
        PostAssetsCorrelationMatrixEffectiveRankResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix_effective_rank(
                assets=2,
                assets_correlation_matrix=[[1.0, 0.0], [0.0, 1.0]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix_effective_rank(
            assets=assets, assets_correlation_matrix=assets_correlation_matrix, request_options=request_options
        )
        return _response.data

    async def correlation_matrix_informativeness(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        distance_metric: typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixInformativenessResponse:
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
        PostAssetsCorrelationMatrixInformativenessResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix_informativeness(
                assets=3,
                assets_correlation_matrix=[
                    [1.0, 0.5, 0.9],
                    [0.5, 1.0, 0.7],
                    [0.9, 0.7, 1.0],
                ],
                distance_metric=PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric.BURES,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix_informativeness(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            distance_metric=distance_metric,
            request_options=request_options,
        )
        return _response.data

    async def nearest_correlation_matrix(
        self,
        *,
        assets: int,
        assets_approximate_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        assets_fixed_correlations: typing.Optional[typing.Sequence[typing.Sequence[int]]] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixNearestResponse:
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
        PostAssetsCorrelationMatrixNearestResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.nearest_correlation_matrix(
                assets=3,
                assets_approximate_correlation_matrix=[
                    [1.0, 1.0, 0.0],
                    [1.0, 1.0, 1.0],
                    [0.0, 1.0, 1.0],
                ],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.nearest_correlation_matrix(
            assets=assets,
            assets_approximate_correlation_matrix=assets_approximate_correlation_matrix,
            assets_fixed_correlations=assets_fixed_correlations,
            request_options=request_options,
        )
        return _response.data

    async def random_correlation_matrix(
        self, *, assets: int, request_options: typing.Optional[RequestOptions] = None
    ) -> PostAssetsCorrelationMatrixRandomResponse:
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
        PostAssetsCorrelationMatrixRandomResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.random_correlation_matrix(
                assets=2,
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.random_correlation_matrix(assets=assets, request_options=request_options)
        return _response.data

    async def correlation_matrix_shrinkage(
        self,
        *,
        request: PostAssetsCorrelationMatrixShrinkageRequest,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixShrinkageResponse:
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
        PostAssetsCorrelationMatrixShrinkageResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix_shrinkage(
                request=PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix(
                    assets=3,
                    assets_correlation_matrix=[
                        [1.0, 0.5, 0.9],
                        [0.5, 1.0, 0.7],
                        [0.9, 0.7, 1.0],
                    ],
                    shrinkage_factor=0.5,
                    target_correlation_matrix=[
                        [1.0, 0.0, 0.0],
                        [0.0, 1.0, 0.0],
                        [0.0, 0.0, 1.0],
                    ],
                ),
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix_shrinkage(
            request=request, request_options=request_options
        )
        return _response.data

    async def theory_implied_correlation_matrix(
        self,
        *,
        assets: typing.Sequence[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem],
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        clustering_method: typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixTheoryImpliedResponse:
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
        PostAssetsCorrelationMatrixTheoryImpliedResponse
            OK

        Examples
        --------
        import asyncio

        from fern.assets_correlation_matrix import (
            PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem,
        )

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.theory_implied_correlation_matrix(
                assets=[
                    PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(
                        asset_hierarchical_classification=[35, 3510, 351010, 35101010],
                    ),
                    PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(
                        asset_hierarchical_classification=[20, 2030, 203020, 20302010],
                    ),
                ],
                assets_correlation_matrix=[[1.0, -0.00035], [-0.00035, 1.0]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.theory_implied_correlation_matrix(
            assets=assets,
            assets_correlation_matrix=assets_correlation_matrix,
            clustering_method=clustering_method,
            request_options=request_options,
        )
        return _response.data

    async def correlation_matrix_validation(
        self,
        *,
        assets: int,
        assets_correlation_matrix: typing.Sequence[typing.Sequence[float]],
        request_options: typing.Optional[RequestOptions] = None,
    ) -> PostAssetsCorrelationMatrixValidationResponse:
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
        PostAssetsCorrelationMatrixValidationResponse
            OK

        Examples
        --------
        import asyncio

        from fern import AsyncFernApi

        client = AsyncFernApi(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.assets_correlation_matrix.correlation_matrix_validation(
                assets=2,
                assets_correlation_matrix=[[1.0, -0.00035], [-0.00035, 1.0]],
            )


        asyncio.run(main())
        """
        _response = await self._raw_client.correlation_matrix_validation(
            assets=assets, assets_correlation_matrix=assets_correlation_matrix, request_options=request_options
        )
        return _response.data
