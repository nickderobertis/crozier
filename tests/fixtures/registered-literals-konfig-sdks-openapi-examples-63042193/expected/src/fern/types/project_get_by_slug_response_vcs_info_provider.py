

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ProjectGetBySlugResponseVcsInfoProvider(enum.StrEnum):
    """
    The VCS provider
    """

    BITBUCKET = "Bitbucket"
    CIRCLE_CI = "CircleCI"
    GIT_HUB = "GitHub"

    def visit(
        self,
        bitbucket: typing.Callable[[], T_Result],
        circle_ci: typing.Callable[[], T_Result],
        git_hub: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ProjectGetBySlugResponseVcsInfoProvider.BITBUCKET:
            return bitbucket()
        if self is ProjectGetBySlugResponseVcsInfoProvider.CIRCLE_CI:
            return circle_ci()
        if self is ProjectGetBySlugResponseVcsInfoProvider.GIT_HUB:
            return git_hub()
