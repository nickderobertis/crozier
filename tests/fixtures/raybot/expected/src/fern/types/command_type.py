

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CommandType(enum.StrEnum):
    """
    The type of command
    """

    STOP_MOVEMENT = "STOP_MOVEMENT"
    MOVE_FORWARD = "MOVE_FORWARD"
    MOVE_BACKWARD = "MOVE_BACKWARD"
    MOVE_TO = "MOVE_TO"
    CARGO_OPEN = "CARGO_OPEN"
    CARGO_CLOSE = "CARGO_CLOSE"
    CARGO_LIFT = "CARGO_LIFT"
    CARGO_LOWER = "CARGO_LOWER"
    CARGO_CHECK_QR = "CARGO_CHECK_QR"
    SCAN_LOCATION = "SCAN_LOCATION"
    WAIT = "WAIT"

    def visit(
        self,
        stop_movement: typing.Callable[[], T_Result],
        move_forward: typing.Callable[[], T_Result],
        move_backward: typing.Callable[[], T_Result],
        move_to: typing.Callable[[], T_Result],
        cargo_open: typing.Callable[[], T_Result],
        cargo_close: typing.Callable[[], T_Result],
        cargo_lift: typing.Callable[[], T_Result],
        cargo_lower: typing.Callable[[], T_Result],
        cargo_check_qr: typing.Callable[[], T_Result],
        scan_location: typing.Callable[[], T_Result],
        wait: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is CommandType.STOP_MOVEMENT:
            return stop_movement()
        if self is CommandType.MOVE_FORWARD:
            return move_forward()
        if self is CommandType.MOVE_BACKWARD:
            return move_backward()
        if self is CommandType.MOVE_TO:
            return move_to()
        if self is CommandType.CARGO_OPEN:
            return cargo_open()
        if self is CommandType.CARGO_CLOSE:
            return cargo_close()
        if self is CommandType.CARGO_LIFT:
            return cargo_lift()
        if self is CommandType.CARGO_LOWER:
            return cargo_lower()
        if self is CommandType.CARGO_CHECK_QR:
            return cargo_check_qr()
        if self is CommandType.SCAN_LOCATION:
            return scan_location()
        if self is CommandType.WAIT:
            return wait()
