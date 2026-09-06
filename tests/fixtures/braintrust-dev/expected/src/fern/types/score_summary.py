

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScoreSummary(UniversalBaseModel):
    """
    Summary of a score's performance
    """

    name: str = pydantic.Field()
    """
    Name of the score
    """

    score: float = pydantic.Field()
    """
    Average score across all examples
    """

    diff: typing.Optional[float] = pydantic.Field(default=None)
    """
    Difference in score between the current and comparison experiment
    """

    improvements: int = pydantic.Field()
    """
    Number of improvements in the score
    """

    regressions: int = pydantic.Field()
    """
    Number of regressions in the score
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
