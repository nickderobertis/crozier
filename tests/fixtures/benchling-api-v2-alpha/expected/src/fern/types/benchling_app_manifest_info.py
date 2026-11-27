

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BenchlingAppManifestInfo(UniversalBaseModel):
    description: typing.Optional[str] = None
    name: typing.Optional[str] = None
    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    A semver string for the version of the benchling app described by this manifest.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
