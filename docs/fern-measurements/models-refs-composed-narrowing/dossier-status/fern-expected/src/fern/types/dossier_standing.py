

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DossierStanding(enum.StrEnum):
    """
    A filed dossier is never a draft.
    """

    DRAFT = "draft"
    SEALED = "sealed"

    def visit(self, draft: typing.Callable[[], T_Result], sealed: typing.Callable[[], T_Result]) -> T_Result:
        if self is DossierStanding.DRAFT:
            return draft()
        if self is DossierStanding.SEALED:
            return sealed()
