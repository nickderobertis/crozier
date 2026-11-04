

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetAudioSourceTracingResponseItemResults(UniversalBaseModel):
    label: typing.Optional[str] = pydantic.Field(default=None)
    """
    Identified source (e.g., resemble_ai, elevenlabs) or "real" if audio is not synthetic
    """

    error_message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
