

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class ListImagesRequestImageStatus(str, enum.Enum):
    ALL = "all"
    ACTIVE = "active"
    DELETING = "deleting"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        active: typing.Callable[[], T_Result],
        deleting: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListImagesRequestImageStatus.ALL:
            return all_()
        if self is ListImagesRequestImageStatus.ACTIVE:
            return active()
        if self is ListImagesRequestImageStatus.DELETING:
            return deleting()
