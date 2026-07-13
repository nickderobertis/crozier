

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PermittedIpRead(UniversalBaseModel):
    ip: typing.Optional[str] = pydantic.Field(default=None)
    """
    The IP address.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the IP. May be "ACTIVE" or "INACTIVE". It is only possible to make requests from "ACTIVE" IP addresses. Only "ACTIVE" IPs will be billed.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
