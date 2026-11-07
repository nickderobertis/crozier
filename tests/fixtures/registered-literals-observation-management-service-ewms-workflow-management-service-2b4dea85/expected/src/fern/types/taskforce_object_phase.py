

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TaskforceObjectPhase(enum.StrEnum):
    """
    The current phase of the taskforce within the workflow's lifetime. Not all taskforces will enter every phase.
    """

    PRE_MQ_ACTIVATION = "pre-mq-activation"
    PRE_LAUNCH = "pre-launch"
    PENDING_STARTER = "pending-starter"
    CONDOR_SUBMIT = "condor-submit"
    PENDING_STOPPER = "pending-stopper"
    CONDOR_RM = "condor-rm"
    CONDOR_COMPLETE = "condor-complete"

    def visit(
        self,
        pre_mq_activation: typing.Callable[[], T_Result],
        pre_launch: typing.Callable[[], T_Result],
        pending_starter: typing.Callable[[], T_Result],
        condor_submit: typing.Callable[[], T_Result],
        pending_stopper: typing.Callable[[], T_Result],
        condor_rm: typing.Callable[[], T_Result],
        condor_complete: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TaskforceObjectPhase.PRE_MQ_ACTIVATION:
            return pre_mq_activation()
        if self is TaskforceObjectPhase.PRE_LAUNCH:
            return pre_launch()
        if self is TaskforceObjectPhase.PENDING_STARTER:
            return pending_starter()
        if self is TaskforceObjectPhase.CONDOR_SUBMIT:
            return condor_submit()
        if self is TaskforceObjectPhase.PENDING_STOPPER:
            return pending_stopper()
        if self is TaskforceObjectPhase.CONDOR_RM:
            return condor_rm()
        if self is TaskforceObjectPhase.CONDOR_COMPLETE:
            return condor_complete()
