# Reference
## AssetsAnalysis
<details><summary><code>client.assets_analysis.<a href="src/fern/assets_analysis/client.py">absorption_ratio</a>(...) -> PostAssetsAnalysisAbsorptionRatioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the absorption ratio associated to a universe of assets.

References
* [Mark Kritzman, Yuanzhen Li, Sebastien Page and Roberto Rigobon, Principal Components as a Measure of Systemic Risk, The Journal of Portfolio Management Summer 2011, 37 (4) 112-126](https://jpm.pm-research.com/content/37/4/112)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_analysis.absorption_ratio(
    assets=2,
    assets_covariance_matrix=[
        [
            9,
            1
        ],
        [
            1,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix_eigenvectors:** `typing.Optional[PostAssetsAnalysisAbsorptionRatioRequestAssetsCovarianceMatrixEigenvectors]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_analysis.<a href="src/fern/assets_analysis/client.py">turbulence_index</a>(...) -> PostAssetsAnalysisTurbulenceIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the turbulence index associated to a universe of assets.

References
* [M. Kritzman, Y. Li, Skulls, Financial Turbulence, and Risk Management,Financial Analysts Journal, Volume 66, Number 5, Pages 30-41, Year 2010](https://www.tandfonline.com/doi/abs/10.2469/faj.v66.n5.3)
* [Kinlaw, W., Turkington, D. Correlation surprise. J Asset Manag 14, 385–399 (2013)](https://link.springer.com/article/10.1057/jam.2013.27)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_analysis.turbulence_index(
    assets=2,
    assets_average_returns=[
        1,
        1
    ],
    assets_covariance_matrix=[
        [
            9,
            1
        ],
        [
            1,
            1
        ]
    ],
    assets_returns=[
        1,
        0
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_average_returns:** `typing.List[float]` — assetsAverageReturns[i] is the average return of asset i over an historical reference period
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j over an historical reference period
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the return of asset i over a period different from the historical reference period
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsCorrelationMatrix
<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix</a>(...) -> PostAssetsCorrelationMatrixResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the Pearson asset correlation matrix from either:  
* The asset returns
* The asset covariance matrix

References
* [Wikipedia, Correlation and Dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_correlation_matrix import PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix(
    request=PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix(
        assets=2,
        assets_covariance_matrix=[
            [
                0.01,
                -0.0025
            ],
            [
                -0.0025,
                0.0025
            ]
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostAssetsCorrelationMatrixRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix_bounds</a>(...) -> PostAssetsCorrelationMatrixBoundsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the lower bounds and the upper bounds of an asset correlation matrix associated to a given group of assets.
 
 References
 * [Kawee Numpacharoen & Kornkanok Bunwong (2013) Boundaries of Correlation Adjustment with Applications to Financial Risk Management, Applied Mathematical Finance, 20:4, 403-414](http://dx.doi.org/10.1080/1350486X.2012.723517).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix_bounds(
    assets=4,
    assets_correlation_matrix=[
        [
            1,
            -0.55,
            -0.15,
            -0.1
        ],
        [
            -0.55,
            1,
            0.4,
            0.3
        ],
        [
            -0.15,
            0.4,
            1,
            0.5
        ],
        [
            -0.1,
            0.3,
            0.5,
            1
        ]
    ],
    assets_group=[
        2,
        3,
        4
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_group:** `typing.List[int]` — assetsGroup[k] is the indexes of the assets belonging to the assets group
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">denoised_correlation_matrix</a>(...) -> PostAssetsCorrelationMatrixDenoisedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute a denoised asset correlation matrix, using one of the following methods:
 * The eigenvalues clipping method, described in the first reference, which is based on random matrix theory
 
 References
 * [Laurent Laloux, Pierre Cizeau, Jean-Philippe Bouchaud, and Marc Potters, Noise Dressing of Financial Correlation Matrices, Phys. Rev. Lett. 83, 1467](https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.83.1467)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.denoised_correlation_matrix(
    assets=3,
    assets_correlation_matrix=[
        [
            1,
            0.5,
            0.9
        ],
        [
            0.5,
            1,
            0.7
        ],
        [
            0.9,
            0.7,
            1
        ]
    ],
    assets_correlation_matrix_aspect_ratio=0.5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix_aspect_ratio:** `float` — The aspect ratio of the asset correlation matrix, defined as the number of assets divided by the number of asset returns per asset used to compute the asset correlation matrix
    
</dd>
</dl>

<dl>
<dd>

**denoising_method:** `typing.Optional[PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod]` — The method used to denoise the asset correlation matrix
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix_distance</a>(...) -> PostAssetsCorrelationMatrixDistanceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the distance between an asset correlation matrix and a reference correlation matrix, using one of the following distance metrics:
* Euclidean distance (default), which is the distance induced by [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)
* Correlation matrix distance, defined in the first reference, which corresponds to [the cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) between the two vectorized asset correlation matrices
* Bures distance, defined in the second reference

 References
 * [M. Herdin, N. Czink, H. Ozcelik and E. Bonek, Correlation matrix distance, a meaningful measure for evaluation of non-stationary MIMO channels, 2005 IEEE 61st Vehicular Technology Conference, 2005, pp. 136-140 Vol. 1](https://ieeexplore.ieee.org/document/1543265)
 * [Rajendra Bhatia, Tanvi Jain, Yongdo Lim, On the Bures–Wasserstein distance between positive definite matrices, Expositiones Mathematicae, Volume 37, Issue 2, 2019](https://www.sciencedirect.com/science/article/pii/S0723086918300021)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_correlation_matrix import PostAssetsCorrelationMatrixDistanceRequestDistanceMetric

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix_distance(
    assets=3,
    assets_correlation_matrix=[
        [
            1,
            0.5,
            0.9
        ],
        [
            0.5,
            1,
            0.7
        ],
        [
            0.9,
            0.7,
            1
        ]
    ],
    distance_metric=PostAssetsCorrelationMatrixDistanceRequestDistanceMetric.CORRELATION_MATRIX,
    reference_correlation_matrix=[
        [
            1,
            1,
            1
        ],
        [
            1,
            1,
            1
        ],
        [
            1,
            1,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**reference_correlation_matrix:** `typing.List[typing.List[float]]` — referenceCorrelationMatrix[i][j] is the reference correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**distance_metric:** `typing.Optional[PostAssetsCorrelationMatrixDistanceRequestDistanceMetric]` — The distance metric to use to compute the distance between the asset correlation matrix and the reference correlation matrix
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix_effective_rank</a>(...) -> PostAssetsCorrelationMatrixEffectiveRankResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the effective rank of an asset correlation matrix.

References
* [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix_effective_rank(
    assets=2,
    assets_correlation_matrix=[
        [
            1,
            0
        ],
        [
            0,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix_informativeness</a>(...) -> PostAssetsCorrelationMatrixInformativenessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the informativeness of an asset correlation matrix, using one of the following distance metrics:
* Euclidean distance (default), which is the distance induced by [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm)
* Correlation matrix distance, defined in the second reference, which corresponds to [the cosine distance](https://en.wikipedia.org/wiki/Cosine_similarity) between the two vectorized asset correlation matrices
* Bures distance, defined in the third reference

 References
 * [Austin J. Brockmeier and Tingting Mu and Sophia Ananiadou and John Y. Goulermas, Quantifying the Informativeness of Similarity Measurements, Journal of Machine Learning Research, 2017](http://jmlr.org/papers/v18/16-296.html)
 * [M. Herdin, N. Czink, H. Ozcelik and E. Bonek, Correlation matrix distance, a meaningful measure for evaluation of non-stationary MIMO channels, 2005 IEEE 61st Vehicular Technology Conference, 2005, pp. 136-140 Vol. 1](https://ieeexplore.ieee.org/document/1543265)
 * [Rajendra Bhatia, Tanvi Jain, Yongdo Lim, On the Bures–Wasserstein distance between positive definite matrices, Expositiones Mathematicae, Volume 37, Issue 2, 2019](https://www.sciencedirect.com/science/article/pii/S0723086918300021)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_correlation_matrix import PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix_informativeness(
    assets=3,
    assets_correlation_matrix=[
        [
            1,
            0.5,
            0.9
        ],
        [
            0.5,
            1,
            0.7
        ],
        [
            0.9,
            0.7,
            1
        ]
    ],
    distance_metric=PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric.BURES,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**distance_metric:** `typing.Optional[PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric]` — The distance metric to use to compute the informativeness of the asset correlation matrix
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">nearest_correlation_matrix</a>(...) -> PostAssetsCorrelationMatrixNearestResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the _closest_ - in terms of [the Frobenius norm](https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm) - asset correlation matrix to an approximate asset correlation matrix, optionally keeping a selected number of correlations fixed.

References
* [Nicholas J. Higham, Computing the Nearest Correlation Matrix—A Problem from Finance, IMA J. Numer. Anal. 22, 329–343, 2002.](http://www.maths.manchester.ac.uk/~higham/narep/narep369.pdf)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.nearest_correlation_matrix(
    assets=3,
    assets_approximate_correlation_matrix=[
        [
            1,
            1,
            0
        ],
        [
            1,
            1,
            1
        ],
        [
            0,
            1,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_approximate_correlation_matrix:** `typing.List[typing.List[float]]` — assetsApproximateCorrelationMatrix[i][i] is the approximate correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_fixed_correlations:** `typing.Optional[typing.List[typing.List[int]]]` — assetsFixedCorrelations[k] is the couple of indices (i,j) of the assets i and j for which to keep the approximate correlation assetsApproximateCorrelationMatrix[i][j] fixed
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">random_correlation_matrix</a>(...) -> PostAssetsCorrelationMatrixRandomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an asset correlation matrix uniformly at random over the space of positive definite correlation matrices.

References
* [Joe, H., Generating random correlation matrices based on partial correlations. Journal of Multivariate Analysis, 2006, 97, 2177-2189](https://www.sciencedirect.com/science/article/pii/S0047259X05000886)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.random_correlation_matrix(
    assets=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix_shrinkage</a>(...) -> PostAssetsCorrelationMatrixShrinkageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute an asset correlation matrix as a convex linear combination of an asset correlation matrix and a target correlation matrix, the target correlation matrix being either:  
 * An equicorrelation matrix made of 1
 * An equicorrelation matrix made of 0
 * An equicorrelation matrix made of -1/(n-1), with n the number of assets
 * A provided correlation matrix
 
 References
 * [Steiner, Andreas, Manipulating Valid Correlation Matrices](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1878165)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_correlation_matrix import PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix_shrinkage(
    request=PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix(
        assets=3,
        assets_correlation_matrix=[
            [
                1,
                0.5,
                0.9
            ],
            [
                0.5,
                1,
                0.7
            ],
            [
                0.9,
                0.7,
                1
            ]
        ],
        shrinkage_factor=0.5,
        target_correlation_matrix=[
            [
                1,
                0,
                0
            ],
            [
                0,
                1,
                0
            ],
            [
                0,
                0,
                1
            ]
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostAssetsCorrelationMatrixShrinkageRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">theory_implied_correlation_matrix</a>(...) -> PostAssetsCorrelationMatrixTheoryImpliedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the theory-implied asset correlation matrix associated with:
* A hierarchical classification of a universe of assets
* An asset correlation matrix

References
* [Lopez de Prado, Marcos Estimation of Theory-Implied Correlation Matrices (November 9, 2019)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3484152)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_correlation_matrix import PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.theory_implied_correlation_matrix(
    assets=[
        PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(
            asset_hierarchical_classification=[
                35,
                3510,
                351010,
                35101010
            ],
        ),
        PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem(
            asset_hierarchical_classification=[
                20,
                2030,
                203020,
                20302010
            ],
        )
    ],
    assets_correlation_matrix=[
        [
            1,
            -0.00035
        ],
        [
            -0.00035,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**clustering_method:** `typing.Optional[PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod]` — The hierarchical clustering method to use
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_correlation_matrix.<a href="src/fern/assets_correlation_matrix/client.py">correlation_matrix_validation</a>(...) -> PostAssetsCorrelationMatrixValidationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate whether a matrix is an asset correlation matrix.

References
* [Wikipedia, Correlation and Dependence](https://en.wikipedia.org/wiki/Correlation_and_dependence#Correlation_matrices)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_correlation_matrix.correlation_matrix_validation(
    assets=2,
    assets_correlation_matrix=[
        [
            1,
            -0.00035
        ],
        [
            -0.00035,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsCovarianceMatrix
<details><summary><code>client.assets_covariance_matrix.<a href="src/fern/assets_covariance_matrix/client.py">covariance_matrix</a>(...) -> PostAssetsCovarianceMatrixResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the covariance matrix of assets from either:  
* The asset correlation matrix and their volatilities (i.e., standard deviations)
* The asset correlation matrix and their variances
* The asset returns

References
* [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_covariance_matrix import PostAssetsCovarianceMatrixRequestAssets

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_covariance_matrix.covariance_matrix(
    request=PostAssetsCovarianceMatrixRequestAssets(
        assets=2,
        assets_correlation_matrix=[
            [
                1,
                -0.5
            ],
            [
                -0.5,
                1
            ]
        ],
        assets_volatilities=[
            0.1,
            0.05
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostAssetsCovarianceMatrixRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_covariance_matrix.<a href="src/fern/assets_covariance_matrix/client.py">covariance_matrix_effective_rank</a>(...) -> PostAssetsCovarianceMatrixEffectiveRankResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the effective rank of an asset covariance matrix.

References
* [Olivier Roy and Martin Vetterli, The effective rank: A measure of effective dimensionality, 15th European Signal Processing Conference, 2007](https://ieeexplore.ieee.org/document/7098875)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_covariance_matrix.covariance_matrix_effective_rank(
    assets=2,
    assets_covariance_matrix=[
        [
            0.00035,
            -0.00035
        ],
        [
            -0.00035,
            0.00035
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_covariance_matrix.<a href="src/fern/assets_covariance_matrix/client.py">exponentially_weighted_covariance_matrix</a>(...) -> PostAssetsCovarianceMatrixExponentiallyWeightedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute an exponentially weighted covariance matrix of assets returns.

References
* [RiskMetrics Group. Longerstaey, J. (1996). RiskMetrics technical document, Technical Report fourth edition](https://www.msci.com/documents/10199/5915b101-4206-4ba0-aee2-3449d5c7e95a)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_covariance_matrix import PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_covariance_matrix.exponentially_weighted_covariance_matrix(
    assets=[
        PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(
            asset_returns=[
                0.01,
                0.01,
                0.02,
                0.01
            ],
        ),
        PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem(
            asset_returns=[
                -0.02,
                -0.02,
                -0.04,
                -0.02
            ],
        )
    ],
    decay_factor=0.5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**decay_factor:** `typing.Optional[float]` — The exponential decay factor
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_covariance_matrix.<a href="src/fern/assets_covariance_matrix/client.py">covariance_matrix_validation</a>(...) -> PostAssetsCovarianceMatrixValidationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Validate whether a matrix is a covariance matrix.

References
* [Wikipedia, Covariance Matrix](https://en.wikipedia.org/wiki/Covariance_matrix)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_covariance_matrix.covariance_matrix_validation(
    assets=2,
    assets_covariance_matrix=[
        [
            0.00035,
            -0.00035
        ],
        [
            -0.00035,
            0.00035
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsKurtosis
<details><summary><code>client.assets_kurtosis.<a href="src/fern/assets_kurtosis/client.py">kurtosis</a>(...) -> PostAssetsKurtosisResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the kurtosis of one or several asset(s), from the asset returns.

References
* [Wikipedia, Kurtosis](https://en.wikipedia.org/wiki/Kurtosis)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_kurtosis import PostAssetsKurtosisRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_kurtosis.kurtosis(
    assets=[
        PostAssetsKurtosisRequestAssetsItem(
            asset_returns=[
                0.01,
                0,
                0.02,
                -0.03
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsKurtosisRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsPrices
<details><summary><code>client.assets_prices.<a href="src/fern/assets_prices/client.py">adjusted_prices</a>(...) -> PostAssetsPricesAdjustedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the backward-adjusted prices of one or several asset(s) for one or several date(s) from:
* Unadjusted prices
* Capital distributions, like stock dividends
* Splits, like stock splits

The adjustment base date is chosen to be the last date for which unadjusted prices are available, which implies that:
* The price on the last date for which unadjusted prices are available is left unadjusted
* The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the last date for which unadjusted prices are available

References
* [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_prices import PostAssetsPricesAdjustedRequestAssetsItem, PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem, PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_prices.adjusted_prices(
    assets=[
        PostAssetsPricesAdjustedRequestAssetsItem(
            asset_prices=[
                PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                    close=2213.4,
                    date="2020-08-28",
                ),
                PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                    close=498.32,
                    date="2020-08-31",
                ),
                PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem(
                    close=475.05,
                    date="2020-09-01",
                )
            ],
            asset_splits=[
                PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem(
                    date="2020-08-31",
                    factor=5,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsPricesAdjustedRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_prices.<a href="src/fern/assets_prices/client.py">forward_adjusted_prices</a>(...) -> PostAssetsPricesAdjustedForwardResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the forward-adjusted prices of one or several asset(s) for one or several date(s) from:
* Unadjusted prices
* Capital distributions, like stock dividends
* Splits, like stock splits

The adjustment base date is chosen to be the first date for which unadjusted prices are available, which implies that:
* The price on the first date for which unadjusted prices are available is left unadjusted
* The price on any other date is adjusted based on the capital distributions and the splits which occurred between this date and the first date for which unadjusted prices are available

References
* [Center for Research in Security Prices](https://www.crsp.org/products/documentation/crsp-calculations)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_prices import PostAssetsPricesAdjustedForwardRequestAssetsItem, PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem, PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_prices.forward_adjusted_prices(
    assets=[
        PostAssetsPricesAdjustedForwardRequestAssetsItem(
            asset_prices=[
                PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                    close=2213.4,
                    date="2020-08-28",
                ),
                PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                    close=498.32,
                    date="2020-08-31",
                ),
                PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem(
                    close=475.05,
                    date="2020-09-01",
                )
            ],
            asset_splits=[
                PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem(
                    date="2020-08-31",
                    factor=5,
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsPricesAdjustedForwardRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsReturns
<details><summary><code>client.assets_returns.<a href="src/fern/assets_returns/client.py">arithmetic_returns</a>(...) -> PostAssetsReturnsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the arithmetic return(s) of one or several asset(s) for one or several time period(s).

References
* [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_returns import PostAssetsReturnsRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_returns.arithmetic_returns(
    assets=[
        PostAssetsReturnsRequestAssetsItem(
            asset_prices=[
                1,
                2
            ],
        ),
        PostAssetsReturnsRequestAssetsItem(
            asset_prices=[
                2,
                3,
                6
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsReturnsRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.assets_returns.<a href="src/fern/assets_returns/client.py">arithmetic_average_return</a>(...) -> PostAssetsReturnsAverageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the arithmetic average of the return(s) of one or several asset(s).

References
* [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_returns import PostAssetsReturnsAverageRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_returns.arithmetic_average_return(
    assets=[
        PostAssetsReturnsAverageRequestAssetsItem(
            asset_returns=[
                0.1,
                -0.05
            ],
        ),
        PostAssetsReturnsAverageRequestAssetsItem(
            asset_returns=[
                0,
                -0.01,
                0.01
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsReturnsAverageRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsReturnsSimulation
<details><summary><code>client.assets_returns_simulation.<a href="src/fern/assets_returns_simulation/client.py">bootstrap</a>(...) -> PostAssetsReturnsSimulationBootstrapResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simulate the return(s) of one or several asset(s) for one or several time period(s) using a bootstrap method.

References
* [Efron, B. (1979), Bootstrap methods: Another look at the jackknife, The Annals of Statistics 7, 1-26](https://projecteuclid.org/journals/annals-of-statistics/volume-7/issue-1/Bootstrap-Methods-Another-Look-at-the-Jackknife/10.1214/aos/1176344552.full)
* [Politis, D. N. and Romano, J. P., A circular block resampling procedure for stationary data, in R. Lepage and L. Billard, eds, Exploring the Limits of Bootstrap, Wiley, New York, pp. 263-270](https://statistics.stanford.edu/technical-reports/circular-block-resampling-procedure-stationary-data)
* [Politis, D. N. and Romano, J. P., The stationary bootstrap, Journal of the American Statistical Association 89, 1303-1313](https://www.jstor.org/stable/2290993)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_returns_simulation import PostAssetsReturnsSimulationBootstrapRequestAssetsItem, PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_returns_simulation.bootstrap(
    assets=[
        PostAssetsReturnsSimulationBootstrapRequestAssetsItem(
            asset_returns=[
                0.1,
                -0.05,
                0.01,
                0.025,
                -0.1
            ],
        ),
        PostAssetsReturnsSimulationBootstrapRequestAssetsItem(
            asset_returns=[
                0,
                0.01,
                0.02,
                -0.01,
                0.05
            ],
        )
    ],
    bootstrap_block_length=2,
    bootstrap_method=PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod.CIRCULAR_BLOCK,
    simulations=5,
    simulations_length=4,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsReturnsSimulationBootstrapRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**bootstrap_average_block_length:** `typing.Optional[float]` — The average length of the blocks to use in case the bootstrap method is 'stationaryBlock', in time periods; if not provided, defaults to the inverse of 3.15 * the common length of the assetReturns arrays^1/3
    
</dd>
</dl>

<dl>
<dd>

**bootstrap_block_length:** `typing.Optional[int]` — The length of the blocks to use in case the bootstrap method is 'circularBlock', in time periods; if not provided, defaults to [3.15 * the common length of the assetReturns arrays^1/3]
    
</dd>
</dl>

<dl>
<dd>

**bootstrap_method:** `typing.Optional[PostAssetsReturnsSimulationBootstrapRequestBootstrapMethod]` — The bootstrap method to use
    
</dd>
</dl>

<dl>
<dd>

**simulations:** `typing.Optional[int]` — The number of simulations to perform
    
</dd>
</dl>

<dl>
<dd>

**simulations_length:** `typing.Optional[int]` — The number of time period(s) to simulate per simulation; if not provided, defaults to the common length of the assetReturns arrays
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsSkewness
<details><summary><code>client.assets_skewness.<a href="src/fern/assets_skewness/client.py">skewness</a>(...) -> PostAssetsSkewnessResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the skewness of one or several asset(s), from the asset returns.

References
* [Wikipedia, Skewness](https://en.wikipedia.org/wiki/Skewness)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_skewness import PostAssetsSkewnessRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_skewness.skewness(
    assets=[
        PostAssetsSkewnessRequestAssetsItem(
            asset_returns=[
                0.01,
                0,
                0.02,
                -0.03
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostAssetsSkewnessRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsVariance
<details><summary><code>client.assets_variance.<a href="src/fern/assets_variance/client.py">variance</a>(...) -> PostAssetsVarianceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the variance of one or several asset(s) from either:  
* The asset returns
* The asset covariance matrix
* The asset volatility(ies)

References
* [Wikipedia, Variance](https://en.wikipedia.org/wiki/Variance)        
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_variance import PostAssetsVarianceRequestAssetsCovarianceMatrix

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_variance.variance(
    request=PostAssetsVarianceRequestAssetsCovarianceMatrix(
        assets=2,
        assets_covariance_matrix=[
            [
                0.01,
                -0.0025
            ],
            [
                -0.0025,
                0.0025
            ]
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostAssetsVarianceRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetsVolatility
<details><summary><code>client.assets_volatility.<a href="src/fern/assets_volatility/client.py">volatility</a>(...) -> PostAssetsVolatilityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the volatility (i.e., standard deviation) of one or several asset(s) from either:  
* The asset returns
* The asset covariance matrix
* The asset variance(s)

References
* [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.assets_volatility import PostAssetsVolatilityRequestAssetsCovarianceMatrix

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.assets_volatility.volatility(
    request=PostAssetsVolatilityRequestAssetsCovarianceMatrix(
        assets=2,
        assets_covariance_matrix=[
            [
                0.01,
                -0.0025
            ],
            [
                -0.0025,
                0.0025
            ]
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostAssetsVolatilityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Factors
<details><summary><code>client.factors.<a href="src/fern/factors/client.py">residualization</a>(...) -> PostFactorsResidualizationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the residuals of a factor against a set of factors, using a returns-based linear regression analysis.

References
* [Factor Research, Factor Exposure Analysis: Exploring Residualization](https://insights.factorresearch.com/research-factor-exposure-analysis-exploring-residualization/)
* [Catalina B. Garcia, Román Salmeron, Claudia Garcia & Jose Garcia (2019): Residualization: justification, properties and application, Journal of Applied Statistics](https://doi.org/10.1080/02664763.2019.1701638)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.factors import PostFactorsResidualizationRequestFactorsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.factors.residualization(
    factors=[
        PostFactorsResidualizationRequestFactorsItem(
            factor_returns=[
                0.01,
                0.02,
                -0.01
            ],
        ),
        PostFactorsResidualizationRequestFactorsItem(
            factor_returns=[
                0.025,
                0.005,
                -0.02
            ],
        )
    ],
    residualized_factor=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**factors:** `typing.List[PostFactorsResidualizationRequestFactorsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**residualized_factor:** `int` — The index of the factor to residualize
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PortfolioAnalysis
<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">alpha</a>(...) -> PostPortfolioAnalysisAlphaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the Jensen’s alpha of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution  
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisAlphaRequestRiskFreeRate, PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.alpha(
    request=PostPortfolioAnalysisAlphaRequestRiskFreeRate(
        benchmark_returns=[
            0.002,
            0.025,
            0.018,
            -0.011,
            0.014
        ],
        portfolios=[
            PostPortfolioAnalysisAlphaRequestRiskFreeRatePortfoliosItem(
                portfolio_returns=[
                    0.003,
                    0.026,
                    0.011,
                    -0.01,
                    0.015
                ],
            )
        ],
        risk_free_rate=0.01,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisAlphaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">beta</a>(...) -> PostPortfolioAnalysisBetaResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the beta of one or several portfolio(s) in the Capital Asset Pricing Model (CAPM).

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution  
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisBetaRequestRiskFreeRate, PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.beta(
    request=PostPortfolioAnalysisBetaRequestRiskFreeRate(
        benchmark_returns=[
            0.002,
            0.025,
            0.018,
            -0.011,
            0.014
        ],
        portfolios=[
            PostPortfolioAnalysisBetaRequestRiskFreeRatePortfoliosItem(
                portfolio_returns=[
                    0.003,
                    0.026,
                    0.011,
                    -0.01,
                    0.015
                ],
            )
        ],
        risk_free_rate=0.01,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisBetaRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">conditional_value_at_risk</a>(...) -> PostPortfolioAnalysisConditionalValueAtRiskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the conditional value at risk of one or several portfolio(s) from portfolio values.

References
* [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
* [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.conditional_value_at_risk(
    alpha=0.05,
    portfolios=[
        PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alpha:** `float` — The conditional value at risk level
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisConditionalValueAtRiskRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">return_contributions</a>(...) -> PostPortfolioAnalysisContributionsReturnResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a return contribution analysis of one or several portfolio(s), optionally using groups of assets.

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.return_contributions(
    assets=3,
    assets_groups=[
        [
            1,
            2
        ]
    ],
    assets_returns=[
        0.01,
        -0.01,
        0.025
    ],
    portfolios=[
        PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem(
            assets_weights=[
                0.5,
                0.25,
                0.25
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisContributionsReturnRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_groups:** `typing.Optional[typing.List[typing.List[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">risk_contributions</a>(...) -> PostPortfolioAnalysisContributionsRiskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Perform a risk contribution analysis of one or several portfolio(s), optionally using groups of assets.

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.risk_contributions(
    assets=3,
    assets_covariance_matrix=[
        [
            0.0001,
            0,
            0
        ],
        [
            0,
            0.0001,
            0
        ],
        [
            0,
            0,
            0.04
        ]
    ],
    portfolios=[
        PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem(
            assets_weights=[
                0.5,
                0.25,
                0.25
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisContributionsRiskRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_groups:** `typing.Optional[typing.List[typing.List[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">correlation_spectrum</a>(...) -> PostPortfolioAnalysisCorrelationSpectrumResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the correlation spectrum of one or several portfolio(s).

References
* [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix, PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.correlation_spectrum(
    request=PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrix(
        assets=2,
        assets_covariance_matrix=[
            [
                0.0025,
                0.0005
            ],
            [
                0.0005,
                0.01
            ]
        ],
        portfolios=[
            PostPortfolioAnalysisCorrelationSpectrumRequestAssetsCovarianceMatrixPortfoliosItem(
                assets_weights=[
                    0.5,
                    0.5
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisCorrelationSpectrumRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">diversification_ratio</a>(...) -> PostPortfolioAnalysisDiversificationRatioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the diversification ratio of one or several portfolio(s).

References
* [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)
* [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix, PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.diversification_ratio(
    request=PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrix(
        assets=2,
        assets_covariance_matrix=[
            [
                0.0025,
                0.0005
            ],
            [
                0.0005,
                0.01
            ]
        ],
        portfolios=[
            PostPortfolioAnalysisDiversificationRatioRequestAssetsCovarianceMatrixPortfoliosItem(
                assets_weights=[
                    0.5,
                    0.5
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisDiversificationRatioRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">drawdowns</a>(...) -> PostPortfolioAnalysisDrawdownsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the drawdown function - also called the underwater equity curve -, as well as the worst 10 drawdowns of one or several portfolio(s).

References
* [Wikipedia, Drawdown](https://en.wikipedia.org/wiki/Drawdown_(economics))        
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisDrawdownsRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.drawdowns(
    portfolios=[
        PostPortfolioAnalysisDrawdownsRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisDrawdownsRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">effective_number_of_bets</a>(...) -> PostPortfolioAnalysisEffectiveNumberOfBetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the effective number of bets of one or several portfolio(s).

References
* [Meucci, Attilio and Santangelo, Alberto and Deguest, Romain, Risk Budgeting and Diversification Based on Optimized Uncorrelated Factors (November 10, 2015)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2276632)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.effective_number_of_bets(
    assets=3,
    assets_covariance_matrix=[
        [
            1,
            0,
            0
        ],
        [
            0,
            286.31,
            100.79
        ],
        [
            0,
            100.79,
            601.36
        ]
    ],
    portfolios=[
        PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem(
            assets_weights=[
                10.96,
                1.06,
                0.22
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisEffectiveNumberOfBetsRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**factors_extraction_method:** `typing.Optional[PostPortfolioAnalysisEffectiveNumberOfBetsRequestFactorsExtractionMethod]` — The method used to extract the uncorrelated risk factors from the asset covariance matrix
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">factor_exposures</a>(...) -> PostPortfolioAnalysisFactorsExposuresResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the exposures of one or several portfolio(s) to a set of factors, using a returns-based linear regression analysis.

References
* [Measuring Factor Exposures: Uses and Abuses, Ronen Israel and Adrienne Ross, The Journal of Alternative Investments Summer 2017, 20 (1) 10-25](https://jai.pm-research.com/content/20/1/10.short) 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisFactorsExposuresRequestFactorsItem, PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.factor_exposures(
    factors=[
        PostPortfolioAnalysisFactorsExposuresRequestFactorsItem(
            factor_returns=[
                -0.00414169934,
                0.01201656108,
                0.0087181369
            ],
        ),
        PostPortfolioAnalysisFactorsExposuresRequestFactorsItem(
            factor_returns=[
                -0.01387258782,
                -0.01097961581,
                0.01742002062
            ],
        )
    ],
    portfolios=[
        PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem(
            portfolio_returns=[
                -0.04302,
                0.01310372213,
                0.06482589323
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisFactorsExposuresRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**factors:** `typing.Optional[typing.List[PostPortfolioAnalysisFactorsExposuresRequestFactorsItem]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">mean_variance_efficient_frontier</a>(...) -> PostPortfolioAnalysisMeanVarianceEfficientFrontierResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the discretized mean-variance efficient frontier associated to a list of assets, optionally subject to:
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraint

References
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.mean_variance_efficient_frontier(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    assets_returns=[
        0.01,
        0.05
    ],
    constraints=PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints(
        minimum_assets_weights=[
            0.2,
            0
        ],
    ),
    portfolios=3,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioAnalysisMeanVarianceEfficientFrontierRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.Optional[int]` — The number of portfolios to compute on the mean-variance efficient frontier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">mean_variance_minimum_variance_frontier</a>(...) -> PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the discretized mean-variance minimum variance frontier associated to a list of assets, optionally subject to:
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraint

> This endpoint is similar to the endpoint [`/portfolio/analysis/mean-variance/efficient-frontier`](#post-/portfolio/analysis/mean-variance/efficient-frontier), because the mean-variance efficient frontier is the "top" portion of the mean-variance minimum variance frontier.

References
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.mean_variance_minimum_variance_frontier(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    assets_returns=[
        0.01,
        0.05
    ],
    constraints=PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints(
        minimum_assets_weights=[
            0.2,
            0
        ],
    ),
    portfolios=4,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioAnalysisMeanVarianceMinimumVarianceFrontierRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.Optional[int]` — The number of portfolios to compute on the mean-variance minimum variance frontier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">arithmetic_return</a>(...) -> PostPortfolioAnalysisReturnResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the arithmetic return of one or several portfolio(s) from either:  
* Portfolio assets arithmetic returns
* Portfolio values

References
* [Wikipedia, Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Return)
* Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisReturnRequestAssets, PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.arithmetic_return(
    request=PostPortfolioAnalysisReturnRequestAssets(
        assets=2,
        assets_returns=[
            0.01,
            0.05
        ],
        portfolios=[
            PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem(
                assets_weights=[
                    1,
                    0
                ],
            ),
            PostPortfolioAnalysisReturnRequestAssetsPortfoliosItem(
                assets_weights=[
                    0,
                    1
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisReturnRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">arithmetic_average_return</a>(...) -> PostPortfolioAnalysisReturnsAverageResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the arithmetic average of the arithmetic return(s) of one or several portfolio(s).

References
* [Wikipedia, Arithmetic Average Rate of Return](https://en.wikipedia.org/wiki/Rate_of_return#Arithmetic_average_rate_of_return)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.arithmetic_average_return(
    portfolios=[
        PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisReturnsAverageRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">tracking_error</a>(...) -> PostPortfolioAnalysisTrackingErrorResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the tracking error between a benchmark and one or several portfolio(s).

References
* [Wikipedia, Tracking error](https://en.wikipedia.org/wiki/Tracking_error) 
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution 
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.tracking_error(
    benchmark_returns=[
        0.002,
        0.025,
        0.018,
        -0.011,
        0.014,
        0.018,
        0.014,
        0.065,
        -0.015,
        0.042,
        -0.006,
        0.083,
        0.039,
        -0.038,
        -0.062,
        0.015,
        -0.048,
        0.021,
        0.06,
        0.056,
        -0.067,
        0.019,
        -0.003,
        0
    ],
    portfolios=[
        PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem(
            portfolio_returns=[
                0.003,
                0.026,
                0.011,
                -0.01,
                0.015,
                0.025,
                0.016,
                0.067,
                -0.014,
                0.04,
                -0.005,
                0.081,
                0.04,
                -0.037,
                -0.061,
                0.017,
                -0.049,
                -0.022,
                0.07,
                0.058,
                -0.065,
                0.024,
                -0.005,
                -0.009
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**benchmark_returns:** `typing.List[float]` — benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the portfolioReturns arrays
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisTrackingErrorRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">ulcer_index</a>(...) -> PostPortfolioAnalysisUlcerIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the Ulcer Index of one or several portfolio(s).

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
* [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.ulcer_index(
    portfolios=[
        PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
    risk_free_rate=1.1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisUlcerIndexRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">ulcer_performance_index</a>(...) -> PostPortfolioAnalysisUlcerPerformanceIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the Ulcer Performance Index of one or several portfolio(s).

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
* [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.ulcer_performance_index(
    portfolios=[
        PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisUlcerPerformanceIndexRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">value_at_risk</a>(...) -> PostPortfolioAnalysisValueAtRiskResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the value at risk of one or several portfolio(s) from portfolio values.

References
* [Wikipedia, Value at risk](https://en.wikipedia.org/wiki/Value_at_risk)
* [Acerbi, C. and Tasche, D. (2002), Expected Shortfall: A Natural Coherent Alternative to Value at Risk. Economic Notes, 31: 379-388](https://onlinelibrary.wiley.com/doi/abs/10.1111/1468-0300.00091)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.value_at_risk(
    alpha=0.05,
    portfolios=[
        PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**alpha:** `float` — The value at risk level
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisValueAtRiskRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis.<a href="src/fern/portfolio_analysis/client.py">volatility</a>(...) -> PostPortfolioAnalysisVolatilityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the volatility (i.e., standard deviation) of one or several portfolio(s) from either:  
* Portfolio assets covariance matrix
* Portfolio values

References
* [Wikipedia, Standard Deviation](https://en.wikipedia.org/wiki/Standard_deviation#Finance)
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
* Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis import PostPortfolioAnalysisVolatilityRequestAssets, PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis.volatility(
    request=PostPortfolioAnalysisVolatilityRequestAssets(
        assets=2,
        assets_covariance_matrix=[
            [
                0.0025,
                0.0005
            ],
            [
                0.0005,
                0.01
            ]
        ],
        portfolios=[
            PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem(
                assets_weights=[
                    1,
                    0
                ],
            ),
            PostPortfolioAnalysisVolatilityRequestAssetsPortfoliosItem(
                assets_weights=[
                    0,
                    1
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisVolatilityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PortfolioAnalysisSharpeRatio
<details><summary><code>client.portfolio_analysis_sharpe_ratio.<a href="src/fern/portfolio_analysis_sharpe_ratio/client.py">sharpe_ratio</a>(...) -> PostPortfolioAnalysisSharpeRatioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the Sharpe ratio of one or several portfolio(s) from either:
* Portfolio assets arithmetic returns and assets covariance matrix
* Portfolio values

References
* Carl R. Bacon, Practical Portfolio Performance Measurement and Attribution
* Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis_sharpe_ratio import PostPortfolioAnalysisSharpeRatioRequestAssets, PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis_sharpe_ratio.sharpe_ratio(
    request=PostPortfolioAnalysisSharpeRatioRequestAssets(
        assets=2,
        assets_covariance_matrix=[
            [
                0.0025,
                0.0005
            ],
            [
                0.0005,
                0.01
            ]
        ],
        assets_returns=[
            0.01,
            0.05
        ],
        portfolios=[
            PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem(
                assets_weights=[
                    1,
                    0
                ],
            ),
            PostPortfolioAnalysisSharpeRatioRequestAssetsPortfoliosItem(
                assets_weights=[
                    0,
                    1
                ],
            )
        ],
        risk_free_rate=0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisSharpeRatioRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis_sharpe_ratio.<a href="src/fern/portfolio_analysis_sharpe_ratio/client.py">bias_adjusted_sharpe_ratio</a>(...) -> PostPortfolioAnalysisSharpeRatioBiasAdjustedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the Sharpe ratio of one or several portfolio(s), adjusted for small sample bias.

References
* [Opdyke, J., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis_sharpe_ratio import PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis_sharpe_ratio.bias_adjusted_sharpe_ratio(
    portfolios=[
        PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisSharpeRatioBiasAdjustedRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis_sharpe_ratio.<a href="src/fern/portfolio_analysis_sharpe_ratio/client.py">sharpe_ratio_confidence_interval</a>(...) -> PostPortfolioAnalysisSharpeRatioConfidenceIntervalResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Build a confidence interval for the Sharpe ratio of one or several portfolio(s).

References
* [Opdyke, J.D., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis_sharpe_ratio import PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType, PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis_sharpe_ratio.sharpe_ratio_confidence_interval(
    confidence_interval_type=PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType.TWO_SIDED,
    confidence_level=0.99,
    portfolios=[
        PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem(
            portfolio_values=[
                100,
                95,
                100,
                90,
                85,
                70
            ],
        )
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**confidence_interval_type:** `typing.Optional[PostPortfolioAnalysisSharpeRatioConfidenceIntervalRequestConfidenceIntervalType]` — The type of confidence interval to build
    
</dd>
</dl>

<dl>
<dd>

**confidence_level:** `typing.Optional[float]` — The confidence level of the confidence interval to build, in percentage
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis_sharpe_ratio.<a href="src/fern/portfolio_analysis_sharpe_ratio/client.py">probabilistic_sharpe_ratio</a>(...) -> PostPortfolioAnalysisSharpeRatioProbabilisticResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the probabilistic Sharpe ratio of one or several portfolio(s).

References
* [Opdyke, J.D., Comparing Sharpe ratios: So where are the p-values?. J Asset Manag 8, 308–336 (2007)](https://link.springer.com/article/10.1057/palgrave.jam.2250084)
* [Bailey, David H. and Lopez de Prado, Marcos, The Sharpe Ratio Efficient Frontier (April 1, 2012). Journal of Risk, Vol. 15, No. 2, Winter 2012/13](https://ssrn.com/abstract=1821643)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis_sharpe_ratio import PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues, PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis_sharpe_ratio.probabilistic_sharpe_ratio(
    request=PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValues(
        benchmark_values=[
            100,
            101,
            98,
            102,
            95,
            90
        ],
        portfolios=[
            PostPortfolioAnalysisSharpeRatioProbabilisticRequestBenchmarkValuesPortfoliosItem(
                portfolio_values=[
                    100,
                    95,
                    100,
                    90,
                    85,
                    70
                ],
            )
        ],
        risk_free_rate=0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisSharpeRatioProbabilisticRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_analysis_sharpe_ratio.<a href="src/fern/portfolio_analysis_sharpe_ratio/client.py">minimum_track_record_length</a>(...) -> PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the minimum track record length of one or several portfolio(s).

References
* [Bailey, David H. and Lopez de Prado, Marcos, The Sharpe Ratio Efficient Frontier (April 1, 2012). Journal of Risk, Vol. 15, No. 2, Winter 2012/13](https://ssrn.com/abstract=1821643)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_analysis_sharpe_ratio import PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues, PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_analysis_sharpe_ratio.minimum_track_record_length(
    request=PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValues(
        benchmark_values=[
            100,
            101,
            98,
            85,
            75,
            65
        ],
        portfolios=[
            PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequestBenchmarkValuesPortfoliosItem(
                portfolio_values=[
                    100,
                    95,
                    100,
                    90,
                    85,
                    70
                ],
            )
        ],
        risk_free_rate=0,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PostPortfolioAnalysisSharpeRatioProbabilisticMinimumTrackRecordLengthRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PortfolioConstruction
<details><summary><code>client.portfolio_construction.<a href="src/fern/portfolio_construction/client.py">investable_portfolio</a>(...) -> PostPortfolioConstructionInvestableResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_construction.investable_portfolio(
    assets=4,
    assets_groups=[
        [
            1,
            2
        ],
        [
            3,
            4
        ]
    ],
    assets_groups_weights=[
        0.4,
        0.4
    ],
    assets_prices=[
        10,
        25,
        100,
        500
    ],
    assets_weights=[
        0.2,
        1.1,
        1.1,
        1.1
    ],
    portfolio_value=10000,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_prices:** `typing.List[float]` — assetsPrices[i] is the price of the asset i
    
</dd>
</dl>

<dl>
<dd>

**portfolio_value:** `float` — The monetary value of the portfolio
    
</dd>
</dl>

<dl>
<dd>

**assets_groups:** `typing.Optional[typing.List[typing.List[int]]]` 
    
</dd>
</dl>

<dl>
<dd>

**assets_groups_weights:** `typing.Optional[typing.List[float]]` — assetsGroupsWeights[i] is the desired weight of the assets group k in the portfolio, in percentage (can be null to indicate no specific desire); requires assetsGroups to be present
    
</dd>
</dl>

<dl>
<dd>

**assets_minimum_notional_values:** `typing.Optional[typing.List[float]]` — assetsMinimumNotionalValues[i] is the minimum monetary value that the position in the asset i is required to represent when the asset i is included in the portfolio
    
</dd>
</dl>

<dl>
<dd>

**assets_minimum_positions:** `typing.Optional[typing.List[float]]` — assetsMinimumPositions[i] is the minimum number of shares of the asset i that is required to purchase when the asset i is included in the portfolio (usual values are the same as for assetsSizeLots)
    
</dd>
</dl>

<dl>
<dd>

**assets_size_lots:** `typing.Optional[typing.List[float]]` — assetsSizeLots[i] is the number of shares by which it is required to purchase the asset i (usual values are 1 if the asset needs to be purchased share by share, 100 if the asset needs to be purchased by an integer multiple of 100 shares, and 1/1000000 - e.g. for Robinhood broker - if the asset can be purchased by fractional shares)
    
</dd>
</dl>

<dl>
<dd>

**assets_weights:** `typing.Optional[typing.List[float]]` — assetsWeights[i] is the desired weight of the asset i in the portfolio, in percentage (can be null to indicate no specific desire)
    
</dd>
</dl>

<dl>
<dd>

**maximum_assets_groups_weights:** `typing.Optional[typing.List[float]]` — maximumAssetsGroupsWeights[k] is the maximum desired weight of the assets group k in the portfolio, in percentage (can be null to indicate no specific desire); requires assetsGroups to be present
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_construction.<a href="src/fern/portfolio_construction/client.py">mimicking_portfolio</a>(...) -> PostPortfolioConstructionMimickingResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Construct a portfolio as close as possible, in terms of returns, to a benchmark, optionally subject to:
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References 
* Konstantinos Benidis, Yiyong Feng, Daniel P. Palomar, Optimization Methods for Financial Index Tracking: From Theory to Practice, now publishers Inc (7 juin 2018)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_construction import PostPortfolioConstructionMimickingRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_construction.mimicking_portfolio(
    assets=[
        PostPortfolioConstructionMimickingRequestAssetsItem(
            asset_returns=[
                0.01,
                0.02,
                0.03
            ],
        ),
        PostPortfolioConstructionMimickingRequestAssetsItem(
            asset_returns=[
                -0.01,
                -0.02,
                -0.03
            ],
        )
    ],
    benchmark_returns=[
        0,
        0,
        0
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostPortfolioConstructionMimickingRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**benchmark_returns:** `typing.List[float]` — benchmarkReturns[t] is the return of the benchmark at the time t; the benchmarkReturns array must have the same length as all the assetReturns arrays
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioConstructionMimickingRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_construction.<a href="src/fern/portfolio_construction/client.py">random_portfolio</a>(...) -> PostPortfolioConstructionRandomResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Construct one or several random portfolio(s), optionally subject to:       
* Minimum and maximum weights constraints
* Minimum and maximum portfolio exposure constraints

> Because of the nature of the endpoint, subsequent calls with the same input data will result in different output data.

References
* [William Thornton Shaw, Monte Carlo Portfolio Optimization for General Investor Risk-Return Objectives and Arbitrary Return Distributions: A Solution for Long-Only Portfolios](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1680224)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_construction.random_portfolio(
    assets=3,
    portfolios=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioConstructionRandomRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.Optional[int]` — The number of portfolios to construct
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PortfolioOptimization
<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">equal_risk_contributions_portfolio</a>(...) -> PostPortfolioOptimizationEqualRiskContributionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the equal risk contributions portfolio, optionally subject to:  
* Minimum and maximum weights constraints  

References
 * [Richard, Jean-Charles and Roncalli, Thierry, Constrained Risk Budgeting Portfolios: Theory, Algorithms, Applications & Puzzles](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3331184)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization import PostPortfolioOptimizationEqualRiskContributionsRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.equal_risk_contributions_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    constraints=PostPortfolioOptimizationEqualRiskContributionsRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationEqualRiskContributionsRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">equal_sharpe_ratio_contributions_portfolio</a>(...) -> PostPortfolioOptimizationEqualSharpeRatioContributionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the equal Sharpe Ratio contributions portfolio.

References
 * [Andreas Steiner, Sharpe Ratio Contribution and Attribution Analysis](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1839166")
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.equal_sharpe_ratio_contributions_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.05,
            0.02
        ],
        [
            0.02,
            0.07
        ]
    ],
    assets_returns=[
        0.05,
        0.1
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">equal_volatility_weighted_portfolio</a>(...) -> PostPortfolioOptimizationEqualVolatilityWeightedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the equal volatility-weighted portfolio.

References
 * [Tristan Froidure, Khalid Jalalzai and Yves Choueifaty, Portfolio Rho-Representativity, International Journal of Theoretical and Applied FinanceVol. 22, No. 07, 1950034 (2019)](https://www.worldscientific.com/doi/10.1142/S0219024919500341)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.equal_volatility_weighted_portfolio(
    assets=2,
    assets_volatilities=[
        0.05,
        0.1
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_volatilities:** `typing.List[float]` — assetsVolatilities[i] is the volatility of the asset i
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">equal_weighted_portfolio</a>(...) -> PostPortfolioOptimizationEqualWeightedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the equal-weighted portfolio.

References
 * [Victor DeMiguel and al., Optimal Versus Naive Diversification: How Inefficient is the 1/N Portfolio Strategy?](https://academic.oup.com/rfs/article-abstract/22/5/1915/1592901?redirectedFrom=fulltext)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.equal_weighted_portfolio(
    assets=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">hierarchical_risk_parity_portfolio</a>(...) -> PostPortfolioOptimizationHierarchicalRiskParityResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the hierarchical risk parity portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [Lopez de Prado, M. (2016). Building diversified portfolios that outperform out-of-sample. Journal of Portfolio Management, 42(4), 59–69](https://jpm.pm-research.com/content/42/4/59)
 * [Johann Pfitzinger & Nico Katzke, 2019. A constrained hierarchical risk parity algorithm with cluster-based capital allocation. Working Papers 14/2019, Stellenbosch University, Department of Economics](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization import PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.hierarchical_risk_parity_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    constraints=PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
        maximum_portfolio_exposure=0.5,
        minimum_portfolio_exposure=0.5,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**clustering_method:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringMethod]` — The hierarchical clustering method to use
    
</dd>
</dl>

<dl>
<dd>

**clustering_ordering:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestClusteringOrdering]` — The order to impose on the hierarchical clustering tree leaves
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">hierarchical_clustering_based_risk_parity_portfolio</a>(...) -> PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the hierarchical clustering-based risk parity portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [Machine Learning for Asset Management: New Developments and Financial Applications, Emmanuel Jurczenko, Chapter 9, Harald Lohre,Carsten Rother,Kilian Axel Schäfer, Hierarchical Risk Parity: Accounting for Tail Dependencies in Multi-asset Multi-factor Allocations](https://onlinelibrary.wiley.com/doi/10.1002/9781119751182.ch9)
 * [Thomas Raffinot, Hierarchical Clustering-Based Asset Allocation, The Journal of Portfolio Management Multi-Asset Special Issue 2018, 44 (2) 89-99](https://jpm.pm-research.com/content/44/2/89.abstract)
 * [Raffinot, Thomas, The Hierarchical Equal Risk Contribution Portfolio](https://ssrn.com/abstract=3237540)
 * [Johann Pfitzinger & Nico Katzke, 2019. A constrained hierarchical risk parity algorithm with cluster-based capital allocation. Working Papers 14/2019, Stellenbosch University, Department of Economics](https://ideas.repec.org/p/sza/wpaper/wpapers328.html)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization import PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.hierarchical_clustering_based_risk_parity_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    constraints=PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
        maximum_portfolio_exposure=0.5,
        minimum_portfolio_exposure=0.5,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**across_cluster_allocation_method:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestAcrossClusterAllocationMethod]` — The allocation method to use across clusters
    
</dd>
</dl>

<dl>
<dd>

**clustering_method:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringMethod]` — The hierarchical clustering method to use
    
</dd>
</dl>

<dl>
<dd>

**clustering_ordering:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestClusteringOrdering]` — The order to impose on the hierarchical clustering tree leaves
    
</dd>
</dl>

<dl>
<dd>

**clusters:** `typing.Optional[int]` — The number of clusters to use in the hierarchical clustering tree; if not provided, the number of clusters to use is computed using the gap statistic method, as described in the first reference
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**within_cluster_allocation_method:** `typing.Optional[PostPortfolioOptimizationHierarchicalRiskParityClusteringBasedRequestWithinClusterAllocationMethod]` — The allocation method to use within clusters
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">inverse_variance_weighted_portfolio</a>(...) -> PostPortfolioOptimizationInverseVarianceWeightedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the inverse variance-weighted portfolio.

References
 * [Raul Leote de Carvalho and al., Demystifying Equity Risk-Based Strategies: A Simple Alpha Plus Beta Description](https://doi.org/10.3905/jpm.2012.38.3.056)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.inverse_variance_weighted_portfolio(
    assets=2,
    assets_variances=[
        1,
        0.5
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_variances:** `typing.List[float]` — assetsVariances[i] is the variance of the asset i
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">inverse_volatility_weighted_portfolio</a>(...) -> PostPortfolioOptimizationInverseVolatilityWeightedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the inverse volatility-weighted portfolio.

References
 * [Raul Leote de Carvalho and al., Demystifying Equity Risk-Based Strategies: A Simple Alpha Plus Beta Description](https://doi.org/10.3905/jpm.2012.38.3.056)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.inverse_volatility_weighted_portfolio(
    assets=2,
    assets_volatilities=[
        0.05,
        0.1
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_volatilities:** `typing.List[float]` — assetsVolatilities[i] is the volatility of the asset i
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">market_capitalization_weighted_portfolio</a>(...) -> PostPortfolioOptimizationMarketCapitalizationWeightedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the market capitalization-weighted portfolio.

References
 * [Wikipedia, Capitalization-weighted Index](https://en.wikipedia.org/wiki/Capitalization-weighted_index)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.market_capitalization_weighted_portfolio(
    assets=2,
    assets_market_capitalizations=[
        1,
        2
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_market_capitalizations:** `typing.List[float]` — assetsMarketCapitalizations[i] is the market capitalization of the asset i
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">maximum_decorrelation_portfolio</a>(...) -> PostPortfolioOptimizationMaximumDecorrelationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the maximum decorrelation portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [F. Goltz, S. Sivasubramanian, Scientific Beta Maximum Decorrelation Indices](http://www.scientificbeta.com/download/file/scientific-beta-max-decorrelation-indices)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.maximum_decorrelation_portfolio(
    assets=3,
    assets_correlation_matrix=[
        [
            1,
            0.9,
            0.85
        ],
        [
            0.9,
            1,
            0.7
        ],
        [
            0.85,
            0.7,
            1
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.Optional[typing.List[float]]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumDecorrelationRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">maximum_ulcer_performance_index_portfolio</a>(...) -> PostPortfolioOptimizationMaximumUlcerPerformanceIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the maximum Ulcer Performance Index portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

Notes:  
* This endpoint will return an error if the maximum Ulcer Performance Index portfolio has a negative Ulcer Performance Index

References
 * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
 * [A. Chekhlov, S. Uryasev, M. Zabarankin, Portfolio Optimization with Drawdown Constraints, Supply Chain and Finance, p 209-228](https://doi.org/10.1142/9789812562586_0013)
 * [A. Chekhlov, S. Uryasev, M. Zabarankin, Drawdown Measure in Portfolio Optimization, International Journal of Theoretical and Applied FinanceVol. 08, No. 01, pp. 13-58 (2005)](https://www.worldscientific.com/doi/10.1142/S0219024905002767)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization import PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.maximum_ulcer_performance_index_portfolio(
    assets=[
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem(
            asset_prices=[
                100,
                95,
                110
            ],
        ),
        PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem(
            asset_prices=[
                100,
                105,
                100
            ],
        )
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumUlcerPerformanceIndexRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">minimum_correlation_portfolio</a>(...) -> PostPortfolioOptimizationMinimumCorrelationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the (heuristic) minimum correlation portfolio, which is a portfolio built using the Minimum Correlation Algorithm discovered by [David Varadi](https://cssanalytics.wordpress.com/).

References
 * [CSSA, Minimum Correlation Algorithm Paper Release](https://cssanalytics.wordpress.com/2012/09/21/minimum-correlation-algorithm-paper-release/)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.minimum_correlation_portfolio(
    assets=3,
    assets_correlation_matrix=[
        [
            1,
            0.9,
            0.85
        ],
        [
            0.9,
            1,
            0.7
        ],
        [
            0.85,
            0.7,
            1
        ]
    ],
    assets_volatilities=[
        0.14,
        0.18,
        0.22
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` 
    
</dd>
</dl>

<dl>
<dd>

**assets_correlation_matrix:** `typing.List[typing.List[float]]` — assetsCorrelationMatrix[i][j] is the correlation between the asset i and the asset j; required if assetsReturns is not provided
    
</dd>
</dl>

<dl>
<dd>

**assets_volatilities:** `typing.List[float]` — assetsVariances[i] is the volatility of the asset i; required if assetsCorrelationMatrix is provided and assetsVariances is not provided
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">minimum_ulcer_index_portfolio</a>(...) -> PostPortfolioOptimizationMinimumUlcerIndexResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the minimum Ulcer Index portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [Peter G. Martin, Ulcer Index, An Alternative Approach to the Measurement of Investment Risk & Risk-Adjusted Performance](http://www.tangotools.com/ui/ui.htm)
 * [A. Chekhlov, S. Uryasev, M. Zabarankin, Portfolio Optimization with Drawdown Constraints, Supply Chain and Finance, p 209-228](https://doi.org/10.1142/9789812562586_0013)
 * [A. Chekhlov, S. Uryasev, M. Zabarankin, Drawdown Measure in Portfolio Optimization, International Journal of Theoretical and Applied FinanceVol. 08, No. 01, pp. 13-58 (2005)](https://www.worldscientific.com/doi/10.1142/S0219024905002767)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization import PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.minimum_ulcer_index_portfolio(
    assets=[
        PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem(
            asset_prices=[
                100,
                95,
                110
            ],
        ),
        PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem(
            asset_prices=[
                100,
                105,
                100
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostPortfolioOptimizationMinimumUlcerIndexRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMinimumUlcerIndexRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization.<a href="src/fern/portfolio_optimization/client.py">most_diversified_portfolio</a>(...) -> PostPortfolioOptimizationMostDiversifiedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the most diversified portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [Yves Choueifaty and Yves Coignard, Toward Maximum Diversification, The Journal of Portfolio Management Fall 2008, 35 (1) 40-51](https://doi.org/10.3905/JPM.2008.35.1.40)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization.most_diversified_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.04,
            0.01
        ],
        [
            0.01,
            0.01
        ]
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMostDiversifiedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PortfolioOptimizationMeanVariance
<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">maximum_return_portfolio</a>(...) -> PostPortfolioOptimizationMaximumReturnResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the maximum return portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMaximumReturnRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.maximum_return_portfolio(
    assets=2,
    assets_returns=[
        0.02,
        0.01
    ],
    constraints=PostPortfolioOptimizationMaximumReturnRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.Optional[typing.List[typing.List[float]]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumReturnRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">diversified_maximum_return_portfolio</a>(...) -> PostPortfolioOptimizationMaximumReturnDiversifiedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the diversified maximum return portfolio, as defined in the first reference, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

References
 * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
 * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.diversified_maximum_return_portfolio(
    assets=2,
    assets_returns=[
        0.02,
        0.01
    ],
    constraints=PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.Optional[typing.List[typing.List[float]]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumReturnDiversifiedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">subset_resampling_based_maximum_return_portfolio</a>(...) -> PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the subset resampling-based maximum return portfolio, following the methodology described in the first and the second references, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
 * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.subset_resampling_based_maximum_return_portfolio(
    assets=3,
    assets_returns=[
        0.01,
        0.02,
        0.03
    ],
    subset_portfolios_enumeration_method=PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod.COMPLETE,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.Optional[typing.List[typing.List[float]]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios:** `typing.Optional[int]` — The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_aggregation_method:** `typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]` — The method to aggregate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_enumeration_method:** `typing.Optional[PostPortfolioOptimizationMaximumReturnSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]` — The method to enumerate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_size:** `typing.Optional[int]` — The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">maximum_sharpe_ratio_portfolio</a>(...) -> PostPortfolioOptimizationMaximumSharpeRatioResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the maximum Sharpe ratio portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.maximum_sharpe_ratio_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.05,
            0.02
        ],
        [
            0.02,
            0.07
        ]
    ],
    assets_returns=[
        0.05,
        0.1
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">diversified_maximum_sharpe_ratio_portfolio</a>(...) -> PostPortfolioOptimizationMaximumSharpeRatioDiversifiedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the diversified maximum Sharpe ratio portfolio, as defined in the first reference, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

References
 * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
 * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.diversified_maximum_sharpe_ratio_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.05,
            0.02
        ],
        [
            0.02,
            0.07
        ]
    ],
    assets_returns=[
        0.05,
        0.1
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioDiversifiedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">subset_resampling_based_maximum_sharpe_ratio_portfolio</a>(...) -> PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the susbet resampling-based maximum Sharpe ratio portfolio, following the methodology described in the first and the second references, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
 * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.subset_resampling_based_maximum_sharpe_ratio_portfolio(
    assets=3,
    assets_covariance_matrix=[
        [
            0.05,
            0.02,
            0
        ],
        [
            0.02,
            0.07,
            0.5
        ],
        [
            0,
            0.5,
            0.1
        ]
    ],
    assets_returns=[
        0.05,
        0.1,
        0.025
    ],
    risk_free_rate=0,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**risk_free_rate:** `float` — The risk free rate
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios:** `typing.Optional[int]` — The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_aggregation_method:** `typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]` — The method to aggregate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_enumeration_method:** `typing.Optional[PostPortfolioOptimizationMaximumSharpeRatioSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]` — The method to enumerate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_size:** `typing.Optional[int]` — The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">mean_variance_efficient_portfolio</a>(...) -> PostPortfolioOptimizationMeanVarianceEfficientResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of a mean-variance efficient portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

> A mean-variance efficient portfolio is a portfolio belonging to [the mean-variance efficient frontier](#post-/portfolio/analysis/mean-variance/efficient-frontier).

References
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.mean_variance_efficient_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            1,
            0.3
        ],
        [
            0.3,
            1
        ]
    ],
    assets_returns=[
        0.1,
        0.2
    ],
    constraints=PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints(
        portfolio_return=0.15,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `PostPortfolioOptimizationMeanVarianceEfficientRequestConstraints` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">diversified_mean_variance_efficient_portfolio</a>(...) -> PostPortfolioOptimizationMeanVarianceEfficientDiversifiedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of a diversified mean-variance efficient portfolio, as defined in the first reference, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

> A diversified mean-variance efficient portfolio does NOT belong to [the mean-variance efficient frontier](#post-/portfolio/analysis/mean-variance/efficient-frontier), but is close to this frontier.

References
 * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
 * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.diversified_mean_variance_efficient_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            1,
            0.3
        ],
        [
            0.3,
            1
        ]
    ],
    assets_returns=[
        0.1,
        0.2
    ],
    constraints=PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints(
        delta_return=0.05,
        delta_volatility=0.05,
        portfolio_return=0.175,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `PostPortfolioOptimizationMeanVarianceEfficientDiversifiedRequestConstraints` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">subset_resampling_based_mean_variance_efficient_portfolio</a>(...) -> PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of a subset resampling-based  mean-variance efficient portfolio, following the methodology described in the first and the second references, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
 * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.subset_resampling_based_mean_variance_efficient_portfolio(
    assets=3,
    assets_covariance_matrix=[
        [
            1,
            0,
            0
        ],
        [
            0,
            1,
            0
        ],
        [
            0,
            0,
            1
        ]
    ],
    assets_returns=[
        0.1,
        0.2,
        0.3
    ],
    constraints=PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints(
        risk_tolerance=2,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.List[float]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestConstraints` 
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios:** `typing.Optional[int]` — The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_aggregation_method:** `typing.Optional[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]` — The method to aggregate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_enumeration_method:** `typing.Optional[PostPortfolioOptimizationMeanVarianceEfficientSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]` — The method to enumerate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_size:** `typing.Optional[int]` — The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">minimum_variance_portfolio</a>(...) -> PostPortfolioOptimizationMinimumVarianceResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the minimum variance portfolio, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMinimumVarianceRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.minimum_variance_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    constraints=PostPortfolioOptimizationMinimumVarianceRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
        maximum_portfolio_exposure=0.5,
        minimum_portfolio_exposure=0.5,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.Optional[typing.List[float]]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMinimumVarianceRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">diversified_minimum_variance_portfolio</a>(...) -> PostPortfolioOptimizationMinimumVarianceDiversifiedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the diversified minimum variance portfolio, as defined in the first reference, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

The diversification measure used in the optimization procedure is the [Herfindahl-Hirschman Index](https://en.wikipedia.org/wiki/Herfindahl%E2%80%93Hirschman_index) of the assets weights.

References
 * [Alejandro Corvalan, 2005. Well Diversified Efficient Portfolios, Working Papers Central Bank of Chile 336, Central Bank of Chile](https://ideas.repec.org/p/chb/bcchwp/336.html)
 * [Bouchaud, Jean-Philippe and Potters, Marc and Aguilar, Jean-Pierre, Missing Information and Asset Allocation, arXiv, 1997](https://arxiv.org/abs/cond-mat/9707042)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.diversified_minimum_variance_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    constraints=PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
        maximum_portfolio_exposure=0.5,
        minimum_portfolio_exposure=0.5,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.Optional[typing.List[float]]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMinimumVarianceDiversifiedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_optimization_mean_variance.<a href="src/fern/portfolio_optimization_mean_variance/client.py">subset_resampling_based_minimum_variance_portfolio</a>(...) -> PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Compute the asset weights of the subset resampling-based minimum variance portfolio, following the methodology described in the first and the second references, optionally subject to:  
* Minimum and maximum weights constraints
* Maximum group weights constraints
* Minimum and maximum portfolio exposure constraints

References
 * [CSSA, Random Subspace Optimization (RSO)](https://cssanalytics.wordpress.com/2013/10/06/random-subspace-optimization-rso/)
 * [Subset Optimization for Asset Allocation,Benjamin J. Gillen](https://www.bengillen.com/uploads/1/2/3/8/123891022/subsets.pdf)
 * Harry M. Markowitz, Portfolio Selection, Efficient Diversification of Investments, Second edition, Blackwell Publishers Inc.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_optimization_mean_variance import PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_optimization_mean_variance.subset_resampling_based_minimum_variance_portfolio(
    assets=2,
    assets_covariance_matrix=[
        [
            0.0025,
            0.0005
        ],
        [
            0.0005,
            0.01
        ]
    ],
    constraints=PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints(
        maximum_assets_weights=[
            0.4,
            1
        ],
        maximum_portfolio_exposure=0.5,
        minimum_portfolio_exposure=0.5,
    ),
    subset_portfolios=1,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `int` — The number of assets
    
</dd>
</dl>

<dl>
<dd>

**assets_covariance_matrix:** `typing.List[typing.List[float]]` — assetsCovarianceMatrix[i][j] is the covariance between the asset i and the asset j
    
</dd>
</dl>

<dl>
<dd>

**assets_returns:** `typing.Optional[typing.List[float]]` — assetsReturns[i] is the arithmetic return of asset i
    
</dd>
</dl>

<dl>
<dd>

**constraints:** `typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestConstraints]` 
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios:** `typing.Optional[int]` — The number of subset portfolios to compute; only applicable if the enumeration method for the subset portfolios is random sampling
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_aggregation_method:** `typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosAggregationMethod]` — The method to aggregate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_portfolios_enumeration_method:** `typing.Optional[PostPortfolioOptimizationMinimumVarianceSubsetResamplingBasedRequestSubsetPortfoliosEnumerationMethod]` — The method to enumerate the subset portfolios
    
</dd>
</dl>

<dl>
<dd>

**subset_size:** `typing.Optional[int]` — The number of assets to include in each subset portfolio; defaults to a value of order the square root of the total number of assets
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PortfolioSimulation
<details><summary><code>client.portfolio_simulation.<a href="src/fern/portfolio_simulation/client.py">drift_weight_portfolio_rebalancing</a>(...) -> PostPortfolioSimulationRebalancingDriftWeightResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being never rebalanced (a.k.a. buy and hold).

References
* [Hillion, Pierre, The Ex-Ante Rebalancing Premium (March 11, 2016). INSEAD Working Paper No. 2016/15/FIN](https://ssrn.com/abstract=2746471)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_simulation import PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem, PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_simulation.drift_weight_portfolio_rebalancing(
    assets=[
        PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
            asset_prices=[
                100,
                105,
                110
            ],
        ),
        PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
            asset_prices=[
                15,
                12.5,
                11.25
            ],
        ),
        PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem(
            asset_prices=[
                0.5,
                0.51,
                0.49
            ],
        )
    ],
    portfolios=[
        PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
            assets_weights=[
                1,
                0,
                0
            ],
        ),
        PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
            assets_weights=[
                0,
                1,
                0
            ],
        ),
        PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem(
            assets_weights=[
                0,
                0,
                1
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostPortfolioSimulationRebalancingDriftWeightRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioSimulationRebalancingDriftWeightRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_simulation.<a href="src/fern/portfolio_simulation/client.py">fixed_weight_portfolio_rebalancing</a>(...) -> PostPortfolioSimulationRebalancingFixedWeightResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being rebalanced toward fixed weights at the beginning of each time period.

References
* [Hillion, Pierre, The Ex-Ante Rebalancing Premium (March 11, 2016). INSEAD Working Paper No. 2016/15/FIN](https://ssrn.com/abstract=2746471)        
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_simulation import PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem, PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_simulation.fixed_weight_portfolio_rebalancing(
    assets=[
        PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
            asset_prices=[
                100,
                105,
                110
            ],
        ),
        PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
            asset_prices=[
                15,
                12.5,
                11.25
            ],
        ),
        PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem(
            asset_prices=[
                0.5,
                0.51,
                0.49
            ],
        )
    ],
    portfolios=[
        PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
            assets_weights=[
                0.5,
                0.5,
                0
            ],
        ),
        PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
            assets_weights=[
                0,
                0.5,
                0.5
            ],
        ),
        PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem(
            assets_weights=[
                0.5,
                0,
                0.5
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostPortfolioSimulationRebalancingFixedWeightRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.List[PostPortfolioSimulationRebalancingFixedWeightRequestPortfoliosItem]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.portfolio_simulation.<a href="src/fern/portfolio_simulation/client.py">random_weight_portfolio_rebalancing</a>(...) -> PostPortfolioSimulationRebalancingRandomWeightResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Simulate the evolution of one or several portfolio(s) over one or several time period(s), the portfolio(s) being rebalanced toward random weights at the beginning of each time period.

References
* [R Stein, Not fooled by randomness: Using random portfolios to analyse investment funds, Investment Analysts Journal, 43:79, 1-15, DOI: 10.1080/10293523.2014.11082564](https://www.tandfonline.com/doi/abs/10.1080/10293523.2014.11082564)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from fern import FernApi
from fern.environment import FernApiEnvironment
from fern.portfolio_simulation import PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem

client = FernApi(
    api_key="<value>",
    environment=FernApiEnvironment.DEFAULT,
)

client.portfolio_simulation.random_weight_portfolio_rebalancing(
    assets=[
        PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
            asset_prices=[
                100,
                105,
                110
            ],
        ),
        PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
            asset_prices=[
                15,
                12.5,
                11.25
            ],
        ),
        PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem(
            asset_prices=[
                0.5,
                0.51,
                0.49
            ],
        )
    ],
    portfolios=2,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**assets:** `typing.List[PostPortfolioSimulationRebalancingRandomWeightRequestAssetsItem]` 
    
</dd>
</dl>

<dl>
<dd>

**portfolios:** `typing.Optional[int]` — The number of portfolios to simulate
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

