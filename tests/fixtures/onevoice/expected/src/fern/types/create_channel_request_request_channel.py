

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class CreateChannelRequestRequestChannel(enum.StrEnum):
    """
    A not-yet-supported channel a business is expressing demand for.
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
        if self is CreateChannelRequestRequestChannel.AVITO:
            return avito()
        if self is CreateChannelRequestRequestChannel.WILDBERRIES:
            return wildberries()
        if self is CreateChannelRequestRequestChannel.OZON:
            return ozon()
        if self is CreateChannelRequestRequestChannel.TWO_GIS:
            return two_gis()
        if self is CreateChannelRequestRequestChannel.OTHER:
            return other()
