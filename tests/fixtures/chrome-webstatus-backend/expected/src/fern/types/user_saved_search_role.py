

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UserSavedSearchRole(enum.StrEnum):
    SAVED_SEARCH_OWNER = "saved_search_owner"

    def visit(self, saved_search_owner: typing.Callable[[], T_Result]) -> T_Result:
        if self is UserSavedSearchRole.SAVED_SEARCH_OWNER:
            return saved_search_owner()
