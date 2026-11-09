

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionRequestSystemMessage(UniversalBaseModel):
    content: str = pydantic.Field()
    """
    The contents of the system message.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    An optional name for the participant. Provides the model information to differentiate between participants of the same role.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
