

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage,
)


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(UniversalBaseModel):
    """
    Provides overdraft details for a specific tier or band
    """

    bank_guaranteed_indicator: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="BankGuaranteedIndicator"),
        pydantic.Field(
            alias="BankGuaranteedIndicator",
            description="Indicates that a bank provides the overdraft limit up to TierValueMIn to all customers automatically",
        ),
    ] = None
    """
    Indicates that a bank provides the overdraft limit up to TierValueMIn to all customers automatically
    """

    ear: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="EAR"),
        pydantic.Field(
            alias="EAR",
            description="EAR means Effective Annual Rate and/or Equivalent Annual Rate (frequently\nused interchangeably), being the actual annual interest rate of an Overdraft.",
        ),
    ] = None
    """
    EAR means Effective Annual Rate and/or Equivalent Annual Rate (frequently
    used interchangeably), being the actual annual interest rate of an Overdraft.
    """

    identification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Identification"),
        pydantic.Field(
            alias="Identification", description="Unique and unambiguous identification of a  Tier Band for a overdraft."
        ),
    ] = None
    """
    Unique and unambiguous identification of a  Tier Band for a overdraft.
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Optional additional notes to supplement the Tier/band details"),
    ] = None
    """
    Optional additional notes to supplement the Tier/band details
    """

    overdraft_fees_charges: typing_extensions.Annotated[
        typing.Optional[
            typing.List[ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem]
        ],
        FieldMetadata(alias="OverdraftFeesCharges"),
        pydantic.Field(alias="OverdraftFeesCharges", description="Overdraft fees and charges"),
    ] = None
    """
    Overdraft fees and charges
    """

    overdraft_interest_charging_coverage: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage
        ],
        FieldMetadata(alias="OverdraftInterestChargingCoverage"),
        pydantic.Field(
            alias="OverdraftInterestChargingCoverage", description="Interest charged on whole amount or tiered/banded"
        ),
    ] = None
    """
    Interest charged on whole amount or tiered/banded
    """

    representative_apr: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="RepresentativeAPR"),
        pydantic.Field(
            alias="RepresentativeAPR",
            description="An annual percentage rate (APR) is the annual rate charged for borrowing or earned through an investment. APR is expressed as a percentage that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction but does not take compounding into account.",
        ),
    ] = None
    """
    An annual percentage rate (APR) is the annual rate charged for borrowing or earned through an investment. APR is expressed as a percentage that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction but does not take compounding into account.
    """

    tier_value_max: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TierValueMax"),
        pydantic.Field(alias="TierValueMax", description="Maximum value of Overdraft Tier/Band"),
    ] = None
    """
    Maximum value of Overdraft Tier/Band
    """

    tier_value_min: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="TierValueMin"),
        pydantic.Field(alias="TierValueMin", description="Minimum value of Overdraft Tier/Band"),
    ]
    """
    Minimum value of Overdraft Tier/Band
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
