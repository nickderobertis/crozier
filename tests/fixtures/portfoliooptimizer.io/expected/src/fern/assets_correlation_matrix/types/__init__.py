



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_correlation_matrix_bounds_response import PostAssetsCorrelationMatrixBoundsResponse
    from .post_assets_correlation_matrix_denoised_request_denoising_method import (
        PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod,
    )
    from .post_assets_correlation_matrix_denoised_response import PostAssetsCorrelationMatrixDenoisedResponse
    from .post_assets_correlation_matrix_distance_request_distance_metric import (
        PostAssetsCorrelationMatrixDistanceRequestDistanceMetric,
    )
    from .post_assets_correlation_matrix_distance_response import PostAssetsCorrelationMatrixDistanceResponse
    from .post_assets_correlation_matrix_effective_rank_response import PostAssetsCorrelationMatrixEffectiveRankResponse
    from .post_assets_correlation_matrix_informativeness_request_distance_metric import (
        PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric,
    )
    from .post_assets_correlation_matrix_informativeness_response import (
        PostAssetsCorrelationMatrixInformativenessResponse,
    )
    from .post_assets_correlation_matrix_nearest_response import PostAssetsCorrelationMatrixNearestResponse
    from .post_assets_correlation_matrix_random_response import PostAssetsCorrelationMatrixRandomResponse
    from .post_assets_correlation_matrix_request import PostAssetsCorrelationMatrixRequest
    from .post_assets_correlation_matrix_request_assets_covariance_matrix import (
        PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix,
    )
    from .post_assets_correlation_matrix_request_zero import PostAssetsCorrelationMatrixRequestZero
    from .post_assets_correlation_matrix_request_zero_assets_item import (
        PostAssetsCorrelationMatrixRequestZeroAssetsItem,
    )
    from .post_assets_correlation_matrix_response import PostAssetsCorrelationMatrixResponse
    from .post_assets_correlation_matrix_shrinkage_request import PostAssetsCorrelationMatrixShrinkageRequest
    from .post_assets_correlation_matrix_shrinkage_request_target_correlation_matrix import (
        PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix,
    )
    from .post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix import (
        PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrix,
    )
    from .post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix_target_equicorrelation_matrix import (
        PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix,
    )
    from .post_assets_correlation_matrix_shrinkage_response import PostAssetsCorrelationMatrixShrinkageResponse
    from .post_assets_correlation_matrix_theory_implied_request_assets_item import (
        PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem,
    )
    from .post_assets_correlation_matrix_theory_implied_request_assets_item_asset_hierarchical_classification_item import (
        PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem,
    )
    from .post_assets_correlation_matrix_theory_implied_request_clustering_method import (
        PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod,
    )
    from .post_assets_correlation_matrix_theory_implied_response import PostAssetsCorrelationMatrixTheoryImpliedResponse
    from .post_assets_correlation_matrix_validation_response import PostAssetsCorrelationMatrixValidationResponse
    from .post_assets_correlation_matrix_validation_response_message import (
        PostAssetsCorrelationMatrixValidationResponseMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsCorrelationMatrixBoundsResponse": ".post_assets_correlation_matrix_bounds_response",
    "PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod": ".post_assets_correlation_matrix_denoised_request_denoising_method",
    "PostAssetsCorrelationMatrixDenoisedResponse": ".post_assets_correlation_matrix_denoised_response",
    "PostAssetsCorrelationMatrixDistanceRequestDistanceMetric": ".post_assets_correlation_matrix_distance_request_distance_metric",
    "PostAssetsCorrelationMatrixDistanceResponse": ".post_assets_correlation_matrix_distance_response",
    "PostAssetsCorrelationMatrixEffectiveRankResponse": ".post_assets_correlation_matrix_effective_rank_response",
    "PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric": ".post_assets_correlation_matrix_informativeness_request_distance_metric",
    "PostAssetsCorrelationMatrixInformativenessResponse": ".post_assets_correlation_matrix_informativeness_response",
    "PostAssetsCorrelationMatrixNearestResponse": ".post_assets_correlation_matrix_nearest_response",
    "PostAssetsCorrelationMatrixRandomResponse": ".post_assets_correlation_matrix_random_response",
    "PostAssetsCorrelationMatrixRequest": ".post_assets_correlation_matrix_request",
    "PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix": ".post_assets_correlation_matrix_request_assets_covariance_matrix",
    "PostAssetsCorrelationMatrixRequestZero": ".post_assets_correlation_matrix_request_zero",
    "PostAssetsCorrelationMatrixRequestZeroAssetsItem": ".post_assets_correlation_matrix_request_zero_assets_item",
    "PostAssetsCorrelationMatrixResponse": ".post_assets_correlation_matrix_response",
    "PostAssetsCorrelationMatrixShrinkageRequest": ".post_assets_correlation_matrix_shrinkage_request",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix": ".post_assets_correlation_matrix_shrinkage_request_target_correlation_matrix",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrix": ".post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix": ".post_assets_correlation_matrix_shrinkage_request_target_equicorrelation_matrix_target_equicorrelation_matrix",
    "PostAssetsCorrelationMatrixShrinkageResponse": ".post_assets_correlation_matrix_shrinkage_response",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem": ".post_assets_correlation_matrix_theory_implied_request_assets_item",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem": ".post_assets_correlation_matrix_theory_implied_request_assets_item_asset_hierarchical_classification_item",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod": ".post_assets_correlation_matrix_theory_implied_request_clustering_method",
    "PostAssetsCorrelationMatrixTheoryImpliedResponse": ".post_assets_correlation_matrix_theory_implied_response",
    "PostAssetsCorrelationMatrixValidationResponse": ".post_assets_correlation_matrix_validation_response",
    "PostAssetsCorrelationMatrixValidationResponseMessage": ".post_assets_correlation_matrix_validation_response_message",
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
    "PostAssetsCorrelationMatrixBoundsResponse",
    "PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod",
    "PostAssetsCorrelationMatrixDenoisedResponse",
    "PostAssetsCorrelationMatrixDistanceRequestDistanceMetric",
    "PostAssetsCorrelationMatrixDistanceResponse",
    "PostAssetsCorrelationMatrixEffectiveRankResponse",
    "PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric",
    "PostAssetsCorrelationMatrixInformativenessResponse",
    "PostAssetsCorrelationMatrixNearestResponse",
    "PostAssetsCorrelationMatrixRandomResponse",
    "PostAssetsCorrelationMatrixRequest",
    "PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix",
    "PostAssetsCorrelationMatrixRequestZero",
    "PostAssetsCorrelationMatrixRequestZeroAssetsItem",
    "PostAssetsCorrelationMatrixResponse",
    "PostAssetsCorrelationMatrixShrinkageRequest",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrix",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix",
    "PostAssetsCorrelationMatrixShrinkageResponse",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod",
    "PostAssetsCorrelationMatrixTheoryImpliedResponse",
    "PostAssetsCorrelationMatrixValidationResponse",
    "PostAssetsCorrelationMatrixValidationResponseMessage",
]
