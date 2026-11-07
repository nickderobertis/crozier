

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AwsSecretParameterParameterType(enum.StrEnum):
    AWS_SECRET = "aws_secret"

    def visit(self, aws_secret: typing.Callable[[], T_Result]) -> T_Result:
        if self is AwsSecretParameterParameterType.AWS_SECRET:
            return aws_secret()
