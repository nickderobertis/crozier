

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .topic_automation_data_scope_zero_type import TopicAutomationDataScopeZeroType


class TopicAutomationDataScopeZero(UniversalBaseModel):
    type: TopicAutomationDataScopeZeroType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
