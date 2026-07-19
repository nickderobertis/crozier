

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .n2info_container import N2InfoContainer
from .n2info_notify_reason import N2InfoNotifyReason
from .pdu_session_id import PduSessionId


class N2InformationNotification(UniversalBaseModel):
    n2notify_subscription_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="n2NotifySubscriptionId"), pydantic.Field(alias="n2NotifySubscriptionId")
    ]
    n2info_container: typing_extensions.Annotated[
        typing.Optional[N2InfoContainer],
        FieldMetadata(alias="n2InfoContainer"),
        pydantic.Field(alias="n2InfoContainer"),
    ] = None
    to_release_session_list: typing_extensions.Annotated[
        typing.Optional[typing.List[PduSessionId]],
        FieldMetadata(alias="toReleaseSessionList"),
        pydantic.Field(alias="toReleaseSessionList"),
    ] = None
    lcs_correlation_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lcsCorrelationId"), pydantic.Field(alias="lcsCorrelationId")
    ] = None
    notify_reason: typing_extensions.Annotated[
        typing.Optional[N2InfoNotifyReason], FieldMetadata(alias="notifyReason"), pydantic.Field(alias="notifyReason")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
