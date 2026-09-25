

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_effort import ReasoningEffort


class ModelProperties(UniversalBaseModel):
    """
    Optional model capability metadata.
    """

    context_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum context window size in tokens.
    """

    max_output_tokens: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum output tokens the model can generate.
    """

    reasoning_efforts: typing.Optional[typing.List[ReasoningEffort]] = pydantic.Field(default=None)
    """
    Supported reasoning-effort values for this model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
