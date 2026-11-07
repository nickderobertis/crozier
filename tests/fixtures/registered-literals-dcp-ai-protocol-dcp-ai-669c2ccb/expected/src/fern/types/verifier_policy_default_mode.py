

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VerifierPolicyDefaultMode(enum.StrEnum):
    CLASSICAL_ONLY = "classical_only"
    PQ_ONLY = "pq_only"
    HYBRID_REQUIRED = "hybrid_required"
    HYBRID_PREFERRED = "hybrid_preferred"

    def visit(
        self,
        classical_only: typing.Callable[[], T_Result],
        pq_only: typing.Callable[[], T_Result],
        hybrid_required: typing.Callable[[], T_Result],
        hybrid_preferred: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VerifierPolicyDefaultMode.CLASSICAL_ONLY:
            return classical_only()
        if self is VerifierPolicyDefaultMode.PQ_ONLY:
            return pq_only()
        if self is VerifierPolicyDefaultMode.HYBRID_REQUIRED:
            return hybrid_required()
        if self is VerifierPolicyDefaultMode.HYBRID_PREFERRED:
            return hybrid_preferred()
