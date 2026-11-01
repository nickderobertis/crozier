

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ComplexTypesNativeEnumResponseResultDataDirection(enum.StrEnum):
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
        if self is ComplexTypesNativeEnumResponseResultDataDirection.UP:
            return up()
        if self is ComplexTypesNativeEnumResponseResultDataDirection.DOWN:
            return down()
        if self is ComplexTypesNativeEnumResponseResultDataDirection.LEFT:
            return left()
        if self is ComplexTypesNativeEnumResponseResultDataDirection.RIGHT:
            return right()
