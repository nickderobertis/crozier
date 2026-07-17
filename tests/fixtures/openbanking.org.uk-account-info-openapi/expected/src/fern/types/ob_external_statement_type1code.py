

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ObExternalStatementType1Code(enum.StrEnum):
    """
    Statement type, in a coded form.
    """

    ACCOUNT_CLOSURE = "AccountClosure"
    ACCOUNT_OPENING = "AccountOpening"
    ANNUAL = "Annual"
    INTERIM = "Interim"
    REGULAR_PERIODIC = "RegularPeriodic"

    def visit(
        self,
        account_closure: typing.Callable[[], T_Result],
        account_opening: typing.Callable[[], T_Result],
        annual: typing.Callable[[], T_Result],
        interim: typing.Callable[[], T_Result],
        regular_periodic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ObExternalStatementType1Code.ACCOUNT_CLOSURE:
            return account_closure()
        if self is ObExternalStatementType1Code.ACCOUNT_OPENING:
            return account_opening()
        if self is ObExternalStatementType1Code.ANNUAL:
            return annual()
        if self is ObExternalStatementType1Code.INTERIM:
            return interim()
        if self is ObExternalStatementType1Code.REGULAR_PERIODIC:
            return regular_periodic()
