

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMockserverLoadScenarioNameResponseStatus(enum.StrEnum):
    DELETED = "deleted"
    ABSENT = "absent"

    def visit(self, deleted: typing.Callable[[], T_Result], absent: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMockserverLoadScenarioNameResponseStatus.DELETED:
            return deleted()
        if self is DeleteMockserverLoadScenarioNameResponseStatus.ABSENT:
            return absent()
