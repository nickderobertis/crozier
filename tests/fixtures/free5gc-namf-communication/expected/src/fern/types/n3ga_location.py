

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ipv6addr import Ipv6Addr
from .tai import Tai


class N3GaLocation(UniversalBaseModel):
    n3gpp_tai: typing_extensions.Annotated[
        typing.Optional[Tai], FieldMetadata(alias="n3gppTai"), pydantic.Field(alias="n3gppTai")
    ] = None
    n3iwf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="n3IwfId"), pydantic.Field(alias="n3IwfId")
    ] = None
    ue_ipv4addr: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueIpv4Addr"), pydantic.Field(alias="ueIpv4Addr")
    ] = None
    ue_ipv6addr: typing_extensions.Annotated[
        typing.Optional[Ipv6Addr], FieldMetadata(alias="ueIpv6Addr"), pydantic.Field(alias="ueIpv6Addr")
    ] = None
    port_number: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="portNumber"), pydantic.Field(alias="portNumber")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
