

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IkeCryptoProfilesDhGroupItem(enum.StrEnum):
    """
    Phase-1 DH group
    """

    GROUP1 = "group1"
    GROUP2 = "group2"
    GROUP5 = "group5"
    GROUP14 = "group14"
    GROUP19 = "group19"
    GROUP20 = "group20"

    def visit(
        self,
        group1: typing.Callable[[], T_Result],
        group2: typing.Callable[[], T_Result],
        group5: typing.Callable[[], T_Result],
        group14: typing.Callable[[], T_Result],
        group19: typing.Callable[[], T_Result],
        group20: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is IkeCryptoProfilesDhGroupItem.GROUP1:
            return group1()
        if self is IkeCryptoProfilesDhGroupItem.GROUP2:
            return group2()
        if self is IkeCryptoProfilesDhGroupItem.GROUP5:
            return group5()
        if self is IkeCryptoProfilesDhGroupItem.GROUP14:
            return group14()
        if self is IkeCryptoProfilesDhGroupItem.GROUP19:
            return group19()
        if self is IkeCryptoProfilesDhGroupItem.GROUP20:
            return group20()
