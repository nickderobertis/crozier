

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CleVersionSpecifier(UniversalBaseModel):
    """
    A version specifier that can be either a single version or a version range
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    A specific version string
    """

    range: typing.Optional[str] = pydantic.Field(default=None)
    """
    A version range in vers format (e.g. "vers:npm/>=1.0.0|<2.0.0")
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
