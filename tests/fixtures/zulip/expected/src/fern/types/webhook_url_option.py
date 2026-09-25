

import typing

from .webhook_url_option_item import WebhookUrlOptionItem

WebhookUrlOption = typing.List[WebhookUrlOptionItem]
"""
An array of optional URL parameter options for the incoming webhook
integration. In the web app, these are used when
[generating a URL for an integration](/help/generate-integration-url).

**Changes**: Before Zulip 12.0 (feature level 485), `input_type`
was named `validator`.

New in Zulip 11.0 (feature level 403). Previously, these optional
URL parameter options were included in the `config_options` object.
"""
