

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Provider(UniversalBaseModel):
    """
    The provider

    *New in version 2.1.0*
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description of the provider.
    """

    package_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The package name of the provider.
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    The version of the provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
