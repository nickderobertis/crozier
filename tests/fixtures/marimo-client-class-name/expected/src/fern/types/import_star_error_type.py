

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ImportStarErrorType(enum.StrEnum):
    IMPORT_STAR = "import-star"

    def visit(self, import_star: typing.Callable[[], T_Result]) -> T_Result:
        if self is ImportStarErrorType.IMPORT_STAR:
            return import_star()
