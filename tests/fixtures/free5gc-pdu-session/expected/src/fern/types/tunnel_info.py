

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ipv6addr import Ipv6Addr


class TunnelInfo(UniversalBaseModel):
    ipv4addr: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ipv4Addr"), pydantic.Field(alias="ipv4Addr")
    ] = None
    ipv6addr: typing_extensions.Annotated[
        typing.Optional[Ipv6Addr], FieldMetadata(alias="ipv6Addr"), pydantic.Field(alias="ipv6Addr")
    ] = None
    gtp_teid: typing_extensions.Annotated[str, FieldMetadata(alias="gtpTeid"), pydantic.Field(alias="gtpTeid")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
