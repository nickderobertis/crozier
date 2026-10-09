

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DossierStatus(enum.StrEnum):
    """
    Lifecycle status of a dossier.
    """

    DRAFT = "draft"
    SEALED = "sealed"

    def visit(self, draft: typing.Callable[[], T_Result], sealed: typing.Callable[[], T_Result]) -> T_Result:
        if self is DossierStatus.DRAFT:
            return draft()
        if self is DossierStatus.SEALED:
            return sealed()
