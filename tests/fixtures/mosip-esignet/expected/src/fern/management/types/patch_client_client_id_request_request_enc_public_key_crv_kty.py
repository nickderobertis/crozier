

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class PatchClientClientIdRequestRequestEncPublicKeyCrvKty(enum.StrEnum):
    """
    Key type (EC)
    """

    EC = "EC"

    def visit(self, ec: typing.Callable[[], T_Result]) -> T_Result:
        if self is PatchClientClientIdRequestRequestEncPublicKeyCrvKty.EC:
            return ec()
