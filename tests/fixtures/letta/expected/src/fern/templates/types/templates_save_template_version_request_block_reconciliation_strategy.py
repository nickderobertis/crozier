

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy(enum.StrEnum):
    """
    Strategy for reconciling memory blocks during migration: "reconcile-all" deletes blocks not in the template, "preserve-deleted" keeps them. Defaults to "preserve-deleted".
    """

    RECONCILE_ALL = "reconcile-all"
    PRESERVE_DELETED = "preserve-deleted"

    def visit(
        self, reconcile_all: typing.Callable[[], T_Result], preserve_deleted: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy.RECONCILE_ALL:
            return reconcile_all()
        if self is TemplatesSaveTemplateVersionRequestBlockReconciliationStrategy.PRESERVE_DELETED:
            return preserve_deleted()
