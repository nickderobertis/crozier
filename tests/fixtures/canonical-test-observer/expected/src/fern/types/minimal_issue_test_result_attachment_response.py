

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .minimal_issue_response import MinimalIssueResponse
from .minimal_issue_test_result_attachment_rule_response import MinimalIssueTestResultAttachmentRuleResponse


class MinimalIssueTestResultAttachmentResponse(UniversalBaseModel):
    issue: MinimalIssueResponse
    attachment_rule: typing.Optional[MinimalIssueTestResultAttachmentRuleResponse] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
