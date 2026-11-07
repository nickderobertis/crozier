

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LoginStepDisplayAndWaitDisplayAndWaitType(enum.StrEnum):
    """
    The type of thing to display
    """

    QR = "qr"
    EMOJI = "emoji"
    CODE = "code"
    NOTHING = "nothing"

    def visit(
        self,
        qr: typing.Callable[[], T_Result],
        emoji: typing.Callable[[], T_Result],
        code: typing.Callable[[], T_Result],
        nothing: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LoginStepDisplayAndWaitDisplayAndWaitType.QR:
            return qr()
        if self is LoginStepDisplayAndWaitDisplayAndWaitType.EMOJI:
            return emoji()
        if self is LoginStepDisplayAndWaitDisplayAndWaitType.CODE:
            return code()
        if self is LoginStepDisplayAndWaitDisplayAndWaitType.NOTHING:
            return nothing()
