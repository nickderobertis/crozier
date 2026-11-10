

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .audio_intelligence_model_status import AudioIntelligenceModelStatus
from .auto_highlight_result import AutoHighlightResult


class AutoHighlightsResult(UniversalBaseModel):
    """
    An array of results for the Key Phrases model, if it is enabled.
    See [Key phrases](https://www.assemblyai.com/docs/speech-understanding/key-phrases) for more information.
    """

    status: AudioIntelligenceModelStatus = pydantic.Field()
    """
    The status of the Key Phrases model. Either success, or unavailable in the rare case that the model failed.
    """

    results: typing.List[AutoHighlightResult] = pydantic.Field()
    """
    A temporally-sequential array of Key Phrases
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
