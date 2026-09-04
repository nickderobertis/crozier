

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .grant_offer_contract_type import GrantOfferContractType
from .grant_offer_fee import GrantOfferFee
from .repayment import Repayment


class GrantOffer(UniversalBaseModel):
    account_holder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountHolderId"),
        pydantic.Field(
            alias="accountHolderId",
            description="The unique identifier of the account holder to which the grant is offered.",
        ),
    ]
    """
    The unique identifier of the account holder to which the grant is offered.
    """

    amount: typing.Optional[Amount] = pydantic.Field(default=None)
    """
    The amount that would be paid out to the user for business financing.
    """

    contract_type: typing_extensions.Annotated[
        typing.Optional[GrantOfferContractType],
        FieldMetadata(alias="contractType"),
        pydantic.Field(
            alias="contractType",
            description="The contract type of the offer.\n\nPossible values:\n* **loan**\n* **cashAdvance**",
        ),
    ] = None
    """
    The contract type of the offer.
    
    Possible values:
    * **loan**
    * **cashAdvance**
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="The expiration date and time of the offer validity period."),
    ] = None
    """
    The expiration date and time of the offer validity period.
    """

    fee: typing.Optional[GrantOfferFee] = pydantic.Field(default=None)
    """
    Contains information about the fee that your user would pay for the grant.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the offer.
    """

    repayment: typing.Optional[Repayment] = pydantic.Field(default=None)
    """
    Contains information about the repayment configuration of the grant.
    """

    starts_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="startsAt"),
        pydantic.Field(alias="startsAt", description="The starting date and time of the offer validity period."),
    ] = None
    """
    The starting date and time of the offer validity period.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
