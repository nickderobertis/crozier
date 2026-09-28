

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PutMockserverChaosExperimentProfilesNameResponseStatus(enum.StrEnum):
    SAVED = "saved"

    def visit(self, saved: typing.Callable[[], T_Result]) -> T_Result:
        if self is PutMockserverChaosExperimentProfilesNameResponseStatus.SAVED:
            return saved()
