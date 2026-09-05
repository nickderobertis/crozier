

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PostGroupsRequestPrivacy(enum.StrEnum):
    PUBLIC = "Public"
    UNLISTED = "Unlisted"
    PRIVATE = "Private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        unlisted: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PostGroupsRequestPrivacy.PUBLIC:
            return public()
        if self is PostGroupsRequestPrivacy.UNLISTED:
            return unlisted()
        if self is PostGroupsRequestPrivacy.PRIVATE:
            return private()
