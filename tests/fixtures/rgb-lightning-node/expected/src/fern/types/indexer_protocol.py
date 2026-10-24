

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class IndexerProtocol(enum.StrEnum):
    ELECTRUM = "Electrum"
    ESPLORA = "Esplora"

    def visit(self, electrum: typing.Callable[[], T_Result], esplora: typing.Callable[[], T_Result]) -> T_Result:
        if self is IndexerProtocol.ELECTRUM:
            return electrum()
        if self is IndexerProtocol.ESPLORA:
            return esplora()
