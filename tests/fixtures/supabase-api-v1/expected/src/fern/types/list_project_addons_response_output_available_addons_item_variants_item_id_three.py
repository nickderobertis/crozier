

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdThree(enum.StrEnum):
    IPV4DEFAULT = "ipv4_default"

    def visit(self, ipv4default: typing.Callable[[], T_Result]) -> T_Result:
        if self is ListProjectAddonsResponseOutputAvailableAddonsItemVariantsItemIdThree.IPV4DEFAULT:
            return ipv4default()
