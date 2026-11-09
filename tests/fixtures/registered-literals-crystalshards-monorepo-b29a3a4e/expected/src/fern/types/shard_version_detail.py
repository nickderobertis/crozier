

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .shard_version import ShardVersion
from .shard_version_detail_dependencies_item import ShardVersionDetailDependenciesItem


class ShardVersionDetail(ShardVersion):
    crystal_version_constraint: typing.Optional[str] = None
    dependencies: typing.Optional[typing.List[ShardVersionDetailDependenciesItem]] = None
    authors: typing.Optional[typing.List[str]] = None
    readme: typing.Optional[str] = None
    checksum: typing.Optional[str] = None
    package_url: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
