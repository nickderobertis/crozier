

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CompositeSignatureBinding(enum.StrEnum):
    PQ_OVER_CLASSICAL = "pq_over_classical"
    CLASSICAL_ONLY = "classical_only"
    INDEPENDENT = "independent"

    def visit(
        self,
        pq_over_classical: typing.Callable[[], T_Result],
        classical_only: typing.Callable[[], T_Result],
        independent: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CompositeSignatureBinding.PQ_OVER_CLASSICAL:
            return pq_over_classical()
        if self is CompositeSignatureBinding.CLASSICAL_ONLY:
            return classical_only()
        if self is CompositeSignatureBinding.INDEPENDENT:
            return independent()
