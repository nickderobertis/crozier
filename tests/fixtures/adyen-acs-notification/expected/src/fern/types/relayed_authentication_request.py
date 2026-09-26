

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .purchase import Purchase
from .relayed_authentication_request_type import RelayedAuthenticationRequestType


class RelayedAuthenticationRequest(UniversalBaseModel):
    environment: str = pydantic.Field()
    """
    The environment from which the webhook originated.
    Possible values: **test**, **live**.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the challenge.
    """

    payment_instrument_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="paymentInstrumentId"),
        pydantic.Field(
            alias="paymentInstrumentId",
            description="The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_) used for the purchase.",
        ),
    ]
    """
    The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_) used for the purchase.
    """

    purchase: Purchase = pydantic.Field()
    """
    The details of the purchase.
    """

    three_ds_requestor_app_url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="threeDSRequestorAppURL"),
        pydantic.Field(
            alias="threeDSRequestorAppURL",
            description="URL for auto-switching to the threeDS Requestor App. If not present, the threeDS Requestor App doesn't support auto-switching.",
        ),
    ] = None
    """
    URL for auto-switching to the threeDS Requestor App. If not present, the threeDS Requestor App doesn't support auto-switching.
    """

    timestamp: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    When the event was queued.
    """

    type: RelayedAuthenticationRequestType = pydantic.Field()
    """
    Type of notification.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
