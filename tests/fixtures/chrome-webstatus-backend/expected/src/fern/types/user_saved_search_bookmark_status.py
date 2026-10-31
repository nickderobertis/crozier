

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserSavedSearchBookmarkStatus(enum.StrEnum):
    """
    The bookmark status for a saved search for a user.
    """

    BOOKMARK_NONE = "bookmark_none"
    BOOKMARK_ACTIVE = "bookmark_active"

    def visit(
        self, bookmark_none: typing.Callable[[], T_Result], bookmark_active: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is UserSavedSearchBookmarkStatus.BOOKMARK_NONE:
            return bookmark_none()
        if self is UserSavedSearchBookmarkStatus.BOOKMARK_ACTIVE:
            return bookmark_active()
