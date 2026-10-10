

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .initial_user_message_type import InitialUserMessageType


class InitialUserMessage(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    Initial user message content injected at the start of every session.
    """

    type: InitialUserMessageType = pydantic.Field()
    """
    Initial message type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
