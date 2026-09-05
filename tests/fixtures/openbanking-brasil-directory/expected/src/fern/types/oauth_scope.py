

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class OauthScope(enum.StrEnum):
    DIRECTORY_WEBSITE = "directory:website"
    """
    Web based operations
    """

    def visit(self, directory_website: typing.Callable[[], T_Result]) -> T_Result:
        if self is OauthScope.DIRECTORY_WEBSITE:
            return directory_website()
