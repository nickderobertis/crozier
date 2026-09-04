

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .dynamic_offer_contract_type import DynamicOfferContractType
from .dynamic_offer_repayment import DynamicOfferRepayment
from .financing_type import FinancingType


class DynamicOffer(UniversalBaseModel):
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

    contract_type: typing_extensions.Annotated[
        DynamicOfferContractType,
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

    financing_type: typing_extensions.Annotated[
        FinancingType,
        FieldMetadata(alias="financingType"),
        pydantic.Field(
            alias="financingType",
            description="The type of financing that the offer is for.\n\nPossible values: **businessFinancing**.",
        ),
    ]
    """
    The type of financing that the offer is for.
    
    Possible values: **businessFinancing**.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the dynamic offer.
    """

    maximum_amount: typing_extensions.Annotated[
        Amount,
        FieldMetadata(alias="maximumAmount"),
        pydantic.Field(
            alias="maximumAmount",
            description="The maximum financing amount available to the account holder under this offer.",
        ),
    ]
    """
    The maximum financing amount available to the account holder under this offer.
    """

    minimum_amount: typing_extensions.Annotated[
        Amount,
        FieldMetadata(alias="minimumAmount"),
        pydantic.Field(
            alias="minimumAmount",
            description="The minimum financing amount available to the account holder under this offer.",
        ),
    ]
    """
    The minimum financing amount available to the account holder under this offer.
    """

    repayment: DynamicOfferRepayment = pydantic.Field()
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
