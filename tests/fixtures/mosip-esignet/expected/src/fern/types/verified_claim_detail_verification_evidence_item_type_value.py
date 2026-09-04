

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VerifiedClaimDetailVerificationEvidenceItemTypeValue(enum.StrEnum):
    DOCUMENT = "document"
    ELECTRONIC_RECORD = "electronic_record"
    VOUCH = "vouch"
    ELECTRONIC_SIGNATURE = "electronic_signature"

    def visit(
        self,
        document: typing.Callable[[], T_Result],
        electronic_record: typing.Callable[[], T_Result],
        vouch: typing.Callable[[], T_Result],
        electronic_signature: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is VerifiedClaimDetailVerificationEvidenceItemTypeValue.DOCUMENT:
            return document()
        if self is VerifiedClaimDetailVerificationEvidenceItemTypeValue.ELECTRONIC_RECORD:
            return electronic_record()
        if self is VerifiedClaimDetailVerificationEvidenceItemTypeValue.VOUCH:
            return vouch()
        if self is VerifiedClaimDetailVerificationEvidenceItemTypeValue.ELECTRONIC_SIGNATURE:
            return electronic_signature()
