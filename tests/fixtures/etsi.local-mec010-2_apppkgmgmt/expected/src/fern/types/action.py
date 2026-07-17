

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Action(enum.StrEnum):
    """
    'Identifies the action of the MEC host data plane, when a packet matches the trafficFilter.'
    """

    DROP = "DROP"
    FORWARD_DECAPSULATED = "FORWARD_DECAPSULATED"
    FORWARD_AS_IS = "FORWARD_AS_IS"
    PASSTHROUGH = "PASSTHROUGH"
    DUPLICATED_DECAPSULATED = "DUPLICATED_DECAPSULATED"
    DUPLICATE_AS_IS = "DUPLICATE_AS_IS"

    def visit(
        self,
        drop: typing.Callable[[], T_Result],
        forward_decapsulated: typing.Callable[[], T_Result],
        forward_as_is: typing.Callable[[], T_Result],
        passthrough: typing.Callable[[], T_Result],
        duplicated_decapsulated: typing.Callable[[], T_Result],
        duplicate_as_is: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Action.DROP:
            return drop()
        if self is Action.FORWARD_DECAPSULATED:
            return forward_decapsulated()
        if self is Action.FORWARD_AS_IS:
            return forward_as_is()
        if self is Action.PASSTHROUGH:
            return passthrough()
        if self is Action.DUPLICATED_DECAPSULATED:
            return duplicated_decapsulated()
        if self is Action.DUPLICATE_AS_IS:
            return duplicate_as_is()
