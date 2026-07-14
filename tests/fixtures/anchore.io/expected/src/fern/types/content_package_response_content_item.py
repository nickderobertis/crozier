

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ContentPackageResponseContentItem(UniversalBaseModel):
    cpes: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of Common Platform Enumerations that may uniquely identify the package
    """

    license: typing.Optional[str] = pydantic.Field(default=None)
    """
    Deprecated in favor of the 'licenses' field"
    """

    licenses: typing.Optional[typing.List[str]] = None
    location: typing.Optional[str] = None
    origin: typing.Optional[str] = None
    package: typing.Optional[str] = None
    size: typing.Optional[str] = None
    type: typing.Optional[str] = None
    version: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
