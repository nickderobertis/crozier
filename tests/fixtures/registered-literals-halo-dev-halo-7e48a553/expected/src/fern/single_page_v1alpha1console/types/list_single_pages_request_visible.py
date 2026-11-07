

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ListSinglePagesRequestVisible(enum.StrEnum):
    PUBLIC = "PUBLIC"
    INTERNAL = "INTERNAL"
    PRIVATE = "PRIVATE"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        internal: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListSinglePagesRequestVisible.PUBLIC:
            return public()
        if self is ListSinglePagesRequestVisible.INTERNAL:
            return internal()
        if self is ListSinglePagesRequestVisible.PRIVATE:
            return private()
