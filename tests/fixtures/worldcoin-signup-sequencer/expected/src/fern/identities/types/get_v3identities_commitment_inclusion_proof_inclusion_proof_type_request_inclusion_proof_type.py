

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType(enum.StrEnum):
    PROCESSED = "processed"
    MINED = "mined"
    BRIDGED = "bridged"

    def visit(
        self,
        processed: typing.Callable[[], T_Result],
        mined: typing.Callable[[], T_Result],
        bridged: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType.PROCESSED:
            return processed()
        if self is GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType.MINED:
            return mined()
        if self is GetV3IdentitiesCommitmentInclusionProofInclusionProofTypeRequestInclusionProofType.BRIDGED:
            return bridged()
