

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunStepCompletionUsage(UniversalBaseModel):
    """
    Usage statistics related to the run step. This value will be `null` while the run step's status is `in_progress`.
    """

    completion_tokens: int = pydantic.Field()
    """
    Number of completion tokens used over the course of the run step.
    """

    prompt_tokens: int = pydantic.Field()
    """
    Number of prompt tokens used over the course of the run step.
    """

    total_tokens: int = pydantic.Field()
    """
    Total number of tokens used (prompt + completion).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
