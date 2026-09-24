

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionChunkDeltaToolCallFunction(UniversalBaseModel):
    arguments: typing.Optional[str] = pydantic.Field(default=None)
    """
    Partial or complete JSON arguments string.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Partial or complete function name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
