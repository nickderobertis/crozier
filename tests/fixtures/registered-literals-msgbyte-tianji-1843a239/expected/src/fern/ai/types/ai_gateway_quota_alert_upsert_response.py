

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class AiGatewayQuotaAlertUpsertResponse(UniversalBaseModel):
    id: str
    daily_quota: typing_extensions.Annotated[
        float, FieldMetadata(alias="dailyQuota"), pydantic.Field(alias="dailyQuota")
    ]
    enabled: bool
    notification_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="notificationId"), pydantic.Field(alias="notificationId")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
