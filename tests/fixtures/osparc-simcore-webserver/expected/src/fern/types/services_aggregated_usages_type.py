

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ServicesAggregatedUsagesType(enum.StrEnum):
    SERVICES = "services"

    def visit(self, services: typing.Callable[[], T_Result]) -> T_Result:
        if self is ServicesAggregatedUsagesType.SERVICES:
            return services()
