

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IpsecCryptoProfilesDhGroup(enum.StrEnum):
    """
    phase-2 DH group (PFS DH group)
    """

    NO_PFS = "no-pfs"
    GROUP1 = "group1"
    GROUP2 = "group2"
    GROUP5 = "group5"
    GROUP14 = "group14"
    GROUP19 = "group19"
    GROUP20 = "group20"

    def visit(
        self,
        no_pfs: typing.Callable[[], T_Result],
        group1: typing.Callable[[], T_Result],
        group2: typing.Callable[[], T_Result],
        group5: typing.Callable[[], T_Result],
        group14: typing.Callable[[], T_Result],
        group19: typing.Callable[[], T_Result],
        group20: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IpsecCryptoProfilesDhGroup.NO_PFS:
            return no_pfs()
        if self is IpsecCryptoProfilesDhGroup.GROUP1:
            return group1()
        if self is IpsecCryptoProfilesDhGroup.GROUP2:
            return group2()
        if self is IpsecCryptoProfilesDhGroup.GROUP5:
            return group5()
        if self is IpsecCryptoProfilesDhGroup.GROUP14:
            return group14()
        if self is IpsecCryptoProfilesDhGroup.GROUP19:
            return group19()
        if self is IpsecCryptoProfilesDhGroup.GROUP20:
            return group20()
