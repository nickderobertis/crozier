

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FdxPartyRegistry(enum.StrEnum):
    """
    The registry containing the party’s registration with name and id
    """

    FDX = "FDX"
    GLEIF = "GLEIF"
    ICANN = "ICANN"
    PRIVATE = "PRIVATE"

    def visit(
        self,
        fdx: typing.Callable[[], T_Result],
        gleif: typing.Callable[[], T_Result],
        icann: typing.Callable[[], T_Result],
        private: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is FdxPartyRegistry.FDX:
            return fdx()
        if self is FdxPartyRegistry.GLEIF:
            return gleif()
        if self is FdxPartyRegistry.ICANN:
            return icann()
        if self is FdxPartyRegistry.PRIVATE:
            return private()
