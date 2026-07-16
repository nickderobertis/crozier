

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .not_specified import NotSpecified
from .tunnel_type import TunnelType


class TunnelInfo(UniversalBaseModel):
    tunnel_dst_address: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tunnelDstAddress"),
        pydantic.Field(alias="tunnelDstAddress", description="Destination address of the tunnel."),
    ]
    """
    Destination address of the tunnel.
    """

    tunnel_specific_data: typing_extensions.Annotated[
        typing.Optional[NotSpecified],
        FieldMetadata(alias="tunnelSpecificData"),
        pydantic.Field(alias="tunnelSpecificData"),
    ] = None
    tunnel_src_address: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tunnelSrcAddress"),
        pydantic.Field(alias="tunnelSrcAddress", description="Source address of the tunnel."),
    ]
    """
    Source address of the tunnel.
    """

    tunnel_type: typing_extensions.Annotated[
        TunnelType, FieldMetadata(alias="tunnelType"), pydantic.Field(alias="tunnelType")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
