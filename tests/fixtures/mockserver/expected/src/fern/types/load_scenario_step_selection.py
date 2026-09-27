

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoadScenarioStepSelection(enum.StrEnum):
    """
    how each iteration selects which steps to run: SEQUENTIAL (default) runs ALL steps in declared order (a multi-step user journey); WEIGHTED runs exactly ONE step per iteration chosen at random proportional to each step's weight (mixed-workload modelling, e.g. 70% browse / 20% search / 10% checkout). Cross-step captures are meaningful only under SEQUENTIAL (a WEIGHTED iteration runs a single step); feeder data and pacing apply to both.
    """

    SEQUENTIAL = "SEQUENTIAL"
    WEIGHTED = "WEIGHTED"

    def visit(self, sequential: typing.Callable[[], T_Result], weighted: typing.Callable[[], T_Result]) -> T_Result:
        if self is LoadScenarioStepSelection.SEQUENTIAL:
            return sequential()
        if self is LoadScenarioStepSelection.WEIGHTED:
            return weighted()
