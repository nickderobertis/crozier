

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .compaction_settings_input import CompactionSettingsInput


class CompactionRequest(UniversalBaseModel):
    compaction_settings: typing.Optional[CompactionSettingsInput] = pydantic.Field(default=None)
    """
    Optional compaction settings to use for this summarization request. If not provided, the agent's default settings will be used.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
