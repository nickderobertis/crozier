

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TemporalSampler(enum.StrEnum):
    """
    Describes how a date-set should be sampled to reduce it to a single day. - EARLIEST is the first day of the sets span - LATEST is the last day of the sets span - RANDOM samples is a single random day within the set.
    """

    EARLIEST = "EARLIEST"
    LATEST = "LATEST"
    RANDOM = "RANDOM"

    def visit(
        self,
        earliest: typing.Callable[[], T_Result],
        latest: typing.Callable[[], T_Result],
        random: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TemporalSampler.EARLIEST:
            return earliest()
        if self is TemporalSampler.LATEST:
            return latest()
        if self is TemporalSampler.RANDOM:
            return random()
