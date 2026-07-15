

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class AdvancedAuthAuthFlowType(str, enum.Enum):
    OAUTH20 = "oauth2.0"
    OAUTH10 = "oauth1.0"

    def visit(self, oauth20: typing.Callable[[], T_Result], oauth10: typing.Callable[[], T_Result]) -> T_Result:
        if self is AdvancedAuthAuthFlowType.OAUTH20:
            return oauth20()
        if self is AdvancedAuthAuthFlowType.OAUTH10:
            return oauth10()
