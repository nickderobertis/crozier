

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoanAccountSubtype(enum.StrEnum):
    """
    Valid account subtypes for loan accounts. For a list containing descriptions of each subtype, see [Account schemas](https://plaid.com/docs/api/accounts/#StandaloneAccountType-loan).
    """

    AUTO = "auto"
    BUSINESS = "business"
    COMMERCIAL = "commercial"
    CONSTRUCTION = "construction"
    CONSUMER = "consumer"
    HOME_EQUITY = "home equity"
    LOAN = "loan"
    MORTGAGE = "mortgage"
    LINE_OF_CREDIT = "line of credit"
    STUDENT = "student"
    OTHER = "other"
    ALL = "all"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        business: typing.Callable[[], T_Result],
        commercial: typing.Callable[[], T_Result],
        construction: typing.Callable[[], T_Result],
        consumer: typing.Callable[[], T_Result],
        home_equity: typing.Callable[[], T_Result],
        loan: typing.Callable[[], T_Result],
        mortgage: typing.Callable[[], T_Result],
        line_of_credit: typing.Callable[[], T_Result],
        student: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
        all_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoanAccountSubtype.AUTO:
            return auto()
        if self is LoanAccountSubtype.BUSINESS:
            return business()
        if self is LoanAccountSubtype.COMMERCIAL:
            return commercial()
        if self is LoanAccountSubtype.CONSTRUCTION:
            return construction()
        if self is LoanAccountSubtype.CONSUMER:
            return consumer()
        if self is LoanAccountSubtype.HOME_EQUITY:
            return home_equity()
        if self is LoanAccountSubtype.LOAN:
            return loan()
        if self is LoanAccountSubtype.MORTGAGE:
            return mortgage()
        if self is LoanAccountSubtype.LINE_OF_CREDIT:
            return line_of_credit()
        if self is LoanAccountSubtype.STUDENT:
            return student()
        if self is LoanAccountSubtype.OTHER:
            return other()
        if self is LoanAccountSubtype.ALL:
            return all_()
