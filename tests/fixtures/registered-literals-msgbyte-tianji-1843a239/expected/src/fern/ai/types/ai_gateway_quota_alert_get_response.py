

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class AiGatewayQuotaAlertGetResponse(UniversalBaseModel):
    id: str
    daily_quota: typing_extensions.Annotated[
        float, FieldMetadata(alias="dailyQuota"), pydantic.Field(alias="dailyQuota")
    ]
    enabled: bool
    notification_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="notificationId"), pydantic.Field(alias="notificationId")
    ] = None
    last_alert_sent_at: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="lastAlertSentAt"), pydantic.Field(alias="lastAlertSentAt")
    ] = None
    alert_level80sent: typing_extensions.Annotated[
        bool, FieldMetadata(alias="alertLevel80Sent"), pydantic.Field(alias="alertLevel80Sent")
    ]
    alert_level100sent: typing_extensions.Annotated[
        bool, FieldMetadata(alias="alertLevel100Sent"), pydantic.Field(alias="alertLevel100Sent")
    ]
    alert_level150sent: typing_extensions.Annotated[
        bool, FieldMetadata(alias="alertLevel150Sent"), pydantic.Field(alias="alertLevel150Sent")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
