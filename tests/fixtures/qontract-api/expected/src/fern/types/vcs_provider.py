

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VcsProvider(enum.StrEnum):
    """
    VCS provider types.
    """

    GITHUB = "github"
    GITLAB = "gitlab"

    def visit(self, github: typing.Callable[[], T_Result], gitlab: typing.Callable[[], T_Result]) -> T_Result:
        if self is VcsProvider.GITHUB:
            return github()
        if self is VcsProvider.GITLAB:
            return gitlab()
