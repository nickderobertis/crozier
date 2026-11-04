

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineGetAllPipelinesResponseItemsItemState(enum.StrEnum):
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
        if self is PipelineGetAllPipelinesResponseItemsItemState.CREATED:
            return created()
        if self is PipelineGetAllPipelinesResponseItemsItemState.ERRORED:
            return errored()
        if self is PipelineGetAllPipelinesResponseItemsItemState.SETUP_PENDING:
            return setup_pending()
        if self is PipelineGetAllPipelinesResponseItemsItemState.SETUP:
            return setup()
        if self is PipelineGetAllPipelinesResponseItemsItemState.PENDING:
            return pending()
