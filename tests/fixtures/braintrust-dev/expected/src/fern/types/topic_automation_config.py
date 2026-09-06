

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .topic_automation_config_backfill_time_range import TopicAutomationConfigBackfillTimeRange
from .topic_automation_config_event_type import TopicAutomationConfigEventType
from .topic_automation_config_facet_functions_item import TopicAutomationConfigFacetFunctionsItem
from .topic_automation_config_scope import TopicAutomationConfigScope
from .topic_automation_data_scope import TopicAutomationDataScope
from .topic_map_function_automation import TopicMapFunctionAutomation


class TopicAutomationConfig(UniversalBaseModel):
    event_type: TopicAutomationConfigEventType = pydantic.Field()
    """
    The type of automation.
    """

    sampling_rate: float = pydantic.Field()
    """
    The sampling rate for topic automation
    """

    facet_functions: typing.List[TopicAutomationConfigFacetFunctionsItem] = pydantic.Field()
    """
    Facet functions used by the topic automation
    """

    topic_map_functions: typing.List[TopicMapFunctionAutomation] = pydantic.Field()
    """
    Topic map functions with optional per-topic-map filters
    """

    scope: typing.Optional[TopicAutomationConfigScope] = pydantic.Field(default=None)
    """
    Execution scope for topic automation. Defaults to span-level execution.
    """

    data_scope: typing.Optional[TopicAutomationDataScope] = None
    btql_filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional BTQL filter applied before topic automation.
    """

    rerun_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    How often to recompute topic maps
    """

    relabel_overlap_seconds: typing.Optional[float] = pydantic.Field(default=None)
    """
    How much recent history to relabel after a new topic map version becomes active
    """

    backfill_time_range: typing.Optional[TopicAutomationConfigBackfillTimeRange] = pydantic.Field(default=None)
    """
    Topic window used for classification coverage and initial backfill.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
