

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class StoreConfigType(enum.StrEnum):
    FILE = "file"
    REDIS = "redis"
    REST = "rest"
    TIERED = "tiered"

    def visit(
        self,
        file: typing.Callable[[], T_Result],
        redis: typing.Callable[[], T_Result],
        rest: typing.Callable[[], T_Result],
        tiered: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StoreConfigType.FILE:
            return file()
        if self is StoreConfigType.REDIS:
            return redis()
        if self is StoreConfigType.REST:
            return rest()
        if self is StoreConfigType.TIERED:
            return tiered()
