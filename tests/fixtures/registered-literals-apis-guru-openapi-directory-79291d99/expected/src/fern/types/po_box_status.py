

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PoBoxStatus(enum.StrEnum):
    """
    Field describing whether the associated address is a post office box. Will be `yes` when a P.O. box is detected, `no` when Plaid confirmed the address is not a P.O. box, and `no_data` when Plaid was not able to determine if the address is a P.O. box.
    """

    YES = "yes"
    NO = "no"
    NO_DATA = "no_data"

    def visit(
        self,
        yes: typing.Callable[[], T_Result],
        no: typing.Callable[[], T_Result],
        no_data: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PoBoxStatus.YES:
            return yes()
        if self is PoBoxStatus.NO:
            return no()
        if self is PoBoxStatus.NO_DATA:
            return no_data()
