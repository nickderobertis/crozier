

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NarrativeStatus(enum.StrEnum):
    GENERATED = "GENERATED"
    EXTENSIONS = "EXTENSIONS"
    ADDITIONAL = "ADDITIONAL"
    EMPTY = "EMPTY"
    NULL = "NULL"

    def visit(
        self,
        generated: typing.Callable[[], T_Result],
        extensions: typing.Callable[[], T_Result],
        additional: typing.Callable[[], T_Result],
        empty: typing.Callable[[], T_Result],
        null: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NarrativeStatus.GENERATED:
            return generated()
        if self is NarrativeStatus.EXTENSIONS:
            return extensions()
        if self is NarrativeStatus.ADDITIONAL:
            return additional()
        if self is NarrativeStatus.EMPTY:
            return empty()
        if self is NarrativeStatus.NULL:
            return null()
