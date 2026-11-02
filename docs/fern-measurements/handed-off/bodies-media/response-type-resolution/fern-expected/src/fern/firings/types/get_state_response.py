

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetStateResponse(enum.StrEnum):
    HEATING = "heating"
    HOLDING = "holding"
    COOLING = "cooling"

    def visit(
        self,
        heating: typing.Callable[[], T_Result],
        holding: typing.Callable[[], T_Result],
        cooling: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetStateResponse.HEATING:
            return heating()
        if self is GetStateResponse.HOLDING:
            return holding()
        if self is GetStateResponse.COOLING:
            return cooling()
