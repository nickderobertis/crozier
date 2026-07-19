

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompletionTokensDetails(UniversalBaseModel):
    """
    Breakdown of tokens used in a completion.
    """

    accepted_prediction_tokens: typing.Optional[int] = None
    audio_tokens: typing.Optional[int] = None
    reasoning_tokens: typing.Optional[int] = None
    rejected_prediction_tokens: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
