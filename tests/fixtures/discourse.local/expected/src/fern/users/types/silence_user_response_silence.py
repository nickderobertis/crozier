

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .silence_user_response_silence_silenced_by import SilenceUserResponseSilenceSilencedBy


class SilenceUserResponseSilence(UniversalBaseModel):
    silence_reason: str
    silenced: bool
    silenced_at: str
    silenced_by: SilenceUserResponseSilenceSilencedBy
    silenced_till: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
