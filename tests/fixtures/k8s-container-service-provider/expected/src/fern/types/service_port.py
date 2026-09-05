

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServicePort(UniversalBaseModel):
    """
    Service port details
    """

    port: int = pydantic.Field()
    """
    Service port number
    """

    target_port: int = pydantic.Field()
    """
    Target container port
    """

    protocol: typing.Optional[str] = pydantic.Field(default=None)
    """
    Protocol (TCP, UDP)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
