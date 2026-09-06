

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automod_keyword_preset_type import AutomodKeywordPresetType


class DefaultKeywordListTriggerMetadataResponse(UniversalBaseModel):
    allow_list: typing.List[str]
    presets: typing.List[AutomodKeywordPresetType]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
