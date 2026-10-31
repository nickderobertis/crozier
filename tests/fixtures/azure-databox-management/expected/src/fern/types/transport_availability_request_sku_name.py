

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TransportAvailabilityRequestSkuName(enum.StrEnum):
    """
    Type of the device.
    """

    DATA_BOX = "DataBox"
    DATA_BOX_DISK = "DataBoxDisk"
    DATA_BOX_HEAVY = "DataBoxHeavy"

    def visit(
        self,
        data_box: typing.Callable[[], T_Result],
        data_box_disk: typing.Callable[[], T_Result],
        data_box_heavy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TransportAvailabilityRequestSkuName.DATA_BOX:
            return data_box()
        if self is TransportAvailabilityRequestSkuName.DATA_BOX_DISK:
            return data_box_disk()
        if self is TransportAvailabilityRequestSkuName.DATA_BOX_HEAVY:
            return data_box_heavy()
