

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InferConfig(UniversalBaseModel):
    batch_size: typing.Optional[int] = None
    spliter_threshold: typing.Optional[int] = None
    eos: typing.Optional[str] = None
    seed: typing.Optional[int] = None
    stream: typing.Optional[bool] = None
    stream_chunk_size: typing.Optional[int] = None
    no_cache: typing.Optional[bool] = None
    sync_gen: typing.Optional[bool] = None
    timeout: typing.Optional[int] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
