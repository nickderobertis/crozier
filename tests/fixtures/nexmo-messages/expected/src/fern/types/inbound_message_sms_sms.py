

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InboundMessageSmsSms(UniversalBaseModel):
    """
    Channel specific metadata for SMS
    """

    keyword: typing.Optional[str] = pydantic.Field(default=None)
    """
    The first word of the message sent to uppercase.
    """

    num_messages: typing.Optional[str] = pydantic.Field(default=None)
    """
    The number of inbound SMS messages concatenated together to comprise this message. SMS messages are 160 characters, if an inbound message exceeds that size they are concatenated together to forma single message. This number indicates how many messages formed this webhook.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
