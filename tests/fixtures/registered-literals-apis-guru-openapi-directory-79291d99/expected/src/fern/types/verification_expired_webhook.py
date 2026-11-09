

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class VerificationExpiredWebhook(UniversalBaseModel):
    """
    Fired when an Item was not verified via automated micro-deposits after seven days since the automated micro-deposit was made.
    """

    account_id: str = pydantic.Field()
    """
    The `account_id` of the account associated with the webhook
    """

    environment: WebhookEnvironmentValues
    item_id: ItemId
    webhook_code: str = pydantic.Field()
    """
    `VERIFICATION_EXPIRED`
    """

    webhook_type: str = pydantic.Field()
    """
    `AUTH`
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
