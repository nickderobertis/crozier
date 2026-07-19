

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_content import N2InfoContent
from .n2sm_information import N2SmInformation
from .ng_ap_cause import NgApCause
from .ng_ran_target_id import NgRanTargetId
from .ue_context import UeContext


class UeContextCreateData(UniversalBaseModel):
    ue_context: typing_extensions.Annotated[
        UeContext, FieldMetadata(alias="ueContext"), pydantic.Field(alias="ueContext")
    ]
    target_id: typing_extensions.Annotated[
        NgRanTargetId, FieldMetadata(alias="targetId"), pydantic.Field(alias="targetId")
    ]
    source_to_target_data: typing_extensions.Annotated[
        N2InfoContent, FieldMetadata(alias="sourceToTargetData"), pydantic.Field(alias="sourceToTargetData")
    ]
    pdu_session_list: typing_extensions.Annotated[
        typing.Optional[typing.List[N2SmInformation]],
        FieldMetadata(alias="pduSessionList"),
        pydantic.Field(alias="pduSessionList"),
    ] = None
    n2notify_uri: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="n2NotifyUri"), pydantic.Field(alias="n2NotifyUri")
    ] = None
    ue_radio_capability: typing_extensions.Annotated[
        typing.Optional[N2InfoContent],
        FieldMetadata(alias="ueRadioCapability"),
        pydantic.Field(alias="ueRadioCapability"),
    ] = None
    ngap_cause: typing_extensions.Annotated[
        typing.Optional[NgApCause], FieldMetadata(alias="ngapCause"), pydantic.Field(alias="ngapCause")
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
