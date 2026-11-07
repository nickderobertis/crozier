

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeclareIntentResponseVerificationMode(enum.StrEnum):
    CLASSICAL_ONLY = "classical_only"
    HYBRID_PREFERRED = "hybrid_preferred"
    HYBRID_REQUIRED = "hybrid_required"
    PQ_ONLY = "pq_only"

    def visit(
        self,
        classical_only: typing.Callable[[], T_Result],
        hybrid_preferred: typing.Callable[[], T_Result],
        hybrid_required: typing.Callable[[], T_Result],
        pq_only: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DeclareIntentResponseVerificationMode.CLASSICAL_ONLY:
            return classical_only()
        if self is DeclareIntentResponseVerificationMode.HYBRID_PREFERRED:
            return hybrid_preferred()
        if self is DeclareIntentResponseVerificationMode.HYBRID_REQUIRED:
            return hybrid_required()
        if self is DeclareIntentResponseVerificationMode.PQ_ONLY:
            return pq_only()
