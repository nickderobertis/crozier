



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_volatility_request import PostAssetsVolatilityRequest
    from .post_assets_volatility_request_assets import PostAssetsVolatilityRequestAssets
    from .post_assets_volatility_request_assets_assets_item import PostAssetsVolatilityRequestAssetsAssetsItem
    from .post_assets_volatility_request_assets_covariance_matrix import (
        PostAssetsVolatilityRequestAssetsCovarianceMatrix,
    )
    from .post_assets_volatility_request_zero import PostAssetsVolatilityRequestZero
    from .post_assets_volatility_request_zero_assets_item import PostAssetsVolatilityRequestZeroAssetsItem
    from .post_assets_volatility_response import PostAssetsVolatilityResponse
    from .post_assets_volatility_response_assets_item import PostAssetsVolatilityResponseAssetsItem
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsVolatilityRequest": ".post_assets_volatility_request",
    "PostAssetsVolatilityRequestAssets": ".post_assets_volatility_request_assets",
    "PostAssetsVolatilityRequestAssetsAssetsItem": ".post_assets_volatility_request_assets_assets_item",
    "PostAssetsVolatilityRequestAssetsCovarianceMatrix": ".post_assets_volatility_request_assets_covariance_matrix",
    "PostAssetsVolatilityRequestZero": ".post_assets_volatility_request_zero",
    "PostAssetsVolatilityRequestZeroAssetsItem": ".post_assets_volatility_request_zero_assets_item",
    "PostAssetsVolatilityResponse": ".post_assets_volatility_response",
    "PostAssetsVolatilityResponseAssetsItem": ".post_assets_volatility_response_assets_item",
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
    "PostAssetsVolatilityRequest",
    "PostAssetsVolatilityRequestAssets",
    "PostAssetsVolatilityRequestAssetsAssetsItem",
    "PostAssetsVolatilityRequestAssetsCovarianceMatrix",
    "PostAssetsVolatilityRequestZero",
    "PostAssetsVolatilityRequestZeroAssetsItem",
    "PostAssetsVolatilityResponse",
    "PostAssetsVolatilityResponseAssetsItem",
]
