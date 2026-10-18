

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdOne(enum.StrEnum):
    CD_DEFAULT = "cd_default"

    def visit(self, cd_default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdOne.CD_DEFAULT:
            return cd_default()
