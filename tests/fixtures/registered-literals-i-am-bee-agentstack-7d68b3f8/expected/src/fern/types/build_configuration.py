

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BuildConfiguration(UniversalBaseModel):
    dockerfile_path: typing.Optional[str] = pydantic.Field(default=None)
    """
    Path to Dockerfile relative to the repository path (provider_build.source.path or repository root if not defined)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
