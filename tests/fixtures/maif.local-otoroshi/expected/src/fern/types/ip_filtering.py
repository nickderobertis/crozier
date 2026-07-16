

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class IpFiltering(UniversalBaseModel):
    """
    The filtering configuration block for a service of globally.
    """

    blacklist: typing.List[str] = pydantic.Field()
    """
    Blacklisted IP addresses
    """

    whitelist: typing.List[str] = pydantic.Field()
    """
    Whitelisted IP addresses
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
