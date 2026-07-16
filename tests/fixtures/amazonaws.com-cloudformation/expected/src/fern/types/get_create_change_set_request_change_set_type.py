

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class GetCreateChangeSetRequestChangeSetType(str, enum.Enum):
    CREATE = "CREATE"
    UPDATE = "UPDATE"
    IMPORT = "IMPORT"

    def visit(
        self,
        create: typing.Callable[[], T_Result],
        update: typing.Callable[[], T_Result],
        import_: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetCreateChangeSetRequestChangeSetType.CREATE:
            return create()
        if self is GetCreateChangeSetRequestChangeSetType.UPDATE:
            return update()
        if self is GetCreateChangeSetRequestChangeSetType.IMPORT:
            return import_()
