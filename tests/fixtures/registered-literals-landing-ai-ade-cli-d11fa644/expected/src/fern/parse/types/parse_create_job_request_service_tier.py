

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class ParseCreateJobRequestServiceTier(enum.StrEnum):
    """
    Async service tier (``POST /jobs`` only). ``priority`` runs in the fast lane at the sync billing rate; absent → ``standard``.
    """

    STANDARD = "standard"
    PRIORITY = "priority"

    def visit(self, standard: typing.Callable[[], T_Result], priority: typing.Callable[[], T_Result]) -> T_Result:
        if self is ParseCreateJobRequestServiceTier.STANDARD:
            return standard()
        if self is ParseCreateJobRequestServiceTier.PRIORITY:
            return priority()
