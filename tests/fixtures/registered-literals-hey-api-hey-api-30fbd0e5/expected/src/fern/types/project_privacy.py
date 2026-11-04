

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectPrivacy(enum.StrEnum):
    """
    This resource's privacy setting. Unlisted resources do not appear on profile pages or elsewhere, but you can link to them.
    """

    PUBLIC = "public"
    UNLISTED = "unlisted"
    PRIVATE = "private"

    def visit(
        self,
        public: typing.Callable[[], T_Result],
        unlisted: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectPrivacy.PUBLIC:
            return public()
        if self is ProjectPrivacy.UNLISTED:
            return unlisted()
        if self is ProjectPrivacy.PRIVATE:
            return private()
