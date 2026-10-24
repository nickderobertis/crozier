

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .platform_id import PlatformId
from .reviewer_issue_severity import ReviewerIssueSeverity


class ReviewerIssue(UniversalBaseModel):
    code: str
    message: str
    severity: ReviewerIssueSeverity
    evidence_refs: typing.List[str]
    platforms: typing.List[PlatformId]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
