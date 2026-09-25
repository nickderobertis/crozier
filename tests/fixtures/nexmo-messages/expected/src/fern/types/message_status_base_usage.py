

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .message_status_base_usage_currency import MessageStatusBaseUsageCurrency


class MessageStatusBaseUsage(UniversalBaseModel):
    currency: typing.Optional[MessageStatusBaseUsageCurrency] = pydantic.Field(default=None)
    """
    The charge currency in ISO 4217 format.
    """

    price: typing.Optional[str] = pydantic.Field(default=None)
    """
    The charge amount as a stringified number.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
