

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .profiles_network import ProfilesNetwork


class Profiles(UniversalBaseModel):
    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The url of the social profile
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    the persistent id related to this social profile (varies by social network)
    """

    network: typing.Optional[ProfilesNetwork] = pydantic.Field(default=None)
    """
    The network the profile exists on
    """

    username: typing.Optional[str] = pydantic.Field(default=None)
    """
    The username associated with the profile
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
