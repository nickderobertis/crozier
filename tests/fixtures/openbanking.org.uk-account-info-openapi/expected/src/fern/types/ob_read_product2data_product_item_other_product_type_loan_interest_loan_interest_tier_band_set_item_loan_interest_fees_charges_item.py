

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_cap_item import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem,
)
from .ob_read_product2data_product_item_other_product_type_loan_interest_loan_interest_tier_band_set_item_loan_interest_fees_charges_item_loan_interest_fee_charge_detail_item import (
    ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem,
)


class ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItem(
    UniversalBaseModel
):
    """
    Contains details of fees and charges which are not associated with either LoanRepayment or features/benefits
    """

    loan_interest_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeCapItem
            ]
        ],
        FieldMetadata(alias="LoanInterestFeeChargeCap"),
        pydantic.Field(alias="LoanInterestFeeChargeCap"),
    ] = None
    loan_interest_fee_charge_detail: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeLoanInterestLoanInterestTierBandSetItemLoanInterestFeesChargesItemLoanInterestFeeChargeDetailItem
        ],
        FieldMetadata(alias="LoanInterestFeeChargeDetail"),
        pydantic.Field(alias="LoanInterestFeeChargeDetail"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
