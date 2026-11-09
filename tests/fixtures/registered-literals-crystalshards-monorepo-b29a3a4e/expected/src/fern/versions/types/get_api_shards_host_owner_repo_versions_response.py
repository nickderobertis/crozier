

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.shard_version import ShardVersion


class GetApiShardsHostOwnerRepoVersionsResponse(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name, which is not unique
    """

    canonical_slug: typing.Optional[str] = None
    versions: typing.Optional[typing.List[ShardVersion]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
