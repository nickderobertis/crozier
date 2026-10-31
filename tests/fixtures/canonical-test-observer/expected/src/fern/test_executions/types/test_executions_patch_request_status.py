

import typing

from ...types.test_execution_status import TestExecutionStatus
from .test_executions_patch_request_status_one import TestExecutionsPatchRequestStatusOne

TestExecutionsPatchRequestStatus = typing.Union[TestExecutionStatus, TestExecutionsPatchRequestStatusOne]
