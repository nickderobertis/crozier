

import typing

from .zulip_outgoing_webhooks_response_message_display_recipient_one_item import (
    ZulipOutgoingWebhooksResponseMessageDisplayRecipientOneItem,
)

ZulipOutgoingWebhooksResponseMessageDisplayRecipient = typing.Union[
    str, typing.List[ZulipOutgoingWebhooksResponseMessageDisplayRecipientOneItem]
]
