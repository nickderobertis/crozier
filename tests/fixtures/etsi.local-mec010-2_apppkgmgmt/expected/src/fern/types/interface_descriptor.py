

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .interface_type import InterfaceType
from .tunnel_info import TunnelInfo


class InterfaceDescriptor(UniversalBaseModel):
    dst_ip_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dstIPAddress")] = (
        pydantic.Field(default=None)
    )
    """
    If the interface type is IP, the destination address identifies the IP address of the destination. Only used for dstInterface.
    """

    dst_mac_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="dstMACAddress")] = (
        pydantic.Field(default=None)
    )
    """
    If the interface type is MAC, the destination address identifies the MAC address of the destination. Only used for dstInterface.
    """

    interface_type: typing_extensions.Annotated[InterfaceType, FieldMetadata(alias="interfaceType")]
    src_mac_address: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="srcMACAddress")] = (
        pydantic.Field(default=None)
    )
    """
    If the interface type is MAC, the source address identifies the MAC address of the interface.
    """

    tunnel_info: typing_extensions.Annotated[typing.Optional[TunnelInfo], FieldMetadata(alias="tunnelInfo")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
