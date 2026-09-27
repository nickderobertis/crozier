

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConversationProperties(UniversalBaseModel):
    """
    Conversation properties
    """

    ttl: typing.Optional[float] = pydantic.Field(default=None)
    """
    Time to leave. After how many seconds an empty conversation is deleted.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
