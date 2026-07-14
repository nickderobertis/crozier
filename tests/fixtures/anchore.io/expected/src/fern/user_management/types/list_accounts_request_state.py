

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListAccountsRequestState(str, enum.Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"
    DELETING = "deleting"

    def visit(
        self,
        enabled: typing.Callable[[], T_Result],
        disabled: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListAccountsRequestState.ENABLED:
            return enabled()
        if self is ListAccountsRequestState.DISABLED:
            return disabled()
        if self is ListAccountsRequestState.DELETING:
            return deleting()
