

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionRequestFunctionMessage(UniversalBaseModel):
    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    The contents of the function message.
    """

    name: str = pydantic.Field()
    """
    The name of the function to call.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
