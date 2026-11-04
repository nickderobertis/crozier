

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImportAgentItemResultStatus(enum.StrEnum):
    CREATED = "created"
    EXISTS = "exists"
    FAILED = "failed"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        exists: typing.Callable[[], T_Result],
        failed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ImportAgentItemResultStatus.CREATED:
            return created()
        if self is ImportAgentItemResultStatus.EXISTS:
            return exists()
        if self is ImportAgentItemResultStatus.FAILED:
            return failed()
