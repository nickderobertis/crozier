

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class LocationFilter(enum.StrEnum):
    TAI = "TAI"
    CELL_ID = "CELL_ID"
    N3IWF = "N3IWF"
    UE_IP = "UE_IP"
    UDP_PORT = "UDP_PORT"

    def visit(
        self,
        tai: typing.Callable[[], T_Result],
        cell_id: typing.Callable[[], T_Result],
        n3iwf: typing.Callable[[], T_Result],
        ue_ip: typing.Callable[[], T_Result],
        udp_port: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is LocationFilter.TAI:
            return tai()
        if self is LocationFilter.CELL_ID:
            return cell_id()
        if self is LocationFilter.N3IWF:
            return n3iwf()
        if self is LocationFilter.UE_IP:
            return ue_ip()
        if self is LocationFilter.UDP_PORT:
            return udp_port()
