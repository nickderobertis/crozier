

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Target(UniversalBaseModel):
    """
    A Target is where an HTTP call will be forwarded in the end from a service domain
    """

    host: str = pydantic.Field()
    """
    The host on which the HTTP call will be forwarded. Can be a domain name, or an IP address. Can also have a port
    """

    scheme: str = pydantic.Field()
    """
    The protocol used for communication. Can be http or https
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
