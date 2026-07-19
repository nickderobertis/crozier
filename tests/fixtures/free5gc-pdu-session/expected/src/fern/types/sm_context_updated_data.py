

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ebi_arp_mapping import EbiArpMapping
from .eps_bearer_container import EpsBearerContainer
from .eps_bearer_id import EpsBearerId
from .ho_state import HoState
from .n2sm_info_type import N2SmInfoType
from .ref_to_binary_data import RefToBinaryData
from .up_cnx_state import UpCnxState


class SmContextUpdatedData(UniversalBaseModel):
    up_cnx_state: typing_extensions.Annotated[
        typing.Optional[UpCnxState], FieldMetadata(alias="upCnxState"), pydantic.Field(alias="upCnxState")
    ] = None
    ho_state: typing_extensions.Annotated[
        typing.Optional[HoState], FieldMetadata(alias="hoState"), pydantic.Field(alias="hoState")
    ] = None
    release_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerId]],
        FieldMetadata(alias="releaseEbiList"),
        pydantic.Field(alias="releaseEbiList"),
    ] = None
    allocated_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EbiArpMapping]],
        FieldMetadata(alias="allocatedEbiList"),
        pydantic.Field(alias="allocatedEbiList"),
    ] = None
    modified_ebi_list: typing_extensions.Annotated[
        typing.Optional[typing.List[EbiArpMapping]],
        FieldMetadata(alias="modifiedEbiList"),
        pydantic.Field(alias="modifiedEbiList"),
    ] = None
    n1sm_msg: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n1SmMsg"), pydantic.Field(alias="n1SmMsg")
    ] = None
    n2sm_info: typing_extensions.Annotated[
        typing.Optional[RefToBinaryData], FieldMetadata(alias="n2SmInfo"), pydantic.Field(alias="n2SmInfo")
    ] = None
    n2sm_info_type: typing_extensions.Annotated[
        typing.Optional[N2SmInfoType], FieldMetadata(alias="n2SmInfoType"), pydantic.Field(alias="n2SmInfoType")
    ] = None
    eps_bearer_setup: typing_extensions.Annotated[
        typing.Optional[typing.List[EpsBearerContainer]],
        FieldMetadata(alias="epsBearerSetup"),
        pydantic.Field(alias="epsBearerSetup"),
    ] = None
    data_forwarding: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="dataForwarding"), pydantic.Field(alias="dataForwarding")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
