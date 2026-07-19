

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .area_of_validity import AreaOfValidity
from .arp import Arp
from .n1message_container import N1MessageContainer
from .n2info_container import N2InfoContainer


class N1N2MessageTransferReqData(UniversalBaseModel):
    n1message_container: typing_extensions.Annotated[
        typing.Optional[N1MessageContainer],
        FieldMetadata(alias="n1MessageContainer"),
        pydantic.Field(alias="n1MessageContainer"),
    ] = None
    n2info_container: typing_extensions.Annotated[
        typing.Optional[N2InfoContainer],
        FieldMetadata(alias="n2InfoContainer"),
        pydantic.Field(alias="n2InfoContainer"),
    ] = None
    skip_ind: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="skipInd"), pydantic.Field(alias="skipInd")
    ] = None
    last_msg_indication: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="lastMsgIndication"), pydantic.Field(alias="lastMsgIndication")
    ] = None
    pdu_session_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pduSessionId"), pydantic.Field(alias="pduSessionId")
    ] = None
    lcs_correlation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lcsCorrelationId"), pydantic.Field(alias="lcsCorrelationId")
    ] = None
    ppi: typing.Optional[int] = None
    arp: typing.Optional[Arp] = None
    f_5qi: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="5qi"), pydantic.Field(alias="5qi")
    ] = None
    n1n2failure_txf_notif_uri: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="n1n2FailureTxfNotifURI"),
        pydantic.Field(alias="n1n2FailureTxfNotifURI"),
    ] = None
    smf_reallocation_ind: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="smfReallocationInd"), pydantic.Field(alias="smfReallocationInd")
    ] = None
    area_of_validity: typing_extensions.Annotated[
        typing.Optional[AreaOfValidity], FieldMetadata(alias="areaOfValidity"), pydantic.Field(alias="areaOfValidity")
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
