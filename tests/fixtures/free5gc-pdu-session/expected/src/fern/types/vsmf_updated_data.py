

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ebi_arp_mapping import EbiArpMapping
from .eps_bearer_id import EpsBearerId
from .qos_flow_item import QosFlowItem
from .ref_to_binary_data import RefToBinaryData
from .secondary_rat_usage_report import SecondaryRatUsageReport
from .user_location import UserLocation


class VsmfUpdatedData(UniversalBaseModel):
    qos_flows_add_mod_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowItem]],
        FieldMetadata(alias="qosFlowsAddModList"),
        pydantic.Field(alias="qosFlowsAddModList"),
    ] = None
    qos_flows_rel_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowItem]],
        FieldMetadata(alias="qosFlowsRelList"),
        pydantic.Field(alias="qosFlowsRelList"),
    ] = None
    qos_flows_failedto_add_mod_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowItem]],
        FieldMetadata(alias="qosFlowsFailedtoAddModList"),
        pydantic.Field(alias="qosFlowsFailedtoAddModList"),
    ] = None
    qos_flows_failedto_rel_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowItem]],
        FieldMetadata(alias="qosFlowsFailedtoRelList"),
        pydantic.Field(alias="qosFlowsFailedtoRelList"),
    ] = None
    n1sm_info_from_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoFromUe"), pydantic.Field(alias="n1SmInfoFromUe")
    ] = None
    unknown_n1sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData],
        FieldMetadata(alias="unknownN1SmInfo"),
        pydantic.Field(alias="unknownN1SmInfo"),
    ] = None
    ue_location: typing_extensions.Annotated[
        typing.Optional[UserLocation], FieldMetadata(alias="ueLocation"), pydantic.Field(alias="ueLocation")
    ] = None
    ue_time_zone: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ueTimeZone"), pydantic.Field(alias="ueTimeZone")
    ] = None
    add_ue_location: typing_extensions.Annotated[
        typing.Optional[UserLocation], FieldMetadata(alias="addUeLocation"), pydantic.Field(alias="addUeLocation")
    ] = None
    assigned_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EbiArpMapping]],
        FieldMetadata(alias="assignedEbiList"),
        pydantic.Field(alias="assignedEbiList"),
    ] = None
    failed_to_assign_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="failedToAssignEbiList"),
        pydantic.Field(alias="failedToAssignEbiList"),
    ] = None
    released_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="releasedEbiList"),
        pydantic.Field(alias="releasedEbiList"),
    ] = None
    secondary_rat_usage_report: typing_extensions.Annotated[
        typing.Optional[typing.List[SecondaryRatUsageReport]],
        FieldMetadata(alias="secondaryRatUsageReport"),
        pydantic.Field(alias="secondaryRatUsageReport"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
