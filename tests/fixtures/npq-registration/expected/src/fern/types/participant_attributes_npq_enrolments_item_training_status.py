

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ParticipantAttributesNpqEnrolmentsItemTrainingStatus(enum.StrEnum):
    """
    The training status of the NPQ participant
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
        if self is ParticipantAttributesNpqEnrolmentsItemTrainingStatus.ACTIVE:
            return active()
        if self is ParticipantAttributesNpqEnrolmentsItemTrainingStatus.DEFERRED:
            return deferred()
        if self is ParticipantAttributesNpqEnrolmentsItemTrainingStatus.WITHDRAWN:
            return withdrawn()
