

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StreamTransformTransformType(enum.StrEnum):
    ADD_STREAM = "add_stream"
    REMOVE_STREAM = "remove_stream"
    UPDATE_STREAM = "update_stream"

    def visit(
        self,
        add_stream: typing.Callable[[], T_Result],
        remove_stream: typing.Callable[[], T_Result],
        update_stream: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StreamTransformTransformType.ADD_STREAM:
            return add_stream()
        if self is StreamTransformTransformType.REMOVE_STREAM:
            return remove_stream()
        if self is StreamTransformTransformType.UPDATE_STREAM:
            return update_stream()
