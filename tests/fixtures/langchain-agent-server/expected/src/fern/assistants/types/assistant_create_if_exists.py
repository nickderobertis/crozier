

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class AssistantCreateIfExists(enum.StrEnum):
    """
    How to handle duplicate creation. Must be either 'raise' (raise error if duplicate), or 'do_nothing' (return existing assistant).
    """

    RAISE = "raise"
    DO_NOTHING = "do_nothing"

    def visit(self, raise_: typing.Callable[[], T_Result], do_nothing: typing.Callable[[], T_Result]) -> T_Result:
        if self is AssistantCreateIfExists.RAISE:
            return raise_()
        if self is AssistantCreateIfExists.DO_NOTHING:
            return do_nothing()
