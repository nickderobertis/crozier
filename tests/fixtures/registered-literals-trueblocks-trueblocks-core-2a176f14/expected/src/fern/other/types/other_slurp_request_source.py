

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class OtherSlurpRequestSource(enum.StrEnum):
    ETHERSCAN = "etherscan"
    COVALENT = "covalent"
    ALCHEMY = "alchemy"

    def visit(
        self,
        etherscan: typing.Callable[[], T_Result],
        covalent: typing.Callable[[], T_Result],
        alchemy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is OtherSlurpRequestSource.ETHERSCAN:
            return etherscan()
        if self is OtherSlurpRequestSource.COVALENT:
            return covalent()
        if self is OtherSlurpRequestSource.ALCHEMY:
            return alchemy()
