

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .shard_detail_dependencies_item import ShardDetailDependenciesItem
from .shard_summary import ShardSummary
from .shard_version import ShardVersion


class ShardDetail(ShardSummary):
    versions: typing.Optional[typing.List[ShardVersion]] = None
    dependencies: typing.Optional[typing.List[ShardDetailDependenciesItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
