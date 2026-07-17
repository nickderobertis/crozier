

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_interest_calculation_method1code import ObInterestCalculationMethod1Code
from .ob_other_code_type10 import ObOtherCodeType10
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItem,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_tier_band_item import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_tier_band_method import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod,
)


class ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItem(UniversalBaseModel):
    """
    The group of tiers or bands for which debit interest can be applied.
    """

    calculation_method: typing_extensions.Annotated[
        ObInterestCalculationMethod1Code,
        FieldMetadata(alias="CalculationMethod"),
        pydantic.Field(alias="CalculationMethod"),
    ]
    identification: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Identification"),
        pydantic.Field(
            alias="Identification",
            description="Loan interest tierbandset identification. Used by  loan providers for internal use purpose.",
        ),
    ] = None
    """
    Loan interest tierbandset identification. Used by  loan providers for internal use purpose.
    """

    loan_interest_fees_charges: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItem
            ]
        ],
        FieldMetadata(alias="LoanInterestFeesCharges"),
        pydantic.Field(alias="LoanInterestFeesCharges"),
    ] = None
    loan_interest_tier_band: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestTierBandItem
        ],
        FieldMetadata(alias="LoanInterestTierBand"),
        pydantic.Field(alias="LoanInterestTierBand"),
    ]
    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Notes"), pydantic.Field(alias="Notes")
    ] = None
    other_calculation_method: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType10],
        FieldMetadata(alias="OtherCalculationMethod"),
        pydantic.Field(alias="OtherCalculationMethod"),
    ] = None
    tier_band_method: typing_extensions.Annotated[
        ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemTierBandMethod,
        FieldMetadata(alias="TierBandMethod"),
        pydantic.Field(
            alias="TierBandMethod",
            description="The methodology of how credit interest is charged. It can be:-\n1. Banded\nInterest rates are banded. i.e. Increasing rate on whole balance as balance increases.\n2. Tiered\nInterest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.\n3. Whole\nThe same interest rate is applied irrespective of the SME Loan balance",
        ),
    ]
    """
    The methodology of how credit interest is charged. It can be:-
    1. Banded
    Interest rates are banded. i.e. Increasing rate on whole balance as balance increases.
    2. Tiered
    Interest rates are tiered. i.e. increasing rate for each tier as balance increases, but interest paid on tier fixed for that tier and not on whole balance.
    3. Whole
    The same interest rate is applied irrespective of the SME Loan balance
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
