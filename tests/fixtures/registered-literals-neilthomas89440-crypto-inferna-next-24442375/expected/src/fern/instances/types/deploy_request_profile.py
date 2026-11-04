

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DeployRequestProfile(enum.StrEnum):
    LATENCY = "latency"
    THROUGHPUT = "throughput"

    def visit(self, latency: typing.Callable[[], T_Result], throughput: typing.Callable[[], T_Result]) -> T_Result:
        if self is DeployRequestProfile.LATENCY:
            return latency()
        if self is DeployRequestProfile.THROUGHPUT:
            return throughput()
