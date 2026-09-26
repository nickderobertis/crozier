

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GameRecordVisibility(enum.StrEnum):
    PRIVATE = "private"
    UNLISTED = "unlisted"
    PUBLIC = "public"

    def visit(
        self,
        private: typing.Callable[[], T_Result],
        unlisted: typing.Callable[[], T_Result],
        public: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GameRecordVisibility.PRIVATE:
            return private()
        if self is GameRecordVisibility.UNLISTED:
            return unlisted()
        if self is GameRecordVisibility.PUBLIC:
            return public()
