

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.shard_version_detail import ShardVersionDetail


class GetApiShardsHostOwnerRepoVersionResponse(UniversalBaseModel):
    name: typing.Optional[str] = None
    canonical_slug: typing.Optional[str] = None
    version: typing.Optional[ShardVersionDetail] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
