

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CreateCompletionResponseChoicesItemLogprobs(UniversalBaseModel):
    text_offset: typing.Optional[typing.List[int]] = None
    token_logprobs: typing.Optional[typing.List[float]] = None
    tokens: typing.Optional[typing.List[str]] = None
    top_logprobs: typing.Optional[typing.List[typing.Dict[str, float]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
