

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ShardSummary(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Display name from shard.yml. NOT unique: two shards on different
    hosts may share a name. Use canonical_slug to identify a shard.
    """

    host: typing.Optional[str] = None
    owner: typing.Optional[str] = None
    repo: typing.Optional[str] = None
    canonical_slug: typing.Optional[str] = pydantic.Field(default=None)
    """
    The shard's identity, host/owner/repo, and the unique key in the
    registry. Null only on legacy rows whose repository_url could not be
    parsed into an identity; those carry a reason and are not indexed.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path to the shard in the registry
    """

    unavailable_at: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    Set when the repository could not be reached on its host
    """

    description: typing.Optional[str] = None
    repository_url: typing.Optional[str] = None
    homepage_url: typing.Optional[str] = None
    documentation_url: typing.Optional[str] = None
    license: typing.Optional[str] = None
    total_downloads: typing.Optional[int] = None
    github_stars: typing.Optional[int] = None
    github_forks: typing.Optional[int] = None
    latest_version: typing.Optional[str] = None
    created_at: typing.Optional[dt.datetime] = None
    updated_at: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
