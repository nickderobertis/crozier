

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateIndex(enum.StrEnum):
    """
    Índice utilizado na atualização do prêmio e do capital segurado, caso critério de atualização por meio de índice:
    1. IPCA (IBGE);
    2. IGP-M (FGV);
    3. INPC (IBGE).
    """

    IPCA = "IPCA"
    IGP_M = "IGP_M"
    INPC = "INPC"

    def visit(
        self,
        ipca: typing.Callable[[], T_Result],
        igp_m: typing.Callable[[], T_Result],
        inpc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateIndex.IPCA:
            return ipca()
        if self is UpdateIndex.IGP_M:
            return igp_m()
        if self is UpdateIndex.INPC:
            return inpc()
