

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskRunResponseRunType(enum.StrEnum):
    """
    Types of a task run - task_v1, task_v2, openai_cua, anthropic_cua
    """

    TASK_V1 = "task_v1"
    TASK_V2 = "task_v2"
    OPENAI_CUA = "openai_cua"
    ANTHROPIC_CUA = "anthropic_cua"

    def visit(
        self,
        task_v1: typing.Callable[[], T_Result],
        task_v2: typing.Callable[[], T_Result],
        openai_cua: typing.Callable[[], T_Result],
        anthropic_cua: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskRunResponseRunType.TASK_V1:
            return task_v1()
        if self is TaskRunResponseRunType.TASK_V2:
            return task_v2()
        if self is TaskRunResponseRunType.OPENAI_CUA:
            return openai_cua()
        if self is TaskRunResponseRunType.ANTHROPIC_CUA:
            return anthropic_cua()
