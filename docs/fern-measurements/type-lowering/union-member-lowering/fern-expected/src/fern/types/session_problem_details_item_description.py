

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .session_problem_details_item_description_description import SessionProblemDetailsItemDescriptionDescription
from .session_problem_details_item_description_issue import SessionProblemDetailsItemDescriptionIssue


class SessionProblemDetailsItemDescription(UniversalBaseModel):
    issue: typing.Optional[SessionProblemDetailsItemDescriptionIssue] = None
    description: typing.Optional[SessionProblemDetailsItemDescriptionDescription] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
