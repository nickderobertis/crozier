

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateProjectAutomationConfigBtqlExportCredentialsType(enum.StrEnum):
    AWS_IAM = "aws_iam"

    def visit(self, aws_iam: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateProjectAutomationConfigBtqlExportCredentialsType.AWS_IAM:
            return aws_iam()
