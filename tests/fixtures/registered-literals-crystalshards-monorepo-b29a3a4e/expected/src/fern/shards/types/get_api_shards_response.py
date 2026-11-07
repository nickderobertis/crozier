

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.pagination_meta import PaginationMeta
from ...types.shard_summary import ShardSummary


class GetApiShardsResponse(UniversalBaseModel):
    shards: typing.Optional[typing.List[ShardSummary]] = None
    meta: typing.Optional[PaginationMeta] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
