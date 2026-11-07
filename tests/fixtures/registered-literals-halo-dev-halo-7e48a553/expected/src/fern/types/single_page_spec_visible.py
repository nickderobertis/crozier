

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SinglePageSpecVisible(enum.StrEnum):
    """
    Visibility used by theme-side and public REST queries; anonymous clients only receive PUBLIC single pages.
    """

    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"
    PRIVATE = "PRIVATE"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SinglePageSpecVisible.PUBLIC:
            return public()
        if self is SinglePageSpecVisible.INTERNAL:
            return internal()
        if self is SinglePageSpecVisible.PRIVATE:
            return private()
