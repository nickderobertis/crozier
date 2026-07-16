

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChangeResourceChangeAction(enum.StrEnum):
    """
    The action that CloudFormation takes on the resource, such as <code>Add</code> (adds a new resource), <code>Modify</code> (changes a resource), <code>Remove</code> (deletes a resource), <code>Import</code> (imports a resource), or <code>Dynamic</code> (exact action for the resource can't be determined).
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
        if self is ChangeResourceChangeAction.ADD:
            return add()
        if self is ChangeResourceChangeAction.MODIFY:
            return modify()
        if self is ChangeResourceChangeAction.REMOVE:
            return remove()
        if self is ChangeResourceChangeAction.IMPORT:
            return import_()
        if self is ChangeResourceChangeAction.DYNAMIC:
            return dynamic()
