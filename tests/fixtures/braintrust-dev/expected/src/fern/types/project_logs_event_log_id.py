

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectLogsEventLogId(enum.StrEnum):
    """
    A literal 'g' which identifies the log as a project log
    """

    G = "g"

    def visit(self, g: typing.Callable[[], T_Result]) -> T_Result:
        if self is ProjectLogsEventLogId.G:
            return g()
