

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MessageStatusWhatsAppWhatsappConversationOrigin(UniversalBaseModel):
    """
    An object contining data related to the origin of the conversation.
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    The conversation type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
