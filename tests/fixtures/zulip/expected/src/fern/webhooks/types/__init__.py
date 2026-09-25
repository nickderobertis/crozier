



import typing
from importlib import import_module

if typing.TYPE_CHECKING:
    from .zulip_outgoing_webhooks_response import ZulipOutgoingWebhooksResponse
    from .zulip_outgoing_webhooks_response_message import ZulipOutgoingWebhooksResponseMessage
    from .zulip_outgoing_webhooks_response_message_display_recipient import (
        ZulipOutgoingWebhooksResponseMessageDisplayRecipient,
    )
    from .zulip_outgoing_webhooks_response_message_display_recipient_one_item import (
        ZulipOutgoingWebhooksResponseMessageDisplayRecipientOneItem,
    )
    from .zulip_outgoing_webhooks_response_message_edit_history_item import (
        ZulipOutgoingWebhooksResponseMessageEditHistoryItem,
    )
    from .zulip_outgoing_webhooks_response_message_submessages_item import (
        ZulipOutgoingWebhooksResponseMessageSubmessagesItem,
    )
    from .zulip_outgoing_webhooks_response_message_topic_links_item import (
        ZulipOutgoingWebhooksResponseMessageTopicLinksItem,
    )
_dynamic_imports: typing.Dict[str, str] = {
    "ZulipOutgoingWebhooksResponse": ".zulip_outgoing_webhooks_response",
    "ZulipOutgoingWebhooksResponseMessage": ".zulip_outgoing_webhooks_response_message",
    "ZulipOutgoingWebhooksResponseMessageDisplayRecipient": ".zulip_outgoing_webhooks_response_message_display_recipient",
    "ZulipOutgoingWebhooksResponseMessageDisplayRecipientOneItem": ".zulip_outgoing_webhooks_response_message_display_recipient_one_item",
    "ZulipOutgoingWebhooksResponseMessageEditHistoryItem": ".zulip_outgoing_webhooks_response_message_edit_history_item",
    "ZulipOutgoingWebhooksResponseMessageSubmessagesItem": ".zulip_outgoing_webhooks_response_message_submessages_item",
    "ZulipOutgoingWebhooksResponseMessageTopicLinksItem": ".zulip_outgoing_webhooks_response_message_topic_links_item",
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
    "ZulipOutgoingWebhooksResponse",
    "ZulipOutgoingWebhooksResponseMessage",
    "ZulipOutgoingWebhooksResponseMessageDisplayRecipient",
    "ZulipOutgoingWebhooksResponseMessageDisplayRecipientOneItem",
    "ZulipOutgoingWebhooksResponseMessageEditHistoryItem",
    "ZulipOutgoingWebhooksResponseMessageSubmessagesItem",
    "ZulipOutgoingWebhooksResponseMessageTopicLinksItem",
]
