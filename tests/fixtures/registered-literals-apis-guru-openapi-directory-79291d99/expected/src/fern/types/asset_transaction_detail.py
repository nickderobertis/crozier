

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_transaction_category_type import AssetTransactionCategoryType
from .asset_transaction_type import AssetTransactionType


class AssetTransactionDetail(UniversalBaseModel):
    """
    Documentation not found in the MISMO model viewer and not provided by Freddie Mac.
    """

    asset_transaction_amount: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="AssetTransactionAmount"),
        pydantic.Field(alias="AssetTransactionAmount", description="Asset Transaction Amount."),
    ]
    """
    Asset Transaction Amount.
    """

    asset_transaction_category_type: typing_extensions.Annotated[
        typing.Optional[AssetTransactionCategoryType],
        FieldMetadata(alias="AssetTransactionCategoryType"),
        pydantic.Field(alias="AssetTransactionCategoryType"),
    ] = None
    asset_transaction_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="AssetTransactionDate"),
        pydantic.Field(alias="AssetTransactionDate", description="Asset Transaction Date."),
    ]
    """
    Asset Transaction Date.
    """

    asset_transaction_paid_by_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AssetTransactionPaidByName"),
        pydantic.Field(alias="AssetTransactionPaidByName", description="Populate with who did the transaction."),
    ] = None
    """
    Populate with who did the transaction.
    """

    asset_transaction_post_date: typing_extensions.Annotated[
        dt.date,
        FieldMetadata(alias="AssetTransactionPostDate"),
        pydantic.Field(alias="AssetTransactionPostDate", description="Asset Transaction Post Date."),
    ]
    """
    Asset Transaction Post Date.
    """

    asset_transaction_type: typing_extensions.Annotated[
        AssetTransactionType, FieldMetadata(alias="AssetTransactionType"), pydantic.Field(alias="AssetTransactionType")
    ]
    asset_transaction_type_additional_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AssetTransactionTypeAdditionalDescription"),
        pydantic.Field(
            alias="AssetTransactionTypeAdditionalDescription",
            description="FI Provided - examples are atm, cash, check, credit, debit, deposit, directDebit, directDeposit, dividend, fee, interest, other, payment, pointOfSale, repeatPayment, serviceCharge, transfer.",
        ),
    ] = None
    """
    FI Provided - examples are atm, cash, check, credit, debit, deposit, directDebit, directDeposit, dividend, fee, interest, other, payment, pointOfSale, repeatPayment, serviceCharge, transfer.
    """

    asset_transaction_unique_identifier: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AssetTransactionUniqueIdentifier"),
        pydantic.Field(alias="AssetTransactionUniqueIdentifier", description="A vendor created unique Identifier."),
    ]
    """
    A vendor created unique Identifier.
    """

    financial_institution_transaction_identifier: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FinancialInstitutionTransactionIdentifier"),
        pydantic.Field(
            alias="FinancialInstitutionTransactionIdentifier", description="FI provided Transaction Identifier."
        ),
    ] = None
    """
    FI provided Transaction Identifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
