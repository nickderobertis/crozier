

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class RunCompletionUsage(UniversalBaseModel):
    """
    Usage statistics related to the run. This value will be `null` if the run is not in a terminal state (i.e. `in_progress`, `queued`, etc.).
    """

    completion_tokens: int = pydantic.Field()
    """
    Number of completion tokens used over the course of the run.
    """

    prompt_tokens: int = pydantic.Field()
    """
    Number of prompt tokens used over the course of the run.
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
