

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AppConfigStartingView(enum.StrEnum):
    """
    Initial view
    """

    HOME = "home"
    DEFAULT = "default"
    MINIMAL = "minimal"
    WORKSPACE = "workspace"

    def visit(
        self,
        home: typing.Callable[[], T_Result],
        default: typing.Callable[[], T_Result],
        minimal: typing.Callable[[], T_Result],
        workspace: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AppConfigStartingView.HOME:
            return home()
        if self is AppConfigStartingView.DEFAULT:
            return default()
        if self is AppConfigStartingView.MINIMAL:
            return minimal()
        if self is AppConfigStartingView.WORKSPACE:
            return workspace()
