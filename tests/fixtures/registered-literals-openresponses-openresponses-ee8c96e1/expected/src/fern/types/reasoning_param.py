

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_effort_enum import ReasoningEffortEnum
from .reasoning_param_summary import ReasoningParamSummary


class ReasoningParam(UniversalBaseModel):
    """
    **gpt-5 and o-series models only** Configuration options for [reasoning models](https://platform.openai.com/docs/guides/reasoning).
    """

    effort: typing.Optional[ReasoningEffortEnum] = None
    summary: typing.Optional[ReasoningParamSummary] = pydantic.Field(default=None)
    """
    Controls whether the response includes a reasoning summary.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
