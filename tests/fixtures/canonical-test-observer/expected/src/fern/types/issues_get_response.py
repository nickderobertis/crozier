

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .minimal_issue_response import MinimalIssueResponse


class IssuesGetResponse(UniversalBaseModel):
    issues: typing.List[MinimalIssueResponse]
    count: int
    limit: int
    offset: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
