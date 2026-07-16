

import datetime as dt
import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class VoiceV1IpRecord(UniversalBaseModel):
    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the IP Record resource.
    """

    cidr_prefix_length: typing.Optional[int] = pydantic.Field(default=None)
    """
    An integer representing the length of the [CIDR](https://tools.ietf.org/html/rfc4632) prefix to use with this IP address. By default the entire IP address is used, which for IPv4 is value 32.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT that the resource was created specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT that the resource was last updated specified in [RFC 2822](https://www.ietf.org/rfc/rfc2822.txt) format.
    """

    friendly_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The string that you assigned to describe the resource.
    """

    ip_address: typing.Optional[str] = pydantic.Field(default=None)
    """
    An IP address in dotted decimal notation, IPv4 only.
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string that we created to identify the IP Record resource.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
