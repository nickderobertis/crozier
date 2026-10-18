

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdOne(enum.StrEnum):
    CD_DEFAULT = "cd_default"

    def visit(self, cd_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputSelectedAddonsItemVariantIdOne.CD_DEFAULT:
            return cd_default()
