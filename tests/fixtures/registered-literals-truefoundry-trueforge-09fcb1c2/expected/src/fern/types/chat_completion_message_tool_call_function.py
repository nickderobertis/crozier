

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionMessageToolCallFunction(UniversalBaseModel):
    arguments: str = pydantic.Field()
    """
    JSON-encoded function arguments string.
    """

    name: str = pydantic.Field()
    """
    Function/tool name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
