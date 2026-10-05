

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .recipient_type import RecipientType


class GlitchtipProjectAlertRecipient(UniversalBaseModel):
    """
    Desired state for a single project alert recipient.
    """

    recipient_type: RecipientType = pydantic.Field()
    """
    Recipient type: 'email' or 'webhook'
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Webhook URL (empty for email recipients)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
