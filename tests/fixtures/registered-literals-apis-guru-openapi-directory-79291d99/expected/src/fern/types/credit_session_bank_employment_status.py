

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreditSessionBankEmploymentStatus(enum.StrEnum):
    """
    The terminal status of the bank employment verification.

    `APPROVED`: User has approved and verified their employment.

    `NO_EMPLOYMENTS_FOUND`: We attempted, but were unable to find any employment in the connected account.

    `EMPLOYER_NOT_LISTED`: The user explicitly indicated that they did not see their current or previous employer in the list of employer names found.
    """

    APPROVED = "APPROVED"
    NO_EMPLOYERS_FOUND = "NO_EMPLOYERS_FOUND"
    EMPLOYER_NOT_LISTED = "EMPLOYER_NOT_LISTED"

    def visit(
        self,
        approved: typing.Callable[[], T_Result],
        no_employers_found: typing.Callable[[], T_Result],
        employer_not_listed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CreditSessionBankEmploymentStatus.APPROVED:
            return approved()
        if self is CreditSessionBankEmploymentStatus.NO_EMPLOYERS_FOUND:
            return no_employers_found()
        if self is CreditSessionBankEmploymentStatus.EMPLOYER_NOT_LISTED:
            return employer_not_listed()
