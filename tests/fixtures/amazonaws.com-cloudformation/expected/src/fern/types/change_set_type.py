

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ChangeSetType(str, enum.Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    IMPORT = "IMPORT"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChangeSetType.CREATE:
            return create()
        if self is ChangeSetType.UPDATE:
            return update()
        if self is ChangeSetType.IMPORT:
            return import_()
