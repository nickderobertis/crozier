

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChangeAction(str, enum.Enum):
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
        if self is ChangeAction.ADD:
            return add()
        if self is ChangeAction.MODIFY:
            return modify()
        if self is ChangeAction.REMOVE:
            return remove()
        if self is ChangeAction.IMPORT:
            return import_()
        if self is ChangeAction.DYNAMIC:
            return dynamic()
