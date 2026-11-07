

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class RunType(enum.StrEnum):
    TASK_V1 = "task_v1"
    TASK_V2 = "task_v2"
    TASK_V3 = "task_v3"
    WORKFLOW_RUN = "workflow_run"
    OPENAI_CUA = "openai_cua"
    ANTHROPIC_CUA = "anthropic_cua"
    UI_TARS = "ui_tars"
    YUTORI_NAVIGATOR = "yutori_navigator"

    def visit(
        self,
        task_v1: typing.Callable[[], T_Result],
        task_v2: typing.Callable[[], T_Result],
        task_v3: typing.Callable[[], T_Result],
        workflow_run: typing.Callable[[], T_Result],
        openai_cua: typing.Callable[[], T_Result],
        anthropic_cua: typing.Callable[[], T_Result],
        ui_tars: typing.Callable[[], T_Result],
        yutori_navigator: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is RunType.TASK_V1:
            return task_v1()
        if self is RunType.TASK_V2:
            return task_v2()
        if self is RunType.TASK_V3:
            return task_v3()
        if self is RunType.WORKFLOW_RUN:
            return workflow_run()
        if self is RunType.OPENAI_CUA:
            return openai_cua()
        if self is RunType.ANTHROPIC_CUA:
            return anthropic_cua()
        if self is RunType.UI_TARS:
            return ui_tars()
        if self is RunType.YUTORI_NAVIGATOR:
            return yutori_navigator()
