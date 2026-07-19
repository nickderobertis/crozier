

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .allowed_nssai import AllowedNssai
from .configured_snssai import ConfiguredSnssai
from .global_ran_node_id import GlobalRanNodeId
from .ipv6addr import Ipv6Addr
from .snssai import Snssai
from .ue_context import UeContext
from .user_location import UserLocation


class RegistrationContextContainer(UniversalBaseModel):
    ue_context: typing_extensions.Annotated[
        UeContext, FieldMetadata(alias="ueContext"), pydantic.Field(alias="ueContext")
    ]
    local_time_zone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="localTimeZone"), pydantic.Field(alias="localTimeZone")
    ] = None
    an_type: typing_extensions.Annotated[AccessType, FieldMetadata(alias="anType"), pydantic.Field(alias="anType")]
    an_n2ap_id: typing_extensions.Annotated[int, FieldMetadata(alias="anN2ApId"), pydantic.Field(alias="anN2ApId")]
    ran_node_id: typing_extensions.Annotated[
        GlobalRanNodeId, FieldMetadata(alias="ranNodeId"), pydantic.Field(alias="ranNodeId")
    ]
    initial_amf_name: typing_extensions.Annotated[
        str, FieldMetadata(alias="initialAmfName"), pydantic.Field(alias="initialAmfName")
    ]
    user_location: typing_extensions.Annotated[
        UserLocation, FieldMetadata(alias="userLocation"), pydantic.Field(alias="userLocation")
    ]
    rrc_est_cause: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="rrcEstCause"), pydantic.Field(alias="rrcEstCause")
    ] = None
    ue_context_request: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="ueContextRequest"), pydantic.Field(alias="ueContextRequest")
    ] = None
    an_n2i_pv4addr: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="anN2IPv4Addr"), pydantic.Field(alias="anN2IPv4Addr")
    ] = None
    an_n2i_pv6addr: typing_extensions.Annotated[
        typing.Optional[Ipv6Addr], FieldMetadata(alias="anN2IPv6Addr"), pydantic.Field(alias="anN2IPv6Addr")
    ] = None
    allowed_nssai: typing_extensions.Annotated[
        typing.Optional[AllowedNssai], FieldMetadata(alias="allowedNssai"), pydantic.Field(alias="allowedNssai")
    ] = None
    configured_nssai: typing_extensions.Annotated[
        typing.Optional[typing.List[ConfiguredSnssai]],
        FieldMetadata(alias="configuredNssai"),
        pydantic.Field(alias="configuredNssai"),
    ] = None
    rejected_nssai_in_plmn: typing_extensions.Annotated[
        typing.Optional[typing.List[Snssai]],
        FieldMetadata(alias="rejectedNssaiInPlmn"),
        pydantic.Field(alias="rejectedNssaiInPlmn"),
    ] = None
    rejected_nssai_in_ta: typing_extensions.Annotated[
        typing.Optional[typing.List[Snssai]],
        FieldMetadata(alias="rejectedNssaiInTa"),
        pydantic.Field(alias="rejectedNssaiInTa"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
