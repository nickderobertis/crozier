

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .authentication_info import AuthenticationInfo
from .authentication_notification_data_status import AuthenticationNotificationDataStatus
from .purchase_info import PurchaseInfo


class AuthenticationNotificationData(UniversalBaseModel):
    authentication: AuthenticationInfo = pydantic.Field()
    """
    Contains information about the authentication.
    """

    balance_platform: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="balancePlatform"),
        pydantic.Field(alias="balancePlatform", description="The unique identifier of the balance platform."),
    ] = None
    """
    The unique identifier of the balance platform.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the authentication.
    """

    payment_instrument_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="paymentInstrumentId"),
        pydantic.Field(
            alias="paymentInstrumentId",
            description="The unique identifier of the payment instrument that was used for the authentication.",
        ),
    ]
    """
    The unique identifier of the payment instrument that was used for the authentication.
    """

    purchase: PurchaseInfo = pydantic.Field()
    """
    Contains information about the purchase.
    """

    status: AuthenticationNotificationDataStatus = pydantic.Field()
    """
    Outcome of the authentication.
    Allowed values:
    * authenticated
    * rejected
    * error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
