

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchGroupsIdRequestPrivacy(enum.StrEnum):
    PUBLIC = "Public"
    UNLISTED = "Unlisted"
    PRIVATE = "Private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        unlisted: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PatchGroupsIdRequestPrivacy.PUBLIC:
            return public()
        if self is PatchGroupsIdRequestPrivacy.UNLISTED:
            return unlisted()
        if self is PatchGroupsIdRequestPrivacy.PRIVATE:
            return private()
