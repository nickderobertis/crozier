

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ProofStatus(enum.StrEnum):
    """
    Where the proof is in its review.
    """

    PROOF_READY = "proof_ready"
    PROOF_PENDING = "proof_pending"

    def visit(
        self, proof_ready: typing.Callable[[], T_Result], proof_pending: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is ProofStatus.PROOF_READY:
            return proof_ready()
        if self is ProofStatus.PROOF_PENDING:
            return proof_pending()
