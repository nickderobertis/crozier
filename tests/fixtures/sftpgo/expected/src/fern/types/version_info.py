

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VersionInfo(UniversalBaseModel):
    version: typing.Optional[str] = None
    build_date: typing.Optional[str] = None
    commit_hash: typing.Optional[str] = None
    features: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Features for the current build. Available features are `portable`, `bolt`, `mysql`, `sqlite`, `pgsql`, `s3`, `gcs`, `azblob`, `metrics`, `unixcrypt`. If a feature is available it has a `+` prefix, otherwise a `-` prefix
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
