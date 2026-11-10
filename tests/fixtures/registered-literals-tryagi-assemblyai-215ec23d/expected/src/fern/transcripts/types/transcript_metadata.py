

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transcript_metadata_warnings_item import TranscriptMetadataWarningsItem


class TranscriptMetadata(UniversalBaseModel):
    """
    Additional information about the transcript, including any warnings raised while processing the request.
    """

    warnings: typing.Optional[typing.List[TranscriptMetadataWarningsItem]] = pydantic.Field(default=None)
    """
    Warnings raised while processing the request, for example when [Automatic Language Detection](https://www.assemblyai.com/docs/pre-recorded-audio/language-detection) was skipped because the audio contained no speech.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
