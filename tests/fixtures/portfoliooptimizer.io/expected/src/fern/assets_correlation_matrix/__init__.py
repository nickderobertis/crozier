



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostAssetsCorrelationMatrixBoundsResponse,
        PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod,
        PostAssetsCorrelationMatrixDenoisedResponse,
        PostAssetsCorrelationMatrixDistanceRequestDistanceMetric,
        PostAssetsCorrelationMatrixDistanceResponse,
        PostAssetsCorrelationMatrixEffectiveRankResponse,
        PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric,
        PostAssetsCorrelationMatrixInformativenessResponse,
        PostAssetsCorrelationMatrixNearestResponse,
        PostAssetsCorrelationMatrixRandomResponse,
        PostAssetsCorrelationMatrixRequest,
        PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix,
        PostAssetsCorrelationMatrixRequestZero,
        PostAssetsCorrelationMatrixRequestZeroAssetsItem,
        PostAssetsCorrelationMatrixResponse,
        PostAssetsCorrelationMatrixShrinkageRequest,
        PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix,
        PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrix,
        PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix,
        PostAssetsCorrelationMatrixShrinkageResponse,
        PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem,
        PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem,
        PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod,
        PostAssetsCorrelationMatrixTheoryImpliedResponse,
        PostAssetsCorrelationMatrixValidationResponse,
        PostAssetsCorrelationMatrixValidationResponseMessage,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsCorrelationMatrixBoundsResponse": ".types",
    "PostAssetsCorrelationMatrixDenoisedRequestDenoisingMethod": ".types",
    "PostAssetsCorrelationMatrixDenoisedResponse": ".types",
    "PostAssetsCorrelationMatrixDistanceRequestDistanceMetric": ".types",
    "PostAssetsCorrelationMatrixDistanceResponse": ".types",
    "PostAssetsCorrelationMatrixEffectiveRankResponse": ".types",
    "PostAssetsCorrelationMatrixInformativenessRequestDistanceMetric": ".types",
    "PostAssetsCorrelationMatrixInformativenessResponse": ".types",
    "PostAssetsCorrelationMatrixNearestResponse": ".types",
    "PostAssetsCorrelationMatrixRandomResponse": ".types",
    "PostAssetsCorrelationMatrixRequest": ".types",
    "PostAssetsCorrelationMatrixRequestAssetsCovarianceMatrix": ".types",
    "PostAssetsCorrelationMatrixRequestZero": ".types",
    "PostAssetsCorrelationMatrixRequestZeroAssetsItem": ".types",
    "PostAssetsCorrelationMatrixResponse": ".types",
    "PostAssetsCorrelationMatrixShrinkageRequest": ".types",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetCorrelationMatrix": ".types",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrix": ".types",
    "PostAssetsCorrelationMatrixShrinkageRequestTargetEquicorrelationMatrixTargetEquicorrelationMatrix": ".types",
    "PostAssetsCorrelationMatrixShrinkageResponse": ".types",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItem": ".types",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestAssetsItemAssetHierarchicalClassificationItem": ".types",
    "PostAssetsCorrelationMatrixTheoryImpliedRequestClusteringMethod": ".types",
    "PostAssetsCorrelationMatrixTheoryImpliedResponse": ".types",
    "PostAssetsCorrelationMatrixValidationResponse": ".types",
    "PostAssetsCorrelationMatrixValidationResponseMessage": ".types",
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
