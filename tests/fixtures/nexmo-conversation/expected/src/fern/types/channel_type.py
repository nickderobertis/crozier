

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelType(enum.StrEnum):
    """
    Channel type
    """

    APP = "app"
    PHONE = "phone"
    SIP = "sip"
    WEBSOCKET = "websocket"
    VBC = "vbc"

    def visit(
        self,
        app: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        sip: typing.Callable[[], T_Result],
        websocket: typing.Callable[[], T_Result],
        vbc: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelType.APP:
            return app()
        if self is ChannelType.PHONE:
            return phone()
        if self is ChannelType.SIP:
            return sip()
        if self is ChannelType.WEBSOCKET:
            return websocket()
        if self is ChannelType.VBC:
            return vbc()
