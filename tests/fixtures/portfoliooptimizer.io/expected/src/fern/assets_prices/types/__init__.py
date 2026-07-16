



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_assets_prices_adjusted_forward_request_assets_item import (
        PostAssetsPricesAdjustedForwardRequestAssetsItem,
    )
    from .post_assets_prices_adjusted_forward_request_assets_item_asset_dividends_item import (
        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetDividendsItem,
    )
    from .post_assets_prices_adjusted_forward_request_assets_item_asset_prices_item import (
        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem,
    )
    from .post_assets_prices_adjusted_forward_request_assets_item_asset_splits_item import (
        PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem,
    )
    from .post_assets_prices_adjusted_forward_response import PostAssetsPricesAdjustedForwardResponse
    from .post_assets_prices_adjusted_forward_response_assets_item import (
        PostAssetsPricesAdjustedForwardResponseAssetsItem,
    )
    from .post_assets_prices_adjusted_forward_response_assets_item_asset_adjusted_prices_item import (
        PostAssetsPricesAdjustedForwardResponseAssetsItemAssetAdjustedPricesItem,
    )
    from .post_assets_prices_adjusted_request_assets_item import PostAssetsPricesAdjustedRequestAssetsItem
    from .post_assets_prices_adjusted_request_assets_item_asset_dividends_item import (
        PostAssetsPricesAdjustedRequestAssetsItemAssetDividendsItem,
    )
    from .post_assets_prices_adjusted_request_assets_item_asset_prices_item import (
        PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem,
    )
    from .post_assets_prices_adjusted_request_assets_item_asset_splits_item import (
        PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem,
    )
    from .post_assets_prices_adjusted_response import PostAssetsPricesAdjustedResponse
    from .post_assets_prices_adjusted_response_assets_item import PostAssetsPricesAdjustedResponseAssetsItem
    from .post_assets_prices_adjusted_response_assets_item_asset_adjusted_prices_item import (
        PostAssetsPricesAdjustedResponseAssetsItemAssetAdjustedPricesItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostAssetsPricesAdjustedForwardRequestAssetsItem": ".post_assets_prices_adjusted_forward_request_assets_item",
    "PostAssetsPricesAdjustedForwardRequestAssetsItemAssetDividendsItem": ".post_assets_prices_adjusted_forward_request_assets_item_asset_dividends_item",
    "PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem": ".post_assets_prices_adjusted_forward_request_assets_item_asset_prices_item",
    "PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem": ".post_assets_prices_adjusted_forward_request_assets_item_asset_splits_item",
    "PostAssetsPricesAdjustedForwardResponse": ".post_assets_prices_adjusted_forward_response",
    "PostAssetsPricesAdjustedForwardResponseAssetsItem": ".post_assets_prices_adjusted_forward_response_assets_item",
    "PostAssetsPricesAdjustedForwardResponseAssetsItemAssetAdjustedPricesItem": ".post_assets_prices_adjusted_forward_response_assets_item_asset_adjusted_prices_item",
    "PostAssetsPricesAdjustedRequestAssetsItem": ".post_assets_prices_adjusted_request_assets_item",
    "PostAssetsPricesAdjustedRequestAssetsItemAssetDividendsItem": ".post_assets_prices_adjusted_request_assets_item_asset_dividends_item",
    "PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem": ".post_assets_prices_adjusted_request_assets_item_asset_prices_item",
    "PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem": ".post_assets_prices_adjusted_request_assets_item_asset_splits_item",
    "PostAssetsPricesAdjustedResponse": ".post_assets_prices_adjusted_response",
    "PostAssetsPricesAdjustedResponseAssetsItem": ".post_assets_prices_adjusted_response_assets_item",
    "PostAssetsPricesAdjustedResponseAssetsItemAssetAdjustedPricesItem": ".post_assets_prices_adjusted_response_assets_item_asset_adjusted_prices_item",
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
    "PostAssetsPricesAdjustedForwardRequestAssetsItem",
    "PostAssetsPricesAdjustedForwardRequestAssetsItemAssetDividendsItem",
    "PostAssetsPricesAdjustedForwardRequestAssetsItemAssetPricesItem",
    "PostAssetsPricesAdjustedForwardRequestAssetsItemAssetSplitsItem",
    "PostAssetsPricesAdjustedForwardResponse",
    "PostAssetsPricesAdjustedForwardResponseAssetsItem",
    "PostAssetsPricesAdjustedForwardResponseAssetsItemAssetAdjustedPricesItem",
    "PostAssetsPricesAdjustedRequestAssetsItem",
    "PostAssetsPricesAdjustedRequestAssetsItemAssetDividendsItem",
    "PostAssetsPricesAdjustedRequestAssetsItemAssetPricesItem",
    "PostAssetsPricesAdjustedRequestAssetsItemAssetSplitsItem",
    "PostAssetsPricesAdjustedResponse",
    "PostAssetsPricesAdjustedResponseAssetsItem",
    "PostAssetsPricesAdjustedResponseAssetsItemAssetAdjustedPricesItem",
]
