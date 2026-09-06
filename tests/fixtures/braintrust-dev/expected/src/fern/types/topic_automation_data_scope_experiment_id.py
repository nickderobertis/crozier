

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .topic_automation_data_scope_experiment_id_type import TopicAutomationDataScopeExperimentIdType


class TopicAutomationDataScopeExperimentId(UniversalBaseModel):
    type: TopicAutomationDataScopeExperimentIdType
    experiment_id: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
