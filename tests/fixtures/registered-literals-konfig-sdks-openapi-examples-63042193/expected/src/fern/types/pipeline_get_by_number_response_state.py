

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineGetByNumberResponseState(enum.StrEnum):
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
        if self is PipelineGetByNumberResponseState.CREATED:
            return created()
        if self is PipelineGetByNumberResponseState.ERRORED:
            return errored()
        if self is PipelineGetByNumberResponseState.SETUP_PENDING:
            return setup_pending()
        if self is PipelineGetByNumberResponseState.SETUP:
            return setup()
        if self is PipelineGetByNumberResponseState.PENDING:
            return pending()
