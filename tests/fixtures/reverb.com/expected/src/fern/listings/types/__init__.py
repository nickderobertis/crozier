



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_listings_request_categories_item import PostListingsRequestCategoriesItem
    from .post_listings_request_condition import PostListingsRequestCondition
    from .post_listings_request_condition_uuid import PostListingsRequestConditionUuid
    from .post_listings_request_exclusive_channel import PostListingsRequestExclusiveChannel
    from .post_listings_request_location import PostListingsRequestLocation
    from .post_listings_request_preorder_info import PostListingsRequestPreorderInfo
    from .post_listings_request_preorder_info_lead_time_unit import PostListingsRequestPreorderInfoLeadTimeUnit
    from .post_listings_request_price import PostListingsRequestPrice
    from .post_listings_request_price_currency import PostListingsRequestPriceCurrency
    from .post_listings_request_seller import PostListingsRequestSeller
    from .post_listings_request_shipping import PostListingsRequestShipping
    from .post_listings_request_shipping_rates_item import PostListingsRequestShippingRatesItem
    from .post_listings_request_shipping_rates_item_rate import PostListingsRequestShippingRatesItemRate
    from .post_listings_request_shipping_rates_item_rate_currency import (
        PostListingsRequestShippingRatesItemRateCurrency,
    )
    from .post_listings_request_videos_item import PostListingsRequestVideosItem
    from .put_listings_slug_request_categories_item import PutListingsSlugRequestCategoriesItem
    from .put_listings_slug_request_condition import PutListingsSlugRequestCondition
    from .put_listings_slug_request_condition_uuid import PutListingsSlugRequestConditionUuid
    from .put_listings_slug_request_exclusive_channel import PutListingsSlugRequestExclusiveChannel
    from .put_listings_slug_request_location import PutListingsSlugRequestLocation
    from .put_listings_slug_request_preorder_info import PutListingsSlugRequestPreorderInfo
    from .put_listings_slug_request_preorder_info_lead_time_unit import PutListingsSlugRequestPreorderInfoLeadTimeUnit
    from .put_listings_slug_request_price import PutListingsSlugRequestPrice
    from .put_listings_slug_request_price_currency import PutListingsSlugRequestPriceCurrency
    from .put_listings_slug_request_seller import PutListingsSlugRequestSeller
    from .put_listings_slug_request_shipping import PutListingsSlugRequestShipping
    from .put_listings_slug_request_shipping_rates_item import PutListingsSlugRequestShippingRatesItem
    from .put_listings_slug_request_shipping_rates_item_rate import PutListingsSlugRequestShippingRatesItemRate
    from .put_listings_slug_request_shipping_rates_item_rate_currency import (
        PutListingsSlugRequestShippingRatesItemRateCurrency,
    )
    from .put_listings_slug_request_videos_item import PutListingsSlugRequestVideosItem
_dynamic_imports: typing.Dict[str, str] = {
    "PostListingsRequestCategoriesItem": ".post_listings_request_categories_item",
    "PostListingsRequestCondition": ".post_listings_request_condition",
    "PostListingsRequestConditionUuid": ".post_listings_request_condition_uuid",
    "PostListingsRequestExclusiveChannel": ".post_listings_request_exclusive_channel",
    "PostListingsRequestLocation": ".post_listings_request_location",
    "PostListingsRequestPreorderInfo": ".post_listings_request_preorder_info",
    "PostListingsRequestPreorderInfoLeadTimeUnit": ".post_listings_request_preorder_info_lead_time_unit",
    "PostListingsRequestPrice": ".post_listings_request_price",
    "PostListingsRequestPriceCurrency": ".post_listings_request_price_currency",
    "PostListingsRequestSeller": ".post_listings_request_seller",
    "PostListingsRequestShipping": ".post_listings_request_shipping",
    "PostListingsRequestShippingRatesItem": ".post_listings_request_shipping_rates_item",
    "PostListingsRequestShippingRatesItemRate": ".post_listings_request_shipping_rates_item_rate",
    "PostListingsRequestShippingRatesItemRateCurrency": ".post_listings_request_shipping_rates_item_rate_currency",
    "PostListingsRequestVideosItem": ".post_listings_request_videos_item",
    "PutListingsSlugRequestCategoriesItem": ".put_listings_slug_request_categories_item",
    "PutListingsSlugRequestCondition": ".put_listings_slug_request_condition",
    "PutListingsSlugRequestConditionUuid": ".put_listings_slug_request_condition_uuid",
    "PutListingsSlugRequestExclusiveChannel": ".put_listings_slug_request_exclusive_channel",
    "PutListingsSlugRequestLocation": ".put_listings_slug_request_location",
    "PutListingsSlugRequestPreorderInfo": ".put_listings_slug_request_preorder_info",
    "PutListingsSlugRequestPreorderInfoLeadTimeUnit": ".put_listings_slug_request_preorder_info_lead_time_unit",
    "PutListingsSlugRequestPrice": ".put_listings_slug_request_price",
    "PutListingsSlugRequestPriceCurrency": ".put_listings_slug_request_price_currency",
    "PutListingsSlugRequestSeller": ".put_listings_slug_request_seller",
    "PutListingsSlugRequestShipping": ".put_listings_slug_request_shipping",
    "PutListingsSlugRequestShippingRatesItem": ".put_listings_slug_request_shipping_rates_item",
    "PutListingsSlugRequestShippingRatesItemRate": ".put_listings_slug_request_shipping_rates_item_rate",
    "PutListingsSlugRequestShippingRatesItemRateCurrency": ".put_listings_slug_request_shipping_rates_item_rate_currency",
    "PutListingsSlugRequestVideosItem": ".put_listings_slug_request_videos_item",
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
