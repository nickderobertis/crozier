

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FeedbackExperimentItemSource(enum.StrEnum):
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
        if self is FeedbackExperimentItemSource.APP:
            return app()
        if self is FeedbackExperimentItemSource.API:
            return api()
        if self is FeedbackExperimentItemSource.EXTERNAL:
            return external()
