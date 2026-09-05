

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StudyUiInputMode(enum.StrEnum):
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
        if self is StudyUiInputMode.WORKBENCH:
            return workbench()
        if self is StudyUiInputMode.APP:
            return app()
        if self is StudyUiInputMode.GUIDED:
            return guided()
        if self is StudyUiInputMode.STANDALONE:
            return standalone()
        if self is StudyUiInputMode.PIPELINE:
            return pipeline()
