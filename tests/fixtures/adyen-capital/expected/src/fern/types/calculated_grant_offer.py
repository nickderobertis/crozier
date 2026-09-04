

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .calculated_grant_offer_contract_type import CalculatedGrantOfferContractType
from .grant_offer_fee import GrantOfferFee
from .repayment import Repayment


class CalculatedGrantOffer(UniversalBaseModel):
    account_holder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountHolderId"),
        pydantic.Field(
            alias="accountHolderId",
            description="The unique identifier of the account holder that the dynamic offer is for.",
        ),
    ]
    """
    The unique identifier of the account holder that the dynamic offer is for.
    """

    amount: Amount = pydantic.Field()
    """
    The financing amount that would be paid out to your user.
    """

    contract_type: typing_extensions.Annotated[
        CalculatedGrantOfferContractType,
        FieldMetadata(alias="contractType"),
        pydantic.Field(
            alias="contractType",
            description="The contract type of the offer.\n\nPossible values:\n* **loan**\n* **cashAdvance**",
        ),
    ]
    """
    The contract type of the offer.
    
    Possible values:
    * **loan**
    * **cashAdvance**
    """

    expires_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="The expiration date and time of the offer validity period."),
    ]
    """
    The expiration date and time of the offer validity period.
    """

    fee: GrantOfferFee = pydantic.Field()
    """
    Contains information about the fee that your user would pay for the grant.
    """

    repayment: Repayment = pydantic.Field()
    """
    Contains information about the repayment configuration of the grant.
    """

    starts_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="startsAt"),
        pydantic.Field(alias="startsAt", description="The starting date and time of the offer validity period."),
    ]
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
