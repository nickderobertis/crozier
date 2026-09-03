

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class IdentificationRequestIdentificationType(enum.StrEnum):
    EID_VERIFICATION = "eid_verification"
    DOCUMENT_VERIFICATION = "document_verification"
    BIOMETRIC_VERIFICATION = "biometric_verification"

    def visit(
        self,
        eid_verification: typing.Callable[[], T_Result],
        document_verification: typing.Callable[[], T_Result],
        biometric_verification: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentificationRequestIdentificationType.EID_VERIFICATION:
            return eid_verification()
        if self is IdentificationRequestIdentificationType.DOCUMENT_VERIFICATION:
            return document_verification()
        if self is IdentificationRequestIdentificationType.BIOMETRIC_VERIFICATION:
            return biometric_verification()
