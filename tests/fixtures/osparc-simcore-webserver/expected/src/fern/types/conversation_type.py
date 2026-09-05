

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ConversationType(enum.StrEnum):
    PROJECT_STATIC = "PROJECT_STATIC"
    PROJECT_ANNOTATION = "PROJECT_ANNOTATION"
    SUPPORT = "SUPPORT"
    SUPPORT_CALL = "SUPPORT_CALL"

    def visit(
        self,
        project_static: typing.Callable[[], T_Result],
        project_annotation: typing.Callable[[], T_Result],
        support: typing.Callable[[], T_Result],
        support_call: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ConversationType.PROJECT_STATIC:
            return project_static()
        if self is ConversationType.PROJECT_ANNOTATION:
            return project_annotation()
        if self is ConversationType.SUPPORT:
            return support()
        if self is ConversationType.SUPPORT_CALL:
            return support_call()
