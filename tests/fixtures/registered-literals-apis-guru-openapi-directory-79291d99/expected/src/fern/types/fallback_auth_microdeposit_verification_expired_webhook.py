

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .item_id import ItemId
from .webhook_environment_values import WebhookEnvironmentValues


class FallbackAuthMicrodepositVerificationExpiredWebhook(UniversalBaseModel):
    """
    Fires when an account has an expired verification when using micro-deposits
    """

    account_id: str = pydantic.Field()
    """
    The external account ID associated with the micro-deposit
    """

    environment: WebhookEnvironmentValues
    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error code associated with the webhook.
    """

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
