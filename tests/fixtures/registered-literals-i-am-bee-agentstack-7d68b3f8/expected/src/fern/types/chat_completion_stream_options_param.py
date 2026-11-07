

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionStreamOptionsParam(UniversalBaseModel):
    """
    Options for streaming response. Only set this when you set `stream: true`.
    """

    include_obfuscation: typing.Optional[bool] = None
    include_usage: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
