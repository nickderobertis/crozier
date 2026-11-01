

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .issue_source import IssueSource
from .issue_status import IssueStatus
from .minimal_issue_test_result_attachment_rule_response import MinimalIssueTestResultAttachmentRuleResponse


class IssueResponse(UniversalBaseModel):
    id: int
    source: IssueSource
    project: str
    key: str
    title: str
    status: IssueStatus
    url: str
    labels: typing.Optional[typing.List[str]] = None
    auto_rerun_enabled: bool
    attachment_rules: typing.List[MinimalIssueTestResultAttachmentRuleResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
