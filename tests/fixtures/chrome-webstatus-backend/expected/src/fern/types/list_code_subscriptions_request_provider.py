

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListCodeSubscriptionsRequestProvider(enum.StrEnum):
    GITHUB = "github"

    def visit(self, github: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListCodeSubscriptionsRequestProvider.GITHUB:
            return github()
