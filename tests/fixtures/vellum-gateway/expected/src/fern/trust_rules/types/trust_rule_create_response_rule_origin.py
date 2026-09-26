

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TrustRuleCreateResponseRuleOrigin(enum.StrEnum):
    DEFAULT = "default"
    USER_DEFINED = "user_defined"

    def visit(self, default: typing.Callable[[], T_Result], user_defined: typing.Callable[[], T_Result]) -> T_Result:
        if self is TrustRuleCreateResponseRuleOrigin.DEFAULT:
            return default()
        if self is TrustRuleCreateResponseRuleOrigin.USER_DEFINED:
            return user_defined()
