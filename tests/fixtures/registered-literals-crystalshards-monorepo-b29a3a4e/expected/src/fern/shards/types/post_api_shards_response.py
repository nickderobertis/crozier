

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .post_api_shards_response_shard import PostApiShardsResponseShard


class PostApiShardsResponse(UniversalBaseModel):
    message: typing.Optional[str] = None
    shard: typing.Optional[PostApiShardsResponseShard] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
