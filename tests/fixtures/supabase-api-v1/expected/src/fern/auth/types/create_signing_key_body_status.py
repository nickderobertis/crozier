

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class CreateSigningKeyBodyStatus(enum.StrEnum):
    IN_USE = "in_use"
    STANDBY = "standby"

    def visit(self, in_use: typing.Callable[[], T_Result], standby: typing.Callable[[], T_Result]) -> T_Result:
        if self is CreateSigningKeyBodyStatus.IN_USE:
            return in_use()
        if self is CreateSigningKeyBodyStatus.STANDBY:
            return standby()
