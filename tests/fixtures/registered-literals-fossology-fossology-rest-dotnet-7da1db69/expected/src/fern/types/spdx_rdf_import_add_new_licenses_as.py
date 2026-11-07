

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SpdxRdfImportAddNewLicensesAs(enum.StrEnum):
    """
    Create new licenses as
    """

    CANDIDATE = "candidate"
    LICENSE = "license"

    def visit(self, candidate: typing.Callable[[], T_Result], license: typing.Callable[[], T_Result]) -> T_Result:
        if self is SpdxRdfImportAddNewLicensesAs.CANDIDATE:
            return candidate()
        if self is SpdxRdfImportAddNewLicensesAs.LICENSE:
            return license()
