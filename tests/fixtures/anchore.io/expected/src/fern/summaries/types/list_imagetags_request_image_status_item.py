

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListImagetagsRequestImageStatusItem(str, enum.Enum):
    ALL = "all"
    ACTIVE = "active"
    DELETING = "deleting"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListImagetagsRequestImageStatusItem.ALL:
            return all_()
        if self is ListImagetagsRequestImageStatusItem.ACTIVE:
            return active()
        if self is ListImagetagsRequestImageStatusItem.DELETING:
            return deleting()
