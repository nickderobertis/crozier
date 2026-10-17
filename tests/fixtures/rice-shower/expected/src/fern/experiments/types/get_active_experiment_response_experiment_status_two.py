

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetActiveExperimentResponseExperimentStatusTwo(enum.StrEnum):
    ABORTED = "aborted"

    def visit(self, aborted: typing.Callable[[], T_Result]) -> T_Result:
        if self is GetActiveExperimentResponseExperimentStatusTwo.ABORTED:
            return aborted()
