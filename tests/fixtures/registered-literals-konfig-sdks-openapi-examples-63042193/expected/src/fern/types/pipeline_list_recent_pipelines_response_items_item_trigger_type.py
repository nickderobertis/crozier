

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PipelineListRecentPipelinesResponseItemsItemTriggerType(enum.StrEnum):
    """
    The type of trigger.
    """

    SCHEDULED_PIPELINE = "scheduled_pipeline"
    EXPLICIT = "explicit"
    API = "api"
    WEBHOOK = "webhook"

    def visit(
        self,
        scheduled_pipeline: typing.Callable[[], T_Result],
        explicit: typing.Callable[[], T_Result],
        api: typing.Callable[[], T_Result],
        webhook: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PipelineListRecentPipelinesResponseItemsItemTriggerType.SCHEDULED_PIPELINE:
            return scheduled_pipeline()
        if self is PipelineListRecentPipelinesResponseItemsItemTriggerType.EXPLICIT:
            return explicit()
        if self is PipelineListRecentPipelinesResponseItemsItemTriggerType.API:
            return api()
        if self is PipelineListRecentPipelinesResponseItemsItemTriggerType.WEBHOOK:
            return webhook()
