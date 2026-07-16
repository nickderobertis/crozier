

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChangeSetHookResourceTargetDetailsResourceAction(str, enum.Enum):
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
        if self is ChangeSetHookResourceTargetDetailsResourceAction.ADD:
            return add()
        if self is ChangeSetHookResourceTargetDetailsResourceAction.MODIFY:
            return modify()
        if self is ChangeSetHookResourceTargetDetailsResourceAction.REMOVE:
            return remove()
        if self is ChangeSetHookResourceTargetDetailsResourceAction.IMPORT:
            return import_()
        if self is ChangeSetHookResourceTargetDetailsResourceAction.DYNAMIC:
            return dynamic()
