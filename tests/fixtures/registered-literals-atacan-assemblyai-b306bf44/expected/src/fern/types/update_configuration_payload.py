

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UpdateConfigurationPayload(UniversalBaseModel):
    type: str
    end_of_turn_confidence_threshold: typing.Optional[float] = pydantic.Field(default=None)
    """
    Confidence threshold (0-1) for detecting end of turn.
    """

    min_end_of_turn_silence_when_confident: typing.Optional[int] = pydantic.Field(default=None)
    """
    Minimum silence duration in ms when confident about end of turn.
    """

    max_turn_silence: typing.Optional[int] = pydantic.Field(default=None)
    """
    The maximum amount of silence allowed in a turn before end of turn is triggered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
