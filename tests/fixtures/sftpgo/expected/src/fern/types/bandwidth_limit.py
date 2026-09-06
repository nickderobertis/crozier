

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BandwidthLimit(UniversalBaseModel):
    sources: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    Source networks in CIDR notation as defined in RFC 4632 and RFC 4291 for example `192.0.2.0/24` or `2001:db8::/32`. The limit applies if the defined networks contain the client IP
    """

    upload_bandwidth: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum upload bandwidth in KB/s per upload, 0 means unlimited
    """

    download_bandwidth: typing.Optional[int] = pydantic.Field(default=None)
    """
    Maximum download bandwidth in KB/s per upload, 0 means unlimited
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
