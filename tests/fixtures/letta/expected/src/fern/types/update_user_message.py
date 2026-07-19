

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .update_user_message_content import UpdateUserMessageContent


class UpdateUserMessage(UniversalBaseModel):
    content: UpdateUserMessageContent = pydantic.Field()
    """
    The message content sent by the user (can be a string or an array of multi-modal content parts)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
