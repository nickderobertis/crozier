

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IssueSource(enum.StrEnum):
    JIRA = "jira"
    GITHUB = "github"
    LAUNCHPAD = "launchpad"

    def visit(
        self,
        jira: typing.Callable[[], T_Result],
        github: typing.Callable[[], T_Result],
        launchpad: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IssueSource.JIRA:
            return jira()
        if self is IssueSource.GITHUB:
            return github()
        if self is IssueSource.LAUNCHPAD:
            return launchpad()
