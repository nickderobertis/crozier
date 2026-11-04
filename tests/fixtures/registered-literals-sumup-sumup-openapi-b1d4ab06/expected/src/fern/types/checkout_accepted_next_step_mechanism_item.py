

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CheckoutAcceptedNextStepMechanismItem(enum.StrEnum):
    IFRAME = "iframe"
    BROWSER = "browser"

    def visit(self, iframe: typing.Callable[[], T_Result], browser: typing.Callable[[], T_Result]) -> T_Result:
        if self is CheckoutAcceptedNextStepMechanismItem.IFRAME:
            return iframe()
        if self is CheckoutAcceptedNextStepMechanismItem.BROWSER:
            return browser()
