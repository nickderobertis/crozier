



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .types import (
        PostListingsRequestCategoriesItem,
        PostListingsRequestCondition,
        PostListingsRequestConditionUuid,
        PostListingsRequestExclusiveChannel,
        PostListingsRequestLocation,
        PostListingsRequestPreorderInfo,
        PostListingsRequestPreorderInfoLeadTimeUnit,
        PostListingsRequestPrice,
        PostListingsRequestPriceCurrency,
        PostListingsRequestSeller,
        PostListingsRequestShipping,
        PostListingsRequestShippingRatesItem,
        PostListingsRequestShippingRatesItemRate,
        PostListingsRequestShippingRatesItemRateCurrency,
        PostListingsRequestVideosItem,
        PutListingsSlugRequestCategoriesItem,
        PutListingsSlugRequestCondition,
        PutListingsSlugRequestConditionUuid,
        PutListingsSlugRequestExclusiveChannel,
        PutListingsSlugRequestLocation,
        PutListingsSlugRequestPreorderInfo,
        PutListingsSlugRequestPreorderInfoLeadTimeUnit,
        PutListingsSlugRequestPrice,
        PutListingsSlugRequestPriceCurrency,
        PutListingsSlugRequestSeller,
        PutListingsSlugRequestShipping,
        PutListingsSlugRequestShippingRatesItem,
        PutListingsSlugRequestShippingRatesItemRate,
        PutListingsSlugRequestShippingRatesItemRateCurrency,
        PutListingsSlugRequestVideosItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostListingsRequestCategoriesItem": ".types",
    "PostListingsRequestCondition": ".types",
    "PostListingsRequestConditionUuid": ".types",
    "PostListingsRequestExclusiveChannel": ".types",
    "PostListingsRequestLocation": ".types",
    "PostListingsRequestPreorderInfo": ".types",
    "PostListingsRequestPreorderInfoLeadTimeUnit": ".types",
    "PostListingsRequestPrice": ".types",
    "PostListingsRequestPriceCurrency": ".types",
    "PostListingsRequestSeller": ".types",
    "PostListingsRequestShipping": ".types",
    "PostListingsRequestShippingRatesItem": ".types",
    "PostListingsRequestShippingRatesItemRate": ".types",
    "PostListingsRequestShippingRatesItemRateCurrency": ".types",
    "PostListingsRequestVideosItem": ".types",
    "PutListingsSlugRequestCategoriesItem": ".types",
    "PutListingsSlugRequestCondition": ".types",
    "PutListingsSlugRequestConditionUuid": ".types",
    "PutListingsSlugRequestExclusiveChannel": ".types",
    "PutListingsSlugRequestLocation": ".types",
    "PutListingsSlugRequestPreorderInfo": ".types",
    "PutListingsSlugRequestPreorderInfoLeadTimeUnit": ".types",
    "PutListingsSlugRequestPrice": ".types",
    "PutListingsSlugRequestPriceCurrency": ".types",
    "PutListingsSlugRequestSeller": ".types",
    "PutListingsSlugRequestShipping": ".types",
    "PutListingsSlugRequestShippingRatesItem": ".types",
    "PutListingsSlugRequestShippingRatesItemRate": ".types",
    "PutListingsSlugRequestShippingRatesItemRateCurrency": ".types",
    "PutListingsSlugRequestVideosItem": ".types",
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
    "PostListingsRequestCategoriesItem",
    "PostListingsRequestCondition",
    "PostListingsRequestConditionUuid",
    "PostListingsRequestExclusiveChannel",
    "PostListingsRequestLocation",
    "PostListingsRequestPreorderInfo",
    "PostListingsRequestPreorderInfoLeadTimeUnit",
    "PostListingsRequestPrice",
    "PostListingsRequestPriceCurrency",
    "PostListingsRequestSeller",
    "PostListingsRequestShipping",
    "PostListingsRequestShippingRatesItem",
    "PostListingsRequestShippingRatesItemRate",
    "PostListingsRequestShippingRatesItemRateCurrency",
    "PostListingsRequestVideosItem",
    "PutListingsSlugRequestCategoriesItem",
    "PutListingsSlugRequestCondition",
    "PutListingsSlugRequestConditionUuid",
    "PutListingsSlugRequestExclusiveChannel",
    "PutListingsSlugRequestLocation",
    "PutListingsSlugRequestPreorderInfo",
    "PutListingsSlugRequestPreorderInfoLeadTimeUnit",
    "PutListingsSlugRequestPrice",
    "PutListingsSlugRequestPriceCurrency",
    "PutListingsSlugRequestSeller",
    "PutListingsSlugRequestShipping",
    "PutListingsSlugRequestShippingRatesItem",
    "PutListingsSlugRequestShippingRatesItemRate",
    "PutListingsSlugRequestShippingRatesItemRateCurrency",
    "PutListingsSlugRequestVideosItem",
]
