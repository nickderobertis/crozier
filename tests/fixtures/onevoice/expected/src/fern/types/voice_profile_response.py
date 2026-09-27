

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class VoiceProfileResponse(UniversalBaseModel):
    voice_profile: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="voiceProfile"),
        pydantic.Field(alias="voiceProfile", description="Stored brand-voice profile; empty string when unset."),
    ]
    """
    Stored brand-voice profile; empty string when unset.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
