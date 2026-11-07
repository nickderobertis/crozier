

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class UnliWithoutApplicationnkApplicationRequestProvider(enum.StrEnum):
    MESSENGER = "messenger"
    VIBER_SERVICE_MSG = "viber_service_msg"
    WHATSAPP = "whatsapp"

    def visit(
        self,
        messenger: typing.Callable[[], T_Result],
        viber_service_msg: typing.Callable[[], T_Result],
        whatsapp: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UnliWithoutApplicationnkApplicationRequestProvider.MESSENGER:
            return messenger()
        if self is UnliWithoutApplicationnkApplicationRequestProvider.VIBER_SERVICE_MSG:
            return viber_service_msg()
        if self is UnliWithoutApplicationnkApplicationRequestProvider.WHATSAPP:
            return whatsapp()
