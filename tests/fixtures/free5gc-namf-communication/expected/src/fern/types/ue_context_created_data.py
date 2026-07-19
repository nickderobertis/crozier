

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_content import N2InfoContent
from .n2sm_information import N2SmInformation
from .ng_ap_cause import NgApCause
from .ue_context import UeContext


class UeContextCreatedData(UniversalBaseModel):
    ue_context: typing_extensions.Annotated[
        UeContext, FieldMetadata(alias="ueContext"), pydantic.Field(alias="ueContext")
    ]
    target_to_source_data: typing_extensions.Annotated[
        N2InfoContent, FieldMetadata(alias="targetToSourceData"), pydantic.Field(alias="targetToSourceData")
    ]
    pdu_session_list: typing_extensions.Annotated[
        typing.Optional[typing.List[N2SmInformation]],
        FieldMetadata(alias="pduSessionList"),
        pydantic.Field(alias="pduSessionList"),
    ] = None
    ngap_cause: typing_extensions.Annotated[
        typing.Optional[NgApCause], FieldMetadata(alias="ngapCause"), pydantic.Field(alias="ngapCause")
    ] = None
    failed_session_list: typing_extensions.Annotated[
        typing.Optional[typing.List[N2SmInformation]],
        FieldMetadata(alias="failedSessionList"),
        pydantic.Field(alias="failedSessionList"),
    ] = None
    supported_features: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="supportedFeatures"), pydantic.Field(alias="supportedFeatures")
    ] = None
    pcf_reselected_ind: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="pcfReselectedInd"), pydantic.Field(alias="pcfReselectedInd")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
