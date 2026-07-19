

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .expected_ue_behavior import ExpectedUeBehavior
from .nas_security_mode import NasSecurityMode
from .nsi_id import NsiId
from .nssai_mapping import NssaiMapping
from .snssai import Snssai


class MmContext(UniversalBaseModel):
    access_type: typing_extensions.Annotated[
        AccessType, FieldMetadata(alias="accessType"), pydantic.Field(alias="accessType")
    ]
    nas_security_mode: typing_extensions.Annotated[
        typing.Optional[NasSecurityMode],
        FieldMetadata(alias="nasSecurityMode"),
        pydantic.Field(alias="nasSecurityMode"),
    ] = None
    nas_downlink_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nasDownlinkCount"), pydantic.Field(alias="nasDownlinkCount")
    ] = None
    nas_uplink_count: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="nasUplinkCount"), pydantic.Field(alias="nasUplinkCount")
    ] = None
    ue_security_capability: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueSecurityCapability"), pydantic.Field(alias="ueSecurityCapability")
    ] = None
    s1ue_network_capability: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="s1UeNetworkCapability"),
        pydantic.Field(alias="s1UeNetworkCapability"),
    ] = None
    allowed_nssai: typing_extensions.Annotated[
        typing.Optional[typing.List[Snssai]], FieldMetadata(alias="allowedNssai"), pydantic.Field(alias="allowedNssai")
    ] = None
    nssai_mapping_list: typing_extensions.Annotated[
        typing.Optional[typing.List[NssaiMapping]],
        FieldMetadata(alias="nssaiMappingList"),
        pydantic.Field(alias="nssaiMappingList"),
    ] = None
    ns_instance_list: typing_extensions.Annotated[
        typing.Optional[typing.List[NsiId]],
        FieldMetadata(alias="nsInstanceList"),
        pydantic.Field(alias="nsInstanceList"),
    ] = None
    expected_u_ebehavior: typing_extensions.Annotated[
        typing.Optional[ExpectedUeBehavior],
        FieldMetadata(alias="expectedUEbehavior"),
        pydantic.Field(alias="expectedUEbehavior"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
