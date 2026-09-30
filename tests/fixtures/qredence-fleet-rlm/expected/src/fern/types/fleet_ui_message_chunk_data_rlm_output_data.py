

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class FleetUiMessageChunkDataRlmOutputData(UniversalBaseModel):
    output: str
    step: typing.Optional[int] = None
    stream_id: typing.Optional[str] = None
    is_delta: typing.Optional[bool] = None
    is_final: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
