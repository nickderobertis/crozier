

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class VcsUploadVcsType(enum.StrEnum):
    """
    VCS type
    """

    SVN = "svn"
    GIT = "git"

    def visit(self, svn: typing.Callable[[], T_Result], git: typing.Callable[[], T_Result]) -> T_Result:
        if self is VcsUploadVcsType.SVN:
            return svn()
        if self is VcsUploadVcsType.GIT:
            return git()
