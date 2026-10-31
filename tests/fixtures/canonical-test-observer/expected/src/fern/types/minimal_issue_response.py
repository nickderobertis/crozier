

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .issue_source import IssueSource
from .issue_status import IssueStatus


class MinimalIssueResponse(UniversalBaseModel):
    id: int
    source: IssueSource
    project: str
    key: str
    title: str
    status: IssueStatus
    url: str
    labels: typing.Optional[typing.List[str]] = None
    test_executions_count: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
