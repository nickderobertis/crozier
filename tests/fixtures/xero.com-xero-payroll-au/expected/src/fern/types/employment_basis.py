

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EmploymentBasis(str, enum.Enum):
    FULLTIME = "FULLTIME"
    PARTTIME = "PARTTIME"
    CASUAL = "CASUAL"
    LABOURHIRE = "LABOURHIRE"
    SUPERINCOMESTREAM = "SUPERINCOMESTREAM"

    def visit(
        self,
        fulltime: typing.Callable[[], T_Result],
        parttime: typing.Callable[[], T_Result],
        casual: typing.Callable[[], T_Result],
        labourhire: typing.Callable[[], T_Result],
        superincomestream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EmploymentBasis.FULLTIME:
            return fulltime()
        if self is EmploymentBasis.PARTTIME:
            return parttime()
        if self is EmploymentBasis.CASUAL:
            return casual()
        if self is EmploymentBasis.LABOURHIRE:
            return labourhire()
        if self is EmploymentBasis.SUPERINCOMESTREAM:
            return superincomestream()
