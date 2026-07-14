

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class InterfaceType(str, enum.Enum):
    """
    Type of interface.
    """

    TUNNEL = "TUNNEL"
    MAC = "MAC"
    IP = "IP"

    def visit(
        self,
        tunnel: typing.Callable[[], T_Result],
        mac: typing.Callable[[], T_Result],
        ip: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceType.TUNNEL:
            return tunnel()
        if self is InterfaceType.MAC:
            return mac()
        if self is InterfaceType.IP:
            return ip()
