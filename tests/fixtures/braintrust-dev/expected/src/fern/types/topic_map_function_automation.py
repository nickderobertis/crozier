

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .topic_map_function_automation_function import TopicMapFunctionAutomationFunction


class TopicMapFunctionAutomation(UniversalBaseModel):
    function: TopicMapFunctionAutomationFunction
    btql_filter: typing.Optional[str] = pydantic.Field(default=None)
    """
    Per-topic-map BTQL filter. For trace scope, a topic map runs when max(filter) over the trace is truthy. For span scope, it runs when the current span matches.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
