

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Capability(str, enum.Enum):
    CAPABILITY_IAM = "CAPABILITY_IAM"
    CAPABILITY_NAMED_IAM = "CAPABILITY_NAMED_IAM"
    CAPABILITY_AUTO_EXPAND = "CAPABILITY_AUTO_EXPAND"

    def visit(
        self,
        capability_iam: typing.Callable[[], T_Result],
        capability_named_iam: typing.Callable[[], T_Result],
        capability_auto_expand: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Capability.CAPABILITY_IAM:
            return capability_iam()
        if self is Capability.CAPABILITY_NAMED_IAM:
            return capability_named_iam()
        if self is Capability.CAPABILITY_AUTO_EXPAND:
            return capability_auto_expand()
