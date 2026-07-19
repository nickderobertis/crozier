

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GeminiThinkingConfig(UniversalBaseModel):
    include_thoughts: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to include thoughts in the model's response.
    """

    thinking_budget: typing.Optional[int] = pydantic.Field(default=None)
    """
    The thinking budget for the model.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
