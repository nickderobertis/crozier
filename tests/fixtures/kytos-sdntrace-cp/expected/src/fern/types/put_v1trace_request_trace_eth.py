

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PutV1TraceRequestTraceEth(UniversalBaseModel):
    dl_vlan: typing.Optional[int] = pydantic.Field(default=None)
    """
    VLAN ID. This is an integer in range [1, 4095] as in a network packet.
    """

    dl_type: typing.Optional[int] = pydantic.Field(default=None)
    """
    Ethernet type
    """

    dl_src: typing.Optional[str] = pydantic.Field(default=None)
    """
    Source MAC address
    """

    dl_dst: typing.Optional[str] = pydantic.Field(default=None)
    """
    Destination MAC address
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
