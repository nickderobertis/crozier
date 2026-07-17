

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InlineTypes(enum.StrEnum):
    """
    Object types to inline under their respective parent object in certain connect v2 responses
    """

    INLINE_NONE = "INLINE_NONE"
    INLINE_VARIATIONS = "INLINE_VARIATIONS"
    INLINE_ALL = "INLINE_ALL"

    def visit(
        self,
        inline_none: typing.Callable[[], T_Result],
        inline_variations: typing.Callable[[], T_Result],
        inline_all: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InlineTypes.INLINE_NONE:
            return inline_none()
        if self is InlineTypes.INLINE_VARIATIONS:
            return inline_variations()
        if self is InlineTypes.INLINE_ALL:
            return inline_all()
