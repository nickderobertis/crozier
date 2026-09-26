

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateVoiceProfileRequest(UniversalBaseModel):
    voice_profile: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="voiceProfile"),
        pydantic.Field(
            alias="voiceProfile",
            description="Free-form brand-voice profile (do/don't phrases, emoji policy,\nshort exemplars) that governs the AI chat loop and the review\ndrafter. A non-empty value is stored verbatim; an empty string\nclears the override.",
        ),
    ] = None
    """
    Free-form brand-voice profile (do/don't phrases, emoji policy,
    short exemplars) that governs the AI chat loop and the review
    drafter. A non-empty value is stored verbatim; an empty string
    clears the override.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
