

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .minimal_issue_test_result_attachment_response import MinimalIssueTestResultAttachmentResponse
from .previous_test_result import PreviousTestResult
from .test_result_status import TestResultStatus


class TestResultResponse(UniversalBaseModel):
    id: int
    name: str
    created_at: dt.datetime
    category: str
    template_id: str
    status: TestResultStatus
    comment: str
    io_log: str
    previous_results: typing.Optional[typing.List[PreviousTestResult]] = pydantic.Field(default=None)
    """
    The last 10 test results matched with the current test execution. The items are sorted in descending order, the first test result is the most recent, while the last one is the oldest one.
    """

    issues: typing.List[MinimalIssueTestResultAttachmentResponse]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
