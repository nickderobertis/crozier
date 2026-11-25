

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_problem_details_item_one_description import SessionProblemDetailsItemOneDescription
from .session_problem_details_item_one_issue import SessionProblemDetailsItemOneIssue


class SessionProblemDetailsItemOne(UniversalBaseModel):
    issue: typing.Optional[SessionProblemDetailsItemOneIssue] = None
    description: typing.Optional[SessionProblemDetailsItemOneDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
