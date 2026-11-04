

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ChaindataBlocksRequestFlow(enum.StrEnum):
    FROM = "from"
    TO = "to"
    REWARD = "reward"

    def visit(
        self,
        from_: typing.Callable[[], T_Result],
        to: typing.Callable[[], T_Result],
        reward: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChaindataBlocksRequestFlow.FROM:
            return from_()
        if self is ChaindataBlocksRequestFlow.TO:
            return to()
        if self is ChaindataBlocksRequestFlow.REWARD:
            return reward()
