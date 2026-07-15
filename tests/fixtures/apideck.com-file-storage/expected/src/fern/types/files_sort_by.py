

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class FilesSortBy(str, enum.Enum):
    """
    The field on which to sort the Files
    """

    UPDATED_AT = "updated_at"
    NAME = "name"

    def visit(self, updated_at: typing.Callable[[], T_Result], name: typing.Callable[[], T_Result]) -> T_Result:
        if self is FilesSortBy.UPDATED_AT:
            return updated_at()
        if self is FilesSortBy.NAME:
            return name()
