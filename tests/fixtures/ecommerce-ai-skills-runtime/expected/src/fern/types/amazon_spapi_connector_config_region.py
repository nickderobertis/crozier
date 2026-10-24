

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class AmazonSpapiConnectorConfigRegion(enum.StrEnum):
    NA = "na"
    EU = "eu"
    FE = "fe"

    def visit(
        self, na: typing.Callable[[], T_Result], eu: typing.Callable[[], T_Result], fe: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is AmazonSpapiConnectorConfigRegion.NA:
            return na()
        if self is AmazonSpapiConnectorConfigRegion.EU:
            return eu()
        if self is AmazonSpapiConnectorConfigRegion.FE:
            return fe()
