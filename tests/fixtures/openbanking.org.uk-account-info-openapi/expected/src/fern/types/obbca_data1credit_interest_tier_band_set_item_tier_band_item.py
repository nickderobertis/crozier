

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_application_frequency import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_calculation_frequency import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_fixed_variable_interest_rate_type import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_application_frequency import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType,
)
from .obbca_data1credit_interest_tier_band_set_item_tier_band_item_other_calculation_frequency import (
    ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency,
)


class ObbcaData1CreditInterestTierBandSetItemTierBandItem(UniversalBaseModel):
    """
    Tier Band Details
    """

    aer: typing_extensions.Annotated[str, FieldMetadata(alias="AER")] = pydantic.Field()
    """
    The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made. 
    
    Read more: Annual Equivalent Rate (AER) http://www.investopedia.com/terms/a/aer.asp#ixzz4gfR7IO1A
    """

    application_frequency: typing_extensions.Annotated[
        ObbcaData1CreditInterestTierBandSetItemTierBandItemApplicationFrequency,
        FieldMetadata(alias="ApplicationFrequency"),
    ] = pydantic.Field()
    """
    How often is interest applied to the BCA for this tier/band i.e. how often the financial institution pays accumulated interest to the customer's BCA.
    """

    bank_interest_rate: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="BankInterestRate")] = (
        pydantic.Field(default=None)
    )
    """
    Bank Interest for the BCA product
    """

    bank_interest_rate_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemTierBandItemBankInterestRateType],
        FieldMetadata(alias="BankInterestRateType"),
    ] = pydantic.Field(default=None)
    """
    Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the BCA.
    """

    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemTierBandItemCalculationFrequency],
        FieldMetadata(alias="CalculationFrequency"),
    ] = pydantic.Field(default=None)
    """
    How often is credit interest calculated for the account.
    """

    deposit_interest_applied_coverage: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage],
        FieldMetadata(alias="DepositInterestAppliedCoverage"),
    ] = pydantic.Field(default=None)
    """
    Amount on which Interest applied.
    """

    fixed_variable_interest_rate_type: typing_extensions.Annotated[
        ObbcaData1CreditInterestTierBandSetItemTierBandItemFixedVariableInterestRateType,
        FieldMetadata(alias="FixedVariableInterestRateType"),
    ] = pydantic.Field()
    """
    Type of interest rate, Fixed or Variable
    """

    identification: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Identification")] = (
        pydantic.Field(default=None)
    )
    """
    Unique and unambiguous identification of a  Tier Band for a BCA.
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = (
        pydantic.Field(default=None)
    )
    """
    Optional additional notes to supplement the Tier Band details
    """

    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherApplicationFrequency],
        FieldMetadata(alias="OtherApplicationFrequency"),
    ] = pydantic.Field(default=None)
    """
    Other application frequencies that are not available in the standard code list
    """

    other_bank_interest_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherBankInterestType],
        FieldMetadata(alias="OtherBankInterestType"),
    ] = pydantic.Field(default=None)
    """
    Other interest rate types which are not available in the standard code list
    """

    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObbcaData1CreditInterestTierBandSetItemTierBandItemOtherCalculationFrequency],
        FieldMetadata(alias="OtherCalculationFrequency"),
    ] = pydantic.Field(default=None)
    """
    Other calculation frequency which is not available in the standard code set.
    """

    tier_value_maximum: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TierValueMaximum")] = (
        pydantic.Field(default=None)
    )
    """
    Maximum deposit value for which the credit interest tier applies.
    """

    tier_value_minimum: typing_extensions.Annotated[str, FieldMetadata(alias="TierValueMinimum")] = pydantic.Field()
    """
    Minimum deposit value for which the credit interest tier applies.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
