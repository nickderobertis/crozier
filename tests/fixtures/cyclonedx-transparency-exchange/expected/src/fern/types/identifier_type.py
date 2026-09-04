

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IdentifierType(enum.StrEnum):
    """
    Enumeration of identifiers types
    """

    CPE = "CPE"
    TEI = "TEI"
    PURL = "PURL"
    COMPLIANCE_DOCUMENT = "COMPLIANCE_DOCUMENT"

    def visit(
        self,
        cpe: typing.Callable[[], T_Result],
        tei: typing.Callable[[], T_Result],
        purl: typing.Callable[[], T_Result],
        compliance_document: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IdentifierType.CPE:
            return cpe()
        if self is IdentifierType.TEI:
            return tei()
        if self is IdentifierType.PURL:
            return purl()
        if self is IdentifierType.COMPLIANCE_DOCUMENT:
            return compliance_document()
