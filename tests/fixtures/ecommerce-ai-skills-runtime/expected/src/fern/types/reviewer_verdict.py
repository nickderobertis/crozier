

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .reviewer_issue import ReviewerIssue
from .reviewer_verdict_verdict import ReviewerVerdictVerdict


class ReviewerVerdict(UniversalBaseModel):
    verdict: ReviewerVerdictVerdict
    issues: typing.List[ReviewerIssue]
    evidence_refs: typing.List[str]
    limitations: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
