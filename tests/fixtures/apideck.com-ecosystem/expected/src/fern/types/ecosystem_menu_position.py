

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class EcosystemMenuPosition(str, enum.Enum):
    TOP = "TOP"
    LEFT = "LEFT"
    RIGHT = "RIGHT"
    HIDDEN = "HIDDEN"

    def visit(
        self,
        top: typing.Callable[[], T_Result],
        left: typing.Callable[[], T_Result],
        right: typing.Callable[[], T_Result],
        hidden: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is EcosystemMenuPosition.TOP:
            return top()
        if self is EcosystemMenuPosition.LEFT:
            return left()
        if self is EcosystemMenuPosition.RIGHT:
            return right()
        if self is EcosystemMenuPosition.HIDDEN:
            return hidden()
