

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StatusResponseDataState(enum.StrEnum):
    """
    Latest state of the device
    """

    IDLE = "IDLE"
    SELECTING_TIP = "SELECTING_TIP"
    WAITING_FOR_CARD = "WAITING_FOR_CARD"
    WAITING_FOR_PIN = "WAITING_FOR_PIN"
    WAITING_FOR_SIGNATURE = "WAITING_FOR_SIGNATURE"
    UPDATING_FIRMWARE = "UPDATING_FIRMWARE"

    def visit(
        self,
        idle: typing.Callable[[], T_Result],
        selecting_tip: typing.Callable[[], T_Result],
        waiting_for_card: typing.Callable[[], T_Result],
        waiting_for_pin: typing.Callable[[], T_Result],
        waiting_for_signature: typing.Callable[[], T_Result],
        updating_firmware: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StatusResponseDataState.IDLE:
            return idle()
        if self is StatusResponseDataState.SELECTING_TIP:
            return selecting_tip()
        if self is StatusResponseDataState.WAITING_FOR_CARD:
            return waiting_for_card()
        if self is StatusResponseDataState.WAITING_FOR_PIN:
            return waiting_for_pin()
        if self is StatusResponseDataState.WAITING_FOR_SIGNATURE:
            return waiting_for_signature()
        if self is StatusResponseDataState.UPDATING_FIRMWARE:
            return updating_firmware()
