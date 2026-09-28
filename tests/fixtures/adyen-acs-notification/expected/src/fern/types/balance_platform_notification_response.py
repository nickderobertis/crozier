

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class BalancePlatformNotificationResponse(UniversalBaseModel):
    notification_response: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="notificationResponse"),
        pydantic.Field(
            alias="notificationResponse",
            description="Respond with any **2xx** HTTP status code to [accept the webhook](https://docs.adyen.com/development-resources/webhooks/#accept-webhooks).",
        ),
    ] = None
    """
    Respond with any **2xx** HTTP status code to [accept the webhook](https://docs.adyen.com/development-resources/webhooks/#accept-webhooks).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
