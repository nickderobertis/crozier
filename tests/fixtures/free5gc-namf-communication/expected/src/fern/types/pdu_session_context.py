

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .access_type import AccessType
from .ebi_arp_mapping import EbiArpMapping
from .snssai import Snssai


class PduSessionContext(UniversalBaseModel):
    pdu_session_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ]
    sm_context_ref: typing_extensions.Annotated[
        str, FieldMetadata(alias="smContextRef"), pydantic.Field(alias="smContextRef")
    ]
    s_nssai: typing_extensions.Annotated[Snssai, FieldMetadata(alias="sNssai"), pydantic.Field(alias="sNssai")]
    dnn: str
    access_type: typing_extensions.Annotated[
        AccessType, FieldMetadata(alias="accessType"), pydantic.Field(alias="accessType")
    ]
    allocated_ebi_list: typing_extensions.Annotated[
        typing.List[EbiArpMapping], FieldMetadata(alias="allocatedEbiList"), pydantic.Field(alias="allocatedEbiList")
    ]
    hsmf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="hsmfId"), pydantic.Field(alias="hsmfId")
    ] = None
    vsmf_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="vsmfId"), pydantic.Field(alias="vsmfId")
    ] = None
    ns_instance: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nsInstance"), pydantic.Field(alias="nsInstance")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
