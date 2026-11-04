

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostSpecVisible(enum.StrEnum):
    """
    Visibility used by theme-side and public REST queries; anonymous clients only receive PUBLIC posts.
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
        if self is PostSpecVisible.PUBLIC:
            return public()
        if self is PostSpecVisible.INTERNAL:
            return internal()
        if self is PostSpecVisible.PRIVATE:
            return private()
