

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compaction_config import CompactionConfig
from .large_tool_response_config import LargeToolResponseConfig


class ContextManagementConfig(UniversalBaseModel):
    compaction: typing.Optional[CompactionConfig] = None
    large_tool_response: typing.Optional[LargeToolResponseConfig] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
