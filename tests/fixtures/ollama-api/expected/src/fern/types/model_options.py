

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_options_stop import ModelOptionsStop


class ModelOptions(UniversalBaseModel):
    """
    Runtime options that control text generation
    """

    seed: typing.Optional[int] = pydantic.Field(default=None)
    """
    Random seed used for reproducible outputs
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    Controls randomness in generation (higher = more random)
    """

    top_k: typing.Optional[int] = pydantic.Field(default=None)
    """
    Limits next token selection to the K most likely
    """

    top_p: typing.Optional[float] = pydantic.Field(default=None)
    """
    Cumulative probability threshold for nucleus sampling
    """

    min_p: typing.Optional[float] = pydantic.Field(default=None)
    """
    Minimum probability threshold for token selection
    """

    stop: typing.Optional[ModelOptionsStop] = pydantic.Field(default=None)
    """
    Stop sequences that will halt generation
    """

    num_ctx: typing.Optional[int] = pydantic.Field(default=None)
    """
    Context length size (number of tokens)
    """

    num_predict: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum number of tokens to generate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
