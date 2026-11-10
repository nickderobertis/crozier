

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .asset_type import AssetType


class CreditFreddieMacAssetDetailVoe25(UniversalBaseModel):
    """
    Details about an asset.
    """

    asset_account_identifier: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AssetAccountIdentifier"),
        pydantic.Field(
            alias="AssetAccountIdentifier", description="A unique alphanumeric string identifying an asset."
        ),
    ]
    """
    A unique alphanumeric string identifying an asset.
    """

    asset_as_of_date: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AssetAsOfDate"),
        pydantic.Field(alias="AssetAsOfDate", description="Account Report As of Date / Create Date. Format YYYY-MM-DD"),
    ]
    """
    Account Report As of Date / Create Date. Format YYYY-MM-DD
    """

    asset_days_requested_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="AssetDaysRequestedCount"),
        pydantic.Field(
            alias="AssetDaysRequestedCount",
            description="The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days.",
        ),
    ]
    """
    The Number of days requested made to the Financial Institution. Example When looking for 3 months of data from the FI, pass in 90 days.
    """

    asset_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AssetDescription"),
        pydantic.Field(
            alias="AssetDescription",
            description="A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset.",
        ),
    ] = None
    """
    A text description that further defines the Asset. This could be used to describe the shares associated with the stocks, bonds or mutual funds, retirement funds or business owned that the borrower has disclosed (named) as an asset.
    """

    asset_ownership_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AssetOwnershipType"),
        pydantic.Field(alias="AssetOwnershipType", description="Ownership type of the asset account."),
    ] = None
    """
    Ownership type of the asset account.
    """

    asset_type: typing_extensions.Annotated[
        AssetType, FieldMetadata(alias="AssetType"), pydantic.Field(alias="AssetType")
    ]
    asset_type_additional_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="AssetTypeAdditionalDescription"),
        pydantic.Field(
            alias="AssetTypeAdditionalDescription",
            description="Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit.",
        ),
    ] = None
    """
    Additional Asset Decription some examples are Investment Tax-Deferred , Loan, 401K, 403B, Checking, Money Market, Credit Card,ROTH,529,Biller,ROLLOVER,CD,Savings,Investment Taxable, IRA, Mortgage, Line Of Credit.
    """

    asset_unique_identifier: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="AssetUniqueIdentifier"),
        pydantic.Field(alias="AssetUniqueIdentifier", description="A vendor created unique Identifier."),
    ]
    """
    A vendor created unique Identifier.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
