

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ListParticipantsFilterTrainingStatus(enum.StrEnum):
    """
    Return only records that have this training status
    """

    ACTIVE = "active"
    DEFERRED = "deferred"
    WITHDRAWN = "withdrawn"

    def visit(
        self,
        active: typing.Callable[[], T_Result],
        deferred: typing.Callable[[], T_Result],
        withdrawn: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ListParticipantsFilterTrainingStatus.ACTIVE:
            return active()
        if self is ListParticipantsFilterTrainingStatus.DEFERRED:
            return deferred()
        if self is ListParticipantsFilterTrainingStatus.WITHDRAWN:
            return withdrawn()
