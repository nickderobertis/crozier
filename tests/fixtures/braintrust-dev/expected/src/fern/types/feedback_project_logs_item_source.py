

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FeedbackProjectLogsItemSource(enum.StrEnum):
    """
    The source of the feedback. Must be one of "external" (default), "app", or "api"
    """

    APP = "app"
    API = "api"
    EXTERNAL = "external"

    def visit(
        self,
        app: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        external: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FeedbackProjectLogsItemSource.APP:
            return app()
        if self is FeedbackProjectLogsItemSource.API:
            return api()
        if self is FeedbackProjectLogsItemSource.EXTERNAL:
            return external()
