

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ChannelRequestChannel(enum.StrEnum):
    """
    A not-yet-supported channel a business is expressing demand for.
    Backs a fake-door affordance so pull is measured before the channel
    is built.
    """

    AVITO = "avito"
    WILDBERRIES = "wildberries"
    OZON = "ozon"
    TWO_GIS = "2gis"
    OTHER = "other"

    def visit(
        self,
        avito: typing.Callable[[], T_Result],
        wildberries: typing.Callable[[], T_Result],
        ozon: typing.Callable[[], T_Result],
        two_gis: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ChannelRequestChannel.AVITO:
            return avito()
        if self is ChannelRequestChannel.WILDBERRIES:
            return wildberries()
        if self is ChannelRequestChannel.OZON:
            return ozon()
        if self is ChannelRequestChannel.TWO_GIS:
            return two_gis()
        if self is ChannelRequestChannel.OTHER:
            return other()
