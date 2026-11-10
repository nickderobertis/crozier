

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .account_ids_with_updated_identity import AccountIdsWithUpdatedIdentity
from .item_id import ItemId
from .plaid_error import PlaidError
from .webhook_environment_values import WebhookEnvironmentValues


class IdentityDefaultUpdateWebhook(UniversalBaseModel):
    """
    Fired when a change to identity data has been detected on an Item. Items are checked for identity updates every 30-90 days. We recommend that upon receiving this webhook you make another call to `/identity/get` to fetch the user's latest identity data.
    """

    account_ids_with_updated_identity: AccountIdsWithUpdatedIdentity
    environment: WebhookEnvironmentValues
    error: typing.Optional[PlaidError] = None
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `DEFAULT_UPDATE`
    """

    webhook_type: str = pydantic.Field()
    """
    `IDENTITY`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
