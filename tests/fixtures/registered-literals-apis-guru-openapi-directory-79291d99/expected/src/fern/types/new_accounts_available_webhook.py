

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class NewAccountsAvailableWebhook(UniversalBaseModel):
    """
    Fired when Plaid detects a new account for Items created or updated with [Account Select v2](https://plaid.com/docs/link/customization/#account-select). Upon receiving this webhook, you can prompt your users to share new accounts with you through [Account Select v2 update mode](https://plaid.com/docs/link/update-mode/#using-update-mode-to-request-new-accounts).
    """

    environment: typing.Optional[WebhookEnvironmentValues] = None
    error: typing.Optional[PlaidError] = None
    item_id: typing.Optional[ItemId] = None
    webhook_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    `NEW_ACCOUNTS_AVAILABLE`
    """

    webhook_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    `ITEM`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
