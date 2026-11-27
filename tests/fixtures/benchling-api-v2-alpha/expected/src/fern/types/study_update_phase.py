

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudyUpdatePhase(enum.StrEnum):
    """
    The phase of the Study.
    """

    DESIGN = "DESIGN"
    EXECUTION = "EXECUTION"
    COMPLETE = "COMPLETE"

    def visit(
        self,
        design: typing.Callable[[], T_Result],
        execution: typing.Callable[[], T_Result],
        complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StudyUpdatePhase.DESIGN:
            return design()
        if self is StudyUpdatePhase.EXECUTION:
            return execution()
        if self is StudyUpdatePhase.COMPLETE:
            return complete()
