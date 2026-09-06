

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ip_list_mode import IpListMode
from .ip_list_type import IpListType


class IpListEntry(UniversalBaseModel):
    ipornet: typing.Optional[str] = pydantic.Field(default=None)
    """
    IP address or network in CIDR format, for example `192.168.1.2/32`, `192.168.0.0/24`, `2001:db8::/32`
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    optional description
    """

    type: typing.Optional[IpListType] = None
    mode: typing.Optional[IpListMode] = None
    protocols: typing.Optional[int] = pydantic.Field(default=None)
    """
    Defines the protocol the entry applies to. `0` means all the supported protocols, 1 SSH, 2 FTP, 4 WebDAV, 8 HTTP. Protocols can be combined, for example 3 means SSH and FTP
    """

    created_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    creation time as unix timestamp in milliseconds
    """

    updated_at: typing.Optional[int] = pydantic.Field(default=None)
    """
    last update time as unix timestamp in millisecond
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
