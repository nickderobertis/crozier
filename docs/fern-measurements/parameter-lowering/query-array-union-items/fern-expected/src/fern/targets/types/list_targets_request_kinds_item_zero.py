

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListTargetsRequestKindsItemZero(enum.StrEnum):
    NEBULA = "nebula"
    CLUSTER = "cluster"
    GALAXY = "galaxy"

    def visit(
        self,
        nebula: typing.Callable[[], T_Result],
        cluster: typing.Callable[[], T_Result],
        galaxy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListTargetsRequestKindsItemZero.NEBULA:
            return nebula()
        if self is ListTargetsRequestKindsItemZero.CLUSTER:
            return cluster()
        if self is ListTargetsRequestKindsItemZero.GALAXY:
            return galaxy()
