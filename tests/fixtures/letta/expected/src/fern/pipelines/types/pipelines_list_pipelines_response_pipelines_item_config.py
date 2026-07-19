

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .pipelines_list_pipelines_response_pipelines_item_config_data import (
    PipelinesListPipelinesResponsePipelinesItemConfigData,
)
from .pipelines_list_pipelines_response_pipelines_item_config_type import (
    PipelinesListPipelinesResponsePipelinesItemConfigType,
)


class PipelinesListPipelinesResponsePipelinesItemConfig(UniversalBaseModel):
    type: PipelinesListPipelinesResponsePipelinesItemConfigType
    data: PipelinesListPipelinesResponsePipelinesItemConfigData

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
