

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ModelParamsMaxTokensToSample(UniversalBaseModel):
    use_cache: typing.Optional[bool] = None
    reasoning_enabled: typing.Optional[bool] = None
    reasoning_budget: typing.Optional[float] = None
    max_tokens: float
    temperature: float
    top_p: typing.Optional[float] = None
    top_k: typing.Optional[float] = None
    stop_sequences: typing.Optional[typing.List[str]] = None
    max_tokens_to_sample: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is a legacy parameter that should not be used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
