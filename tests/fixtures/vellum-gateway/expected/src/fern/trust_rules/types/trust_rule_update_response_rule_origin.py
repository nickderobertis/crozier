

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TrustRuleUpdateResponseRuleOrigin(enum.StrEnum):
    DEFAULT = "default"
    USER_DEFINED = "user_defined"

    def visit(self, default: typing.Callable[[], T_Result], user_defined: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrustRuleUpdateResponseRuleOrigin.DEFAULT:
            return default()
        if self is TrustRuleUpdateResponseRuleOrigin.USER_DEFINED:
            return user_defined()
