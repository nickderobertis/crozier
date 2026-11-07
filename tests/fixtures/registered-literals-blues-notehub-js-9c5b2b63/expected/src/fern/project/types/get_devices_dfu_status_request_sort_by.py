

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class GetDevicesDfuStatusRequestSortBy(enum.StrEnum):
    BEST_ID = "best_id"
    DEVICE_SERIAL = "device_serial"
    DEVICE_UID = "device_uid"
    CAPTURED = "captured"
    MODIFIED = "modified"
    DEVICE_LOCATION = "device_location"
    TOWER_LOCATION = "tower_location"
    TRIANGULATED_LOCATION = "triangulated_location"
    BEST_LOCATION = "best_location"

    def visit(
        self,
        best_id: typing.Callable[[], T_Result],
        device_serial: typing.Callable[[], T_Result],
        device_uid: typing.Callable[[], T_Result],
        captured: typing.Callable[[], T_Result],
        modified: typing.Callable[[], T_Result],
        device_location: typing.Callable[[], T_Result],
        tower_location: typing.Callable[[], T_Result],
        triangulated_location: typing.Callable[[], T_Result],
        best_location: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is GetDevicesDfuStatusRequestSortBy.BEST_ID:
            return best_id()
        if self is GetDevicesDfuStatusRequestSortBy.DEVICE_SERIAL:
            return device_serial()
        if self is GetDevicesDfuStatusRequestSortBy.DEVICE_UID:
            return device_uid()
        if self is GetDevicesDfuStatusRequestSortBy.CAPTURED:
            return captured()
        if self is GetDevicesDfuStatusRequestSortBy.MODIFIED:
            return modified()
        if self is GetDevicesDfuStatusRequestSortBy.DEVICE_LOCATION:
            return device_location()
        if self is GetDevicesDfuStatusRequestSortBy.TOWER_LOCATION:
            return tower_location()
        if self is GetDevicesDfuStatusRequestSortBy.TRIANGULATED_LOCATION:
            return triangulated_location()
        if self is GetDevicesDfuStatusRequestSortBy.BEST_LOCATION:
            return best_location()
