



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_covariance_matrix_effective_rank_response import PostAssetsCovarianceMatrixEffectiveRankResponse
    from .post_assets_covariance_matrix_exponentially_weighted_request_assets_item import (
        PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem,
    )
    from .post_assets_covariance_matrix_exponentially_weighted_response import (
        PostAssetsCovarianceMatrixExponentiallyWeightedResponse,
    )
    from .post_assets_covariance_matrix_request import PostAssetsCovarianceMatrixRequest
    from .post_assets_covariance_matrix_request_assets import PostAssetsCovarianceMatrixRequestAssets
    from .post_assets_covariance_matrix_request_assets_variances import PostAssetsCovarianceMatrixRequestAssetsVariances
    from .post_assets_covariance_matrix_request_zero import PostAssetsCovarianceMatrixRequestZero
    from .post_assets_covariance_matrix_request_zero_assets_item import PostAssetsCovarianceMatrixRequestZeroAssetsItem
    from .post_assets_covariance_matrix_response import PostAssetsCovarianceMatrixResponse
    from .post_assets_covariance_matrix_validation_response import PostAssetsCovarianceMatrixValidationResponse
    from .post_assets_covariance_matrix_validation_response_message import (
        PostAssetsCovarianceMatrixValidationResponseMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsCovarianceMatrixEffectiveRankResponse": ".post_assets_covariance_matrix_effective_rank_response",
    "PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem": ".post_assets_covariance_matrix_exponentially_weighted_request_assets_item",
    "PostAssetsCovarianceMatrixExponentiallyWeightedResponse": ".post_assets_covariance_matrix_exponentially_weighted_response",
    "PostAssetsCovarianceMatrixRequest": ".post_assets_covariance_matrix_request",
    "PostAssetsCovarianceMatrixRequestAssets": ".post_assets_covariance_matrix_request_assets",
    "PostAssetsCovarianceMatrixRequestAssetsVariances": ".post_assets_covariance_matrix_request_assets_variances",
    "PostAssetsCovarianceMatrixRequestZero": ".post_assets_covariance_matrix_request_zero",
    "PostAssetsCovarianceMatrixRequestZeroAssetsItem": ".post_assets_covariance_matrix_request_zero_assets_item",
    "PostAssetsCovarianceMatrixResponse": ".post_assets_covariance_matrix_response",
    "PostAssetsCovarianceMatrixValidationResponse": ".post_assets_covariance_matrix_validation_response",
    "PostAssetsCovarianceMatrixValidationResponseMessage": ".post_assets_covariance_matrix_validation_response_message",
}


def __getattr__(attr_name: str) -> typing.Any:
    module_name = _dynamic_imports.get(attr_name)
    if module_name is None:
        raise AttributeError(f"No {attr_name} found in _dynamic_imports for module name -> {__name__}")
    try:
        module = import_module(module_name, __package__)
        if module_name == f".{attr_name}":
            return module
        else:
            return getattr(module, attr_name)
    except ImportError as e:
        raise ImportError(f"Failed to import {attr_name} from {module_name}: {e}") from e
    except AttributeError as e:
        raise AttributeError(f"Failed to get {attr_name} from {module_name}: {e}") from e


def __dir__():
    lazy_attrs = list(_dynamic_imports.keys())
    return sorted(lazy_attrs)


__all__ = [
    "PostAssetsCovarianceMatrixEffectiveRankResponse",
    "PostAssetsCovarianceMatrixExponentiallyWeightedRequestAssetsItem",
    "PostAssetsCovarianceMatrixExponentiallyWeightedResponse",
    "PostAssetsCovarianceMatrixRequest",
    "PostAssetsCovarianceMatrixRequestAssets",
    "PostAssetsCovarianceMatrixRequestAssetsVariances",
    "PostAssetsCovarianceMatrixRequestZero",
    "PostAssetsCovarianceMatrixRequestZeroAssetsItem",
    "PostAssetsCovarianceMatrixResponse",
    "PostAssetsCovarianceMatrixValidationResponse",
    "PostAssetsCovarianceMatrixValidationResponseMessage",
]
