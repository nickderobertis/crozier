

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class NodeValidationErrorType(enum.StrEnum):
    RENDER_NOT_ALLOWED = "RenderNotAllowed"
    SAVE_NOT_ALLOWED = "SaveNotAllowed"
    SAVE_ALLOWED = "SaveAllowed"

    def visit(
        self,
        render_not_allowed: typing.Callable[[], T_Result],
        save_not_allowed: typing.Callable[[], T_Result],
        save_allowed: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is NodeValidationErrorType.RENDER_NOT_ALLOWED:
            return render_not_allowed()
        if self is NodeValidationErrorType.SAVE_NOT_ALLOWED:
            return save_not_allowed()
        if self is NodeValidationErrorType.SAVE_ALLOWED:
            return save_allowed()
