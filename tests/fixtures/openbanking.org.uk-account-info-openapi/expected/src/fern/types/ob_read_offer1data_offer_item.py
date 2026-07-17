

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_id import AccountId
from .ob_read_offer1data_offer_item_amount import ObReadOffer1DataOfferItemAmount
from .ob_read_offer1data_offer_item_fee import ObReadOffer1DataOfferItemFee
from .ob_read_offer1data_offer_item_offer_type import ObReadOffer1DataOfferItemOfferType


class ObReadOffer1DataOfferItem(UniversalBaseModel):
    account_id: typing_extensions.Annotated[
        AccountId, FieldMetadata(alias="AccountId"), pydantic.Field(alias="AccountId")
    ]
    amount: typing_extensions.Annotated[
        typing.Optional[ObReadOffer1DataOfferItemAmount],
        FieldMetadata(alias="Amount"),
        pydantic.Field(alias="Amount", description="Amount of money associated with the offer type."),
    ] = None
    """
    Amount of money associated with the offer type.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="Further details of the offer."),
    ] = None
    """
    Further details of the offer.
    """

    end_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="EndDateTime"),
        pydantic.Field(
            alias="EndDateTime",
            description="Date and time at which the offer ends.All dates in the JSON payloads are represented in ISO 8601 date-time format. \nAll date-time fields in responses must include the timezone. An example is below:\n2017-04-05T10:43:07+00:00",
        ),
    ] = None
    """
    Date and time at which the offer ends.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    fee: typing_extensions.Annotated[
        typing.Optional[ObReadOffer1DataOfferItemFee],
        FieldMetadata(alias="Fee"),
        pydantic.Field(alias="Fee", description="Fee associated with the offer type."),
    ] = None
    """
    Fee associated with the offer type.
    """

    offer_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OfferId"),
        pydantic.Field(
            alias="OfferId",
            description="A unique and immutable identifier used to identify the offer resource. This identifier has no meaning to the account owner.",
        ),
    ] = None
    """
    A unique and immutable identifier used to identify the offer resource. This identifier has no meaning to the account owner.
    """

    offer_type: typing_extensions.Annotated[
        typing.Optional[ObReadOffer1DataOfferItemOfferType],
        FieldMetadata(alias="OfferType"),
        pydantic.Field(alias="OfferType", description="Offer type, in a coded form."),
    ] = None
    """
    Offer type, in a coded form.
    """

    rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Rate"),
        pydantic.Field(alias="Rate", description="Rate associated with the offer type."),
    ] = None
    """
    Rate associated with the offer type.
    """

    start_date_time: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="StartDateTime"),
        pydantic.Field(
            alias="StartDateTime",
            description="Date and time at which the offer starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. \nAll date-time fields in responses must include the timezone. An example is below:\n2017-04-05T10:43:07+00:00",
        ),
    ] = None
    """
    Date and time at which the offer starts.All dates in the JSON payloads are represented in ISO 8601 date-time format. 
    All date-time fields in responses must include the timezone. An example is below:
    2017-04-05T10:43:07+00:00
    """

    term: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Term"),
        pydantic.Field(alias="Term", description="Further details of the term of the offer."),
    ] = None
    """
    Further details of the term of the offer.
    """

    url: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="URL"),
        pydantic.Field(
            alias="URL", description="URL (Uniform Resource Locator) where documentation on the offer can be found"
        ),
    ] = None
    """
    URL (Uniform Resource Locator) where documentation on the offer can be found
    """

    value: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="Value"),
        pydantic.Field(alias="Value", description="Value associated with the offer type."),
    ] = None
    """
    Value associated with the offer type.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
