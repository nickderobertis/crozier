

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bank_account_identification import BankAccountIdentification
from .funds_collection_type import FundsCollectionType


class FundsCollection(UniversalBaseModel):
    account_identification: typing_extensions.Annotated[
        typing.Optional[BankAccountIdentification],
        FieldMetadata(alias="accountIdentification"),
        pydantic.Field(
            alias="accountIdentification",
            description="Contains the identification information of the account to which you can transfer funds related to repayments.",
        ),
    ] = None
    """
    Contains the identification information of the account to which you can transfer funds related to repayments.
    """

    funds_collection_type: typing_extensions.Annotated[
        typing.Optional[FundsCollectionType],
        FieldMetadata(alias="fundsCollectionType"),
        pydantic.Field(
            alias="fundsCollectionType",
            description="The type of funds collection.\n\nPossible values: **UnscheduledRepayment**, **Revocation**.",
        ),
    ] = None
    """
    The type of funds collection.
    
    Possible values: **UnscheduledRepayment**, **Revocation**.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
