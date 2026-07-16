



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .post_conversations_conversation_id_offer_request_offer_items_item import (
        PostConversationsConversationIdOfferRequestOfferItemsItem,
    )
    from .post_conversations_conversation_id_offer_request_price import PostConversationsConversationIdOfferRequestPrice
    from .post_conversations_conversation_id_offer_request_price_currency import (
        PostConversationsConversationIdOfferRequestPriceCurrency,
    )
    from .post_conversations_conversation_id_offer_request_shipping_price import (
        PostConversationsConversationIdOfferRequestShippingPrice,
    )
    from .post_conversations_conversation_id_offer_request_shipping_price_currency import (
        PostConversationsConversationIdOfferRequestShippingPriceCurrency,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "PostConversationsConversationIdOfferRequestOfferItemsItem": ".post_conversations_conversation_id_offer_request_offer_items_item",
    "PostConversationsConversationIdOfferRequestPrice": ".post_conversations_conversation_id_offer_request_price",
    "PostConversationsConversationIdOfferRequestPriceCurrency": ".post_conversations_conversation_id_offer_request_price_currency",
    "PostConversationsConversationIdOfferRequestShippingPrice": ".post_conversations_conversation_id_offer_request_shipping_price",
    "PostConversationsConversationIdOfferRequestShippingPriceCurrency": ".post_conversations_conversation_id_offer_request_shipping_price_currency",
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
    "PostConversationsConversationIdOfferRequestOfferItemsItem",
    "PostConversationsConversationIdOfferRequestPrice",
    "PostConversationsConversationIdOfferRequestPriceCurrency",
    "PostConversationsConversationIdOfferRequestShippingPrice",
    "PostConversationsConversationIdOfferRequestShippingPriceCurrency",
]
