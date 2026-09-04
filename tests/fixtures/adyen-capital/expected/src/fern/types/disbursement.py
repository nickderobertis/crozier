

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .amount import Amount
from .balance import Balance
from .disbursement_repayment import DisbursementRepayment
from .fee import Fee
from .funds_collection import FundsCollection


class Disbursement(UniversalBaseModel):
    account_holder_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="accountHolderId"),
        pydantic.Field(
            alias="accountHolderId",
            description="The unique identifier of the account holder that received the disbursement.",
        ),
    ]
    """
    The unique identifier of the account holder that received the disbursement.
    """

    amount: Amount = pydantic.Field()
    """
    Contains information about the amount of the disbursement.
    """

    balance_account_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="balanceAccountId"),
        pydantic.Field(
            alias="balanceAccountId",
            description="The unique identifier of the balance account that received the disbursement.",
        ),
    ]
    """
    The unique identifier of the balance account that received the disbursement.
    """

    balances: Balance = pydantic.Field()
    """
    Contains information about the balances of the disbursement.
    """

    fee: Fee = pydantic.Field()
    """
    Contains information about the fee that your user must pay for the disbursement.
    """

    funds_collections: typing_extensions.Annotated[
        typing.Optional[typing.List[FundsCollection]],
        FieldMetadata(alias="fundsCollections"),
        pydantic.Field(
            alias="fundsCollections",
            description="Contains information about the accounts that Adyen uses to collect funds related to repayments.",
        ),
    ] = None
    """
    Contains information about the accounts that Adyen uses to collect funds related to repayments.
    """

    grant_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="grantId"),
        pydantic.Field(alias="grantId", description="The unique identifier of the grant related to the disbursement."),
    ]
    """
    The unique identifier of the grant related to the disbursement.
    """

    id: str = pydantic.Field()
    """
    The unique identifier of the disbursement.
    """

    repayment: DisbursementRepayment = pydantic.Field()
    """
    Contains information about the basis points configured for repaying the disbursement.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
