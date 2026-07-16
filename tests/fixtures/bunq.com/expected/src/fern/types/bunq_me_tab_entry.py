

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .bunq_me_merchant_available import BunqMeMerchantAvailable
from .label_monetary_account import LabelMonetaryAccount


class BunqMeTabEntry(UniversalBaseModel):
    alias: typing.Optional[LabelMonetaryAccount] = pydantic.Field(default=None)
    """
    The LabelMonetaryAccount with the public information of the User and the MonetaryAccount that created the bunq.me link.
    """

    amount_inquired: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The requested Amount.
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    The description for the bunq.me. Maximum 9000 characters.
    """

    invite_profile_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Provided if the user has enabled their invite link.
    """

    merchant_available: typing.Optional[typing.List[BunqMeMerchantAvailable]] = pydantic.Field(default=None)
    """
    List of available merchants.
    """

    redirect_url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL which the user is sent to when a payment is completed.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the bunq.me. Can be WAITING_FOR_PAYMENT, CANCELLED or EXPIRED.
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="uuid"),
        pydantic.Field(alias="uuid", description="The uuid of the bunq.me."),
    ] = None
    """
    The uuid of the bunq.me.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
