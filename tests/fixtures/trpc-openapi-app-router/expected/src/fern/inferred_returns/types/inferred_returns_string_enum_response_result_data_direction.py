

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class InferredReturnsStringEnumResponseResultDataDirection(enum.StrEnum):
    UP = "UP"
    DOWN = "DOWN"
    LEFT = "LEFT"
    RIGHT = "RIGHT"

    def visit(
        self,
        up: typing.Callable[[], T_Result],
        down: typing.Callable[[], T_Result],
        left: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InferredReturnsStringEnumResponseResultDataDirection.UP:
            return up()
        if self is InferredReturnsStringEnumResponseResultDataDirection.DOWN:
            return down()
        if self is InferredReturnsStringEnumResponseResultDataDirection.LEFT:
            return left()
        if self is InferredReturnsStringEnumResponseResultDataDirection.RIGHT:
            return right()
