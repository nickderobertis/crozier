

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_interest_fixed_variable_type1code import ObInterestFixedVariableType1Code
from .ob_other_code_type11 import ObOtherCodeType11
from .ob_other_code_type12 import ObOtherCodeType12
from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_application_frequency import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency,
)
from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_bank_interest_rate_type import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType,
)
from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_calculation_frequency import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemCalculationFrequency,
)
from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_deposit_interest_applied_coverage import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage,
)
from .ob_read_product2data_product_item_other_product_type_credit_interest_tier_band_set_item_tier_band_item_other_bank_interest_type import (
    ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType,
)


class ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItem(UniversalBaseModel):
    """
    Tier Band Details
    """

    aer: typing_extensions.Annotated[str, FieldMetadata(alias="AER")] = pydantic.Field()
    """
    The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made. 
    Read more: Annual Equivalent Rate (AER) http://www.investopedia.com/terms/a/aer.asp#ixzz4gfR7IO1A
    """

    application_frequency: typing_extensions.Annotated[
        ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemApplicationFrequency,
        FieldMetadata(alias="ApplicationFrequency"),
    ] = pydantic.Field()
    """
    How often is interest applied to the Product for this tier/band i.e. how often the financial institution pays accumulated interest to the customer's account.
    """

    bank_interest_rate: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="BankInterestRate")] = (
        pydantic.Field(default=None)
    )
    """
    Bank Interest for the product
    """

    bank_interest_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemBankInterestRateType
        ],
        FieldMetadata(alias="BankInterestRateType"),
    ] = pydantic.Field(default=None)
    """
    Interest rate types, other than AER, which financial institutions may use to describe the annual interest rate payable to the account holder's account.
    """

    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemCalculationFrequency
        ],
        FieldMetadata(alias="CalculationFrequency"),
    ] = pydantic.Field(default=None)
    """
    How often is credit interest calculated for the account.
    """

    deposit_interest_applied_coverage: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemDepositInterestAppliedCoverage
        ],
        FieldMetadata(alias="DepositInterestAppliedCoverage"),
    ] = pydantic.Field(default=None)
    """
    Amount on which Interest applied.
    """

    fixed_variable_interest_rate_type: typing_extensions.Annotated[
        ObInterestFixedVariableType1Code, FieldMetadata(alias="FixedVariableInterestRateType")
    ]
    identification: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Identification")] = (
        pydantic.Field(default=None)
    )
    """
    Unique and unambiguous identification of a  Tier Band for the Product.
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = None
    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType11], FieldMetadata(alias="OtherApplicationFrequency")
    ] = None
    other_bank_interest_type: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeCreditInterestTierBandSetItemTierBandItemOtherBankInterestType
        ],
        FieldMetadata(alias="OtherBankInterestType"),
    ] = pydantic.Field(default=None)
    """
    Other interest rate types which are not available in the standard code list
    """

    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType12], FieldMetadata(alias="OtherCalculationFrequency")
    ] = None
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
