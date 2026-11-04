

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineTriggerNewPipelineResponseState(enum.StrEnum):
    """
    The current state of the pipeline.
    """

    CREATED = "created"
    ERRORED = "errored"
    SETUP_PENDING = "setup-pending"
    SETUP = "setup"
    PENDING = "pending"

    def visit(
        self,
        created: typing.Callable[[], T_Result],
        errored: typing.Callable[[], T_Result],
        setup_pending: typing.Callable[[], T_Result],
        setup: typing.Callable[[], T_Result],
        pending: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelineTriggerNewPipelineResponseState.CREATED:
            return created()
        if self is PipelineTriggerNewPipelineResponseState.ERRORED:
            return errored()
        if self is PipelineTriggerNewPipelineResponseState.SETUP_PENDING:
            return setup_pending()
        if self is PipelineTriggerNewPipelineResponseState.SETUP:
            return setup()
        if self is PipelineTriggerNewPipelineResponseState.PENDING:
            return pending()
