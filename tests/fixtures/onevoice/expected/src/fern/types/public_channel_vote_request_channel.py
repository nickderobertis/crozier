

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PublicChannelVoteRequestChannel(enum.StrEnum):
    WHATSAPP = "whatsapp"
    AVITO = "avito"
    TWO_GIS = "2gis"
    OTHER = "other"

    def visit(
        self,
        whatsapp: typing.Callable[[], T_Result],
        avito: typing.Callable[[], T_Result],
        two_gis: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PublicChannelVoteRequestChannel.WHATSAPP:
            return whatsapp()
        if self is PublicChannelVoteRequestChannel.AVITO:
            return avito()
        if self is PublicChannelVoteRequestChannel.TWO_GIS:
            return two_gis()
        if self is PublicChannelVoteRequestChannel.OTHER:
            return other()
