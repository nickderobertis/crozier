

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ReaderDeviceModel(enum.StrEnum):
    """
    Identifier of the model of the device.
    """

    SOLO = "solo"
    VIRTUAL_SOLO = "virtual-solo"

    def visit(self, solo: typing.Callable[[], T_Result], virtual_solo: typing.Callable[[], T_Result]) -> T_Result:
        if self is ReaderDeviceModel.SOLO:
            return solo()
        if self is ReaderDeviceModel.VIRTUAL_SOLO:
            return virtual_solo()
