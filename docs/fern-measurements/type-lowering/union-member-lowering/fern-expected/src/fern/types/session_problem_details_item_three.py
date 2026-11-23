

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_problem_details_item_three_issue import SessionProblemDetailsItemThreeIssue


class SessionProblemDetailsItemThree(UniversalBaseModel):
    issue: typing.Optional[SessionProblemDetailsItemThreeIssue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
