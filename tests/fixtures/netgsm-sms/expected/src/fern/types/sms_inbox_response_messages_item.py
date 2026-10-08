

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SmsInboxResponseMessagesItem(UniversalBaseModel):
    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    SMS message content
    """

    sender: typing.Optional[str] = pydantic.Field(default=None)
    """
    Sender number
    """

    receiver: typing.Optional[str] = pydantic.Field(default=None)
    """
    Recipient number
    """

    datetime: typing.Optional[str] = pydantic.Field(default=None)
    """
    Send date and time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
