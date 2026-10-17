

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .phrase_based_action_trigger_config import PhraseBasedActionTriggerConfig


class PhraseBasedActionTriggerOutput(UniversalBaseModel):
    config: PhraseBasedActionTriggerConfig

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
