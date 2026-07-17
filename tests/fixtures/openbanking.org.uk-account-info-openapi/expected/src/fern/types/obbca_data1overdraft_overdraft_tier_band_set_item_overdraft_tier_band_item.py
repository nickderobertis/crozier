

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_agreement_period import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_interest_charging_coverage import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage,
)


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItem(UniversalBaseModel):
    """
    Provides overdraft details for a specific tier or band
    """

    agreement_length_max: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="AgreementLengthMax"),
        pydantic.Field(
            alias="AgreementLengthMax",
            description="Specifies the maximum length of a band for a fixed overdraft agreement",
        ),
    ] = None
    """
    Specifies the maximum length of a band for a fixed overdraft agreement
    """

    agreement_length_min: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="AgreementLengthMin"),
        pydantic.Field(
            alias="AgreementLengthMin",
            description="Specifies the minimum length of a band for a fixed overdraft agreement",
        ),
    ] = None
    """
    Specifies the minimum length of a band for a fixed overdraft agreement
    """

    agreement_period: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemAgreementPeriod],
        FieldMetadata(alias="AgreementPeriod"),
        pydantic.Field(
            alias="AgreementPeriod", description="Specifies the period of a fixed length overdraft agreement"
        ),
    ] = None
    """
    Specifies the period of a fixed length overdraft agreement
    """

    bank_guaranteed_indicator: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="BankGuaranteedIndicator"),
        pydantic.Field(
            alias="BankGuaranteedIndicator",
            description="Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it’s part of a government scheme, or whether the rate may vary dependent on the applicant’s circumstances.",
        ),
    ] = None
    """
    Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it’s part of a government scheme, or whether the rate may vary dependent on the applicant’s circumstances.
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
            typing.List[ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem]
        ],
        FieldMetadata(alias="OverdraftFeesCharges"),
        pydantic.Field(alias="OverdraftFeesCharges", description="Overdraft fees and charges"),
    ] = None
    """
    Overdraft fees and charges
    """

    overdraft_interest_charging_coverage: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftInterestChargingCoverage
        ],
        FieldMetadata(alias="OverdraftInterestChargingCoverage"),
        pydantic.Field(
            alias="OverdraftInterestChargingCoverage",
            description="Refers to which interest rate is applied when interests are tiered. For example, if an overdraft balance is £2k and the interest tiers are:- 0-£500 0.1%, 500-1000 0.2%, 1000-10000 0.5%, then the applicable interest rate could either be 0.5% of the entire balance (since the account balance sits in the top interest tier) or (0.1%*500)+(0.2%*500)+(0.5%*1000). In the 1st situation, we say the interest is applied to the ‘Whole’ of the account balance,  and in the 2nd that it is ‘Tiered’.",
        ),
    ] = None
    """
    Refers to which interest rate is applied when interests are tiered. For example, if an overdraft balance is £2k and the interest tiers are:- 0-£500 0.1%, 500-1000 0.2%, 1000-10000 0.5%, then the applicable interest rate could either be 0.5% of the entire balance (since the account balance sits in the top interest tier) or (0.1%*500)+(0.2%*500)+(0.5%*1000). In the 1st situation, we say the interest is applied to the ‘Whole’ of the account balance,  and in the 2nd that it is ‘Tiered’.
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
