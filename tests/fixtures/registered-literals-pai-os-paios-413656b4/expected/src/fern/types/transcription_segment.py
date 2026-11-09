

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TranscriptionSegment(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier of the segment.
    """

    seek: int = pydantic.Field()
    """
    Seek offset of the segment.
    """

    start: float = pydantic.Field()
    """
    Start time of the segment in seconds.
    """

    end: float = pydantic.Field()
    """
    End time of the segment in seconds.
    """

    text: str = pydantic.Field()
    """
    Text content of the segment.
    """

    tokens: typing.List[int] = pydantic.Field()
    """
    Array of token IDs for the text content.
    """

    temperature: float = pydantic.Field()
    """
    Temperature parameter used for generating the segment.
    """

    avg_logprob: float = pydantic.Field()
    """
    Average logprob of the segment. If the value is lower than -1, consider the logprobs failed.
    """

    compression_ratio: float = pydantic.Field()
    """
    Compression ratio of the segment. If the value is greater than 2.4, consider the compression failed.
    """

    no_speech_prob: float = pydantic.Field()
    """
    Probability of no speech in the segment. If the value is higher than 1.0 and the `avg_logprob` is below -1, consider this segment silent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
