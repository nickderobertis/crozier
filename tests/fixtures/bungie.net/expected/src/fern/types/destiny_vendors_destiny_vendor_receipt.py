

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .destiny_destiny_item_quantity import DestinyDestinyItemQuantity


class DestinyVendorsDestinyVendorReceipt(UniversalBaseModel):
    """
    If a character purchased an item that is refundable, a Vendor Receipt will be created on the user's Destiny Profile. These expire after a configurable period of time, but until then can be used to get refunds on items. BNet does not provide the ability to refund a purchase *yet*, but you know.
    """

    currency_paid: typing_extensions.Annotated[
        typing.Optional[typing.List[DestinyDestinyItemQuantity]], FieldMetadata(alias="currencyPaid")
    ] = pydantic.Field(default=None)
    """
    The amount paid for the item, in terms of items that were consumed in the purchase and their quantity.
    """

    expires_on: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="expiresOn")] = (
        pydantic.Field(default=None)
    )
    """
    The date at which this receipt is rendered invalid.
    """

    item_received: typing_extensions.Annotated[
        typing.Optional[DestinyDestinyItemQuantity], FieldMetadata(alias="itemReceived")
    ] = pydantic.Field(default=None)
    """
    The item that was received, and its quantity.
    """

    license_unlock_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="licenseUnlockHash")] = (
        pydantic.Field(default=None)
    )
    """
    The unlock flag used to determine whether you still have the purchased item.
    """

    purchased_by_character_id: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="purchasedByCharacterId")
    ] = pydantic.Field(default=None)
    """
    The ID of the character who made the purchase.
    """

    refund_policy: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="refundPolicy")] = (
        pydantic.Field(default=None)
    )
    """
    Whether you can get a refund, and what happens in order for the refund to be received. See the DestinyVendorItemRefundPolicy enum for details.
    """

    sequence_number: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="sequenceNumber")] = (
        pydantic.Field(default=None)
    )
    """
    The identifier of this receipt.
    """

    time_to_expiration: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="timeToExpiration")] = (
        pydantic.Field(default=None)
    )
    """
    The seconds since epoch at which this receipt is rendered invalid.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
