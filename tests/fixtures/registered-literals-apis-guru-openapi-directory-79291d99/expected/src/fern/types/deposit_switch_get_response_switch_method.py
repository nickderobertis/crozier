

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DepositSwitchGetResponseSwitchMethod(enum.StrEnum):
    """
    The method used to make the deposit switch.

    - `instant` – User instantly switched their direct deposit to a new or existing bank account by connecting their payroll or employer account.

    - `mail` – User requested that Plaid contact their employer by mail to make the direct deposit switch.

    - `pdf` – User generated a PDF or email to be sent to their employer with the information necessary to make the deposit switch.'
    """

    INSTANT = "instant"
    MAIL = "mail"
    PDF = "pdf"

    def visit(
        self,
        instant: typing.Callable[[], T_Result],
        mail: typing.Callable[[], T_Result],
        pdf: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DepositSwitchGetResponseSwitchMethod.INSTANT:
            return instant()
        if self is DepositSwitchGetResponseSwitchMethod.MAIL:
            return mail()
        if self is DepositSwitchGetResponseSwitchMethod.PDF:
            return pdf()
