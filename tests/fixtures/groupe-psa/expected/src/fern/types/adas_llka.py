

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AdasLlka(enum.StrEnum):
    """
    Left Lane Keeping Assist
    """

    AUTHORIZED = "Authorized"
    CORRECTION_IN_PROGRESS = "CorrectionInProgress"
    NOT_AUTHORIZED = "NotAuthorized"
    NOT_SELECTED = "NotSelected"

    def visit(
        self,
        authorized: typing.Callable[[], T_Result],
        correction_in_progress: typing.Callable[[], T_Result],
        not_authorized: typing.Callable[[], T_Result],
        not_selected: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is AdasLlka.AUTHORIZED:
            return authorized()
        if self is AdasLlka.CORRECTION_IN_PROGRESS:
            return correction_in_progress()
        if self is AdasLlka.NOT_AUTHORIZED:
            return not_authorized()
        if self is AdasLlka.NOT_SELECTED:
            return not_selected()
