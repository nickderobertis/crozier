

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ebi_arp_mapping import EbiArpMapping
from .ho_state import HoState
from .n2sm_info_type import N2SmInfoType
from .ref_to_binary_data import RefToBinaryData
from .snssai import Snssai
from .up_cnx_state import UpCnxState


class SmContextCreatedData(UniversalBaseModel):
    h_smf_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hSmfUri"), pydantic.Field(alias="hSmfUri")
    ] = None
    pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ] = None
    s_nssai: typing_extensions.Annotated[
        typing.Optional[Snssai], FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")
    ] = None
    up_cnx_state: typing_extensions.Annotated[
        typing.Optional[UpCnxState], FieldMetadata(alias="upCnxState"), pydantic.Field(alias="upCnxState")
    ] = None
    n2sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n2SmInfo"), pydantic.Field(alias="n2SmInfo")
    ] = None
    n2sm_info_type: typing_extensions.Annotated[
        typing.Optional[N2SmInfoType], FieldMetadata(alias="n2SmInfoType"), pydantic.Field(alias="n2SmInfoType")
    ] = None
    allocated_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EbiArpMapping]],
        FieldMetadata(alias="allocatedEbiList"),
        pydantic.Field(alias="allocatedEbiList"),
    ] = None
    ho_state: typing_extensions.Annotated[
        typing.Optional[HoState], FieldMetadata(alias="hoState"), pydantic.Field(alias="hoState")
    ] = None
    smf_service_instance_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="smfServiceInstanceId"), pydantic.Field(alias="smfServiceInstanceId")
    ] = None
    recovery_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="recoveryTime"), pydantic.Field(alias="recoveryTime")
    ] = None
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
