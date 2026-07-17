

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_interest_fixed_variable_type1code import ObInterestFixedVariableType1Code
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_interest_fees_charges_item import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItem,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_loan_provider_interest_rate_type import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_max_term_period import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMaxTermPeriod,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_min_term_period import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item_other_loan_provider_interest_rate_type import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType,
)


class ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem(
    UniversalBaseModel
):
    """
    Tier Band Details
    """

    fixed_variable_interest_rate_type: typing_extensions.Annotated[
        ObInterestFixedVariableType1Code,
        FieldMetadata(alias="FixedVariableInterestRateType"),
        pydantic.Field(alias="FixedVariableInterestRateType"),
    ]
    identification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Identification"),
        pydantic.Field(
            alias="Identification", description="Unique and unambiguous identification of a  Tier Band for a SME Loan."
        ),
    ] = None
    """
    Unique and unambiguous identification of a  Tier Band for a SME Loan.
    """

    loan_interest_fees_charges: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanInterestFeesChargesItem
            ]
        ],
        FieldMetadata(alias="LoanInterestFeesCharges"),
        pydantic.Field(alias="LoanInterestFeesCharges"),
    ] = None
    loan_provider_interest_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LoanProviderInterestRate"),
        pydantic.Field(alias="LoanProviderInterestRate", description="Loan provider Interest for the SME Loan product"),
    ] = None
    """
    Loan provider Interest for the SME Loan product
    """

    loan_provider_interest_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemLoanProviderInterestRateType
        ],
        FieldMetadata(alias="LoanProviderInterestRateType"),
        pydantic.Field(
            alias="LoanProviderInterestRateType",
            description="Interest rate types, other than APR, which financial institutions may use to describe the annual interest rate payable for the SME Loan.",
        ),
    ] = None
    """
    Interest rate types, other than APR, which financial institutions may use to describe the annual interest rate payable for the SME Loan.
    """

    max_term_period: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMaxTermPeriod
        ],
        FieldMetadata(alias="MaxTermPeriod"),
        pydantic.Field(
            alias="MaxTermPeriod", description="The unit of period (days, weeks, months etc.) of the Maximum Term"
        ),
    ] = None
    """
    The unit of period (days, weeks, months etc.) of the Maximum Term
    """

    min_term_period: typing_extensions.Annotated[
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemMinTermPeriod,
        FieldMetadata(alias="MinTermPeriod"),
        pydantic.Field(
            alias="MinTermPeriod", description="The unit of period (days, weeks, months etc.) of the Minimum Term"
        ),
    ]
    """
    The unit of period (days, weeks, months etc.) of the Minimum Term
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Notes"), pydantic.Field(alias="Notes")
    ] = None
    other_loan_provider_interest_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItemOtherLoanProviderInterestRateType
        ],
        FieldMetadata(alias="OtherLoanProviderInterestRateType"),
        pydantic.Field(
            alias="OtherLoanProviderInterestRateType",
            description="Other loan interest rate types which are not available in the standard code list",
        ),
    ] = None
    """
    Other loan interest rate types which are not available in the standard code list
    """

    rep_apr: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="RepAPR"),
        pydantic.Field(
            alias="RepAPR",
            description="The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made. \nFor SME Loan, this APR is the representative APR which includes any account fees.",
        ),
    ]
    """
    The annual equivalent rate (AER) is interest that is calculated under the assumption that any interest paid is combined with the original balance and the next interest payment will be based on the slightly higher account balance. Overall, this means that interest can be compounded several times in a year depending on the number of times that interest payments are made. 
    For SME Loan, this APR is the representative APR which includes any account fees.
    """

    tier_value_max_term: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="TierValueMaxTerm"),
        pydantic.Field(
            alias="TierValueMaxTerm", description="Maximum loan term for which the loan interest tier applies."
        ),
    ] = None
    """
    Maximum loan term for which the loan interest tier applies.
    """

    tier_value_maximum: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TierValueMaximum"),
        pydantic.Field(
            alias="TierValueMaximum", description="Maximum loan value for which the loan interest tier applies."
        ),
    ] = None
    """
    Maximum loan value for which the loan interest tier applies.
    """

    tier_value_min_term: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="TierValueMinTerm"),
        pydantic.Field(
            alias="TierValueMinTerm", description="Minimum loan term for which the loan interest tier applies."
        ),
    ]
    """
    Minimum loan term for which the loan interest tier applies.
    """

    tier_value_minimum: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="TierValueMinimum"),
        pydantic.Field(
            alias="TierValueMinimum", description="Minimum loan value for which the loan interest tier applies."
        ),
    ]
    """
    Minimum loan value for which the loan interest tier applies.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
