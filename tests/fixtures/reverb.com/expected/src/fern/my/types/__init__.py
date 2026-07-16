



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_my_follows_search_request_currency import PostMyFollowsSearchRequestCurrency
    from .post_my_follows_search_request_listing_type import PostMyFollowsSearchRequestListingType
    from .post_my_negotiations_id_counter_request_offer_items_item import (
        PostMyNegotiationsIdCounterRequestOfferItemsItem,
    )
    from .post_my_negotiations_id_counter_request_price import PostMyNegotiationsIdCounterRequestPrice
    from .post_my_negotiations_id_counter_request_price_currency import PostMyNegotiationsIdCounterRequestPriceCurrency
    from .post_my_negotiations_id_counter_request_shipping_price import PostMyNegotiationsIdCounterRequestShippingPrice
    from .post_my_negotiations_id_counter_request_shipping_price_currency import (
        PostMyNegotiationsIdCounterRequestShippingPriceCurrency,
    )
    from .put_my_listings_slug_state_end_request_reason import PutMyListingsSlugStateEndRequestReason
_dynamic_imports: typing.Dict[str, str] = {
    "PostMyFollowsSearchRequestCurrency": ".post_my_follows_search_request_currency",
    "PostMyFollowsSearchRequestListingType": ".post_my_follows_search_request_listing_type",
    "PostMyNegotiationsIdCounterRequestOfferItemsItem": ".post_my_negotiations_id_counter_request_offer_items_item",
    "PostMyNegotiationsIdCounterRequestPrice": ".post_my_negotiations_id_counter_request_price",
    "PostMyNegotiationsIdCounterRequestPriceCurrency": ".post_my_negotiations_id_counter_request_price_currency",
    "PostMyNegotiationsIdCounterRequestShippingPrice": ".post_my_negotiations_id_counter_request_shipping_price",
    "PostMyNegotiationsIdCounterRequestShippingPriceCurrency": ".post_my_negotiations_id_counter_request_shipping_price_currency",
    "PutMyListingsSlugStateEndRequestReason": ".put_my_listings_slug_state_end_request_reason",
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
    "PostMyFollowsSearchRequestCurrency",
    "PostMyFollowsSearchRequestListingType",
    "PostMyNegotiationsIdCounterRequestOfferItemsItem",
    "PostMyNegotiationsIdCounterRequestPrice",
    "PostMyNegotiationsIdCounterRequestPriceCurrency",
    "PostMyNegotiationsIdCounterRequestShippingPrice",
    "PostMyNegotiationsIdCounterRequestShippingPriceCurrency",
    "PutMyListingsSlugStateEndRequestReason",
]
