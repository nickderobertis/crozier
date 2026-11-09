

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class OpenAiResponseUsageSchema(UniversalBaseModel):
    """
    OpenAI Usage schema from Response API
    """

    input_tokens: int
    output_tokens: int
    total_tokens: int
    input_tokens_details: typing.Optional[typing.Dict[str, typing.Optional[int]]] = None
    output_tokens_details: typing.Optional[typing.Dict[str, typing.Optional[int]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
