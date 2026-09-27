

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeleteMockserverChaosExperimentProfilesNameResponseStatus(enum.StrEnum):
    DELETED = "deleted"
    ABSENT = "absent"

    def visit(self, deleted: typing.Callable[[], T_Result], absent: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeleteMockserverChaosExperimentProfilesNameResponseStatus.DELETED:
            return deleted()
        if self is DeleteMockserverChaosExperimentProfilesNameResponseStatus.ABSENT:
            return absent()
