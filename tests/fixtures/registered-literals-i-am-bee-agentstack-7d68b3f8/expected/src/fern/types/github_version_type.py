

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class GithubVersionType(enum.StrEnum):
    HEAD = "head"
    TAG = "tag"

    def visit(self, head: typing.Callable[[], T_Result], tag: typing.Callable[[], T_Result]) -> T_Result:
        if self is GithubVersionType.HEAD:
            return head()
        if self is GithubVersionType.TAG:
            return tag()
