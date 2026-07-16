

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction(enum.StrEnum):
    """
    Specifies the action of the resource.
    """

    ADD = "Add"
    MODIFY = "Modify"
    REMOVE = "Remove"
    IMPORT = "Import"
    DYNAMIC = "Dynamic"

    def visit(
        self,
        add: typing.Callable[[], T_Result],
        modify: typing.Callable[[], T_Result],
        remove: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
        dynamic: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction.ADD:
            return add()
        if self is ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction.MODIFY:
            return modify()
        if self is ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction.REMOVE:
            return remove()
        if self is ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction.IMPORT:
            return import_()
        if self is ChangeSetHookTargetDetailsResourceTargetDetailsResourceAction.DYNAMIC:
            return dynamic()
