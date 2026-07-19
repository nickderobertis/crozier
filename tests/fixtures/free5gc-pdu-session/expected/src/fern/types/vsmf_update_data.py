

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ambr import Ambr
from .cause import Cause
from .ebi_arp_mapping import EbiArpMapping
from .eps_bearer_id import EpsBearerId
from .eps_bearer_info import EpsBearerInfo
from .qos_flow_add_modify_request_item import QosFlowAddModifyRequestItem
from .qos_flow_release_request_item import QosFlowReleaseRequestItem
from .ref_to_binary_data import RefToBinaryData
from .request_indication import RequestIndication


class VsmfUpdateData(UniversalBaseModel):
    request_indication: typing_extensions.Annotated[
        RequestIndication, FieldMetadata(alias="requestIndication"), pydantic.Field(alias="requestIndication")
    ]
    session_ambr: typing_extensions.Annotated[
        typing.Optional[Ambr], FieldMetadata(alias="sessionAmbr"), pydantic.Field(alias="sessionAmbr")
    ] = None
    qos_flows_add_mod_request_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowAddModifyRequestItem]],
        FieldMetadata(alias="qosFlowsAddModRequestList"),
        pydantic.Field(alias="qosFlowsAddModRequestList"),
    ] = None
    qos_flows_rel_request_list: typing_extensions.Annotated[
        typing.Optional[typing.List[QosFlowReleaseRequestItem]],
        FieldMetadata(alias="qosFlowsRelRequestList"),
        pydantic.Field(alias="qosFlowsRelRequestList"),
    ] = None
    eps_bearer_info: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerInfo]],
        FieldMetadata(alias="epsBearerInfo"),
        pydantic.Field(alias="epsBearerInfo"),
    ] = None
    assign_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="assignEbiList"),
        pydantic.Field(alias="assignEbiList"),
    ] = None
    revoke_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="revokeEbiList"),
        pydantic.Field(alias="revokeEbiList"),
    ] = None
    modified_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EbiArpMapping]],
        FieldMetadata(alias="modifiedEbiList"),
        pydantic.Field(alias="modifiedEbiList"),
    ] = None
    pti: typing.Optional[int] = None
    n1sm_info_to_ue: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmInfoToUe"), pydantic.Field(alias="n1SmInfoToUe")
    ] = None
    always_on_granted: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="alwaysOnGranted"), pydantic.Field(alias="alwaysOnGranted")
    ] = None
    cause: typing.Optional[Cause] = None
    n1sm_cause: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="n1smCause"), pydantic.Field(alias="n1smCause")
    ] = None
    back_off_timer: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="backOffTimer"), pydantic.Field(alias="backOffTimer")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
