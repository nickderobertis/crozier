



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_variance_request import PostAssetsVarianceRequest
    from .post_assets_variance_request_assets import PostAssetsVarianceRequestAssets
    from .post_assets_variance_request_assets_assets_item import PostAssetsVarianceRequestAssetsAssetsItem
    from .post_assets_variance_request_assets_covariance_matrix import PostAssetsVarianceRequestAssetsCovarianceMatrix
    from .post_assets_variance_request_zero import PostAssetsVarianceRequestZero
    from .post_assets_variance_request_zero_assets_item import PostAssetsVarianceRequestZeroAssetsItem
    from .post_assets_variance_response import PostAssetsVarianceResponse
    from .post_assets_variance_response_assets_item import PostAssetsVarianceResponseAssetsItem
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsVarianceRequest": ".post_assets_variance_request",
    "PostAssetsVarianceRequestAssets": ".post_assets_variance_request_assets",
    "PostAssetsVarianceRequestAssetsAssetsItem": ".post_assets_variance_request_assets_assets_item",
    "PostAssetsVarianceRequestAssetsCovarianceMatrix": ".post_assets_variance_request_assets_covariance_matrix",
    "PostAssetsVarianceRequestZero": ".post_assets_variance_request_zero",
    "PostAssetsVarianceRequestZeroAssetsItem": ".post_assets_variance_request_zero_assets_item",
    "PostAssetsVarianceResponse": ".post_assets_variance_response",
    "PostAssetsVarianceResponseAssetsItem": ".post_assets_variance_response_assets_item",
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
    "PostAssetsVarianceRequest",
    "PostAssetsVarianceRequestAssets",
    "PostAssetsVarianceRequestAssetsAssetsItem",
    "PostAssetsVarianceRequestAssetsCovarianceMatrix",
    "PostAssetsVarianceRequestZero",
    "PostAssetsVarianceRequestZeroAssetsItem",
    "PostAssetsVarianceResponse",
    "PostAssetsVarianceResponseAssetsItem",
]
