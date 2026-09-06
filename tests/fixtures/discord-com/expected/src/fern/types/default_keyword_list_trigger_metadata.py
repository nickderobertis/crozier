

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .automod_keyword_preset_type import AutomodKeywordPresetType


class DefaultKeywordListTriggerMetadata(UniversalBaseModel):
    allow_list: typing.Optional[typing.List[str]] = None
    presets: typing.Optional[typing.List[AutomodKeywordPresetType]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
