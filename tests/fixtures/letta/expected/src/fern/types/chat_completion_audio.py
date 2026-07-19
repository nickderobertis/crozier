

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ChatCompletionAudio(UniversalBaseModel):
    """
    If the audio output modality is requested, this object contains data
    about the audio response from the model. [Learn more](https://platform.openai.com/docs/guides/audio).
    """

    id: str
    data: str
    expires_at: int
    transcript: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
