

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetTranscriptResponseItemWordsItem(UniversalBaseModel):
    text: typing.Optional[str] = None
    start_time: typing.Optional[float] = None
    end_time: typing.Optional[float] = None
    speaker_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
