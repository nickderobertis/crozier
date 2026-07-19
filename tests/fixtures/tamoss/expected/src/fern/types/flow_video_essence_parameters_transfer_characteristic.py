

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class FlowVideoEssenceParametersTransferCharacteristic(enum.StrEnum):
    """
    Transfer characteristic
    """

    SDR = "SDR"
    HLG = "HLG"
    PQ = "PQ"

    def visit(
        self, sdr: typing.Callable[[], T_Result], hlg: typing.Callable[[], T_Result], pq: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is FlowVideoEssenceParametersTransferCharacteristic.SDR:
            return sdr()
        if self is FlowVideoEssenceParametersTransferCharacteristic.HLG:
            return hlg()
        if self is FlowVideoEssenceParametersTransferCharacteristic.PQ:
            return pq()
