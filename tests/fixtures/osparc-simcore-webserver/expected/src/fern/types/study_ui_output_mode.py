

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudyUiOutputMode(enum.StrEnum):
    WORKBENCH = "workbench"
    APP = "app"
    GUIDED = "guided"
    STANDALONE = "standalone"
    PIPELINE = "pipeline"

    def visit(
        self,
        workbench: typing.Callable[[], T_Result],
        app: typing.Callable[[], T_Result],
        guided: typing.Callable[[], T_Result],
        standalone: typing.Callable[[], T_Result],
        pipeline: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StudyUiOutputMode.WORKBENCH:
            return workbench()
        if self is StudyUiOutputMode.APP:
            return app()
        if self is StudyUiOutputMode.GUIDED:
            return guided()
        if self is StudyUiOutputMode.STANDALONE:
            return standalone()
        if self is StudyUiOutputMode.PIPELINE:
            return pipeline()
