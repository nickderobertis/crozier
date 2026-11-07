

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ValsCreate2RequestPrivacy(enum.StrEnum):
    PUBLIC = "public"
    UNLISTED = "unlisted"
    PRIVATE = "private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        unlisted: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ValsCreate2RequestPrivacy.PUBLIC:
            return public()
        if self is ValsCreate2RequestPrivacy.UNLISTED:
            return unlisted()
        if self is ValsCreate2RequestPrivacy.PRIVATE:
            return private()
