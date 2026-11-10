

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .match_summary_code import MatchSummaryCode


class MatchSummary(UniversalBaseModel):
    """
    Summary object reflecting the match result of the associated data
    """

    summary: MatchSummaryCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
