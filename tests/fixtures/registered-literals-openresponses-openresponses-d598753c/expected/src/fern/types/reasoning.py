

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reasoning_effort_enum import ReasoningEffortEnum
from .reasoning_summary import ReasoningSummary


class Reasoning(UniversalBaseModel):
    """
    Reasoning configuration and metadata that were used for the response.
    """

    effort: typing.Optional[ReasoningEffortEnum] = None
    summary: typing.Optional[ReasoningSummary] = pydantic.Field(default=None)
    """
    A model-generated summary of its reasoning that was produced, if available.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
