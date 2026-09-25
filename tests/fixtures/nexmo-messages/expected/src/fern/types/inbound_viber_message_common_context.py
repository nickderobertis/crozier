

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InboundViberMessageCommonContext(UniversalBaseModel):
    """
    Object containing contextual details for the inbound message when it is a response to another message.
    """

    message_uuid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the message being replied to.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
