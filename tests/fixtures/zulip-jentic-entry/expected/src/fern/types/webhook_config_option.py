

import typing

from .webhook_config_option_item import WebhookConfigOptionItem

WebhookConfigOption = typing.List[WebhookConfigOptionItem]
"""
An array of configuration options that can be set when creating
a bot user for this incoming webhook integration.

This is an unstable API. Please discuss in chat.zulip.org before
using it.

**Changes**: As of Zulip 11.0 (feature level 403), this
object is reserved for integration-specific configuration options
that can be set when creating a bot user. Previously, this object
also included optional webhook URL parameters, which are now
specified in the `url_options` object.

Before Zulip 10.0 (feature level 318), this field was named `config`,
and was reserved for configuration data key-value pairs.
"""
