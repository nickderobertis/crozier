

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class StudiesArchiveReason(enum.StrEnum):
    """
    The reason for archiving the provided Studies. Accepted reasons may differ based on tenant configuration.
    """

    MADE_IN_ERROR = "Made in error"
    RETIRED = "Retired"
    EXPENDED = "Expended"
    SHIPPED = "Shipped"
    CONTAMINATED = "Contaminated"
    EXPIRED = "Expired"
    MISSING = "Missing"
    OTHER = "Other"

    def visit(
        self,
        made_in_error: typing.Callable[[], T_Result],
        retired: typing.Callable[[], T_Result],
        expended: typing.Callable[[], T_Result],
        shipped: typing.Callable[[], T_Result],
        contaminated: typing.Callable[[], T_Result],
        expired: typing.Callable[[], T_Result],
        missing: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StudiesArchiveReason.MADE_IN_ERROR:
            return made_in_error()
        if self is StudiesArchiveReason.RETIRED:
            return retired()
        if self is StudiesArchiveReason.EXPENDED:
            return expended()
        if self is StudiesArchiveReason.SHIPPED:
            return shipped()
        if self is StudiesArchiveReason.CONTAMINATED:
            return contaminated()
        if self is StudiesArchiveReason.EXPIRED:
            return expired()
        if self is StudiesArchiveReason.MISSING:
            return missing()
        if self is StudiesArchiveReason.OTHER:
            return other()
