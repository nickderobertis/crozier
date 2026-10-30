

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .speaker_reference import SpeakerReference


class SpeakerConfig(UniversalBaseModel):
    """
    任选其中一种形式指定 spk
    """

    from_spk_id: typing.Optional[str] = None
    from_spk_name: typing.Optional[str] = None
    from_ref: typing.Optional[SpeakerReference] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
