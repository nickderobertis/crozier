

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_amount13 import ObAmount13
from .ob_fee_category1code import ObFeeCategory1Code
from .ob_fee_frequency1code2 import ObFeeFrequency1Code2
from .ob_fee_frequency1code3 import ObFeeFrequency1Code3
from .ob_fee_type1code import ObFeeType1Code
from .ob_interest_rate_type1code1 import ObInterestRateType1Code1
from .ob_other_code_type10 import ObOtherCodeType10
from .ob_other_code_type16 import ObOtherCodeType16
from .ob_other_code_type17 import ObOtherCodeType17
from .ob_other_code_type18 import ObOtherCodeType18
from .ob_other_fee_charge_detail_type import ObOtherFeeChargeDetailType
from .ob_rate11 import ObRate11
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange,
)
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem,
)


class ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItem(UniversalBaseModel):
    """
    Other fees/charges details
    """

    application_frequency: typing_extensions.Annotated[
        ObFeeFrequency1Code2, FieldMetadata(alias="ApplicationFrequency")
    ]
    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObFeeFrequency1Code3], FieldMetadata(alias="CalculationFrequency")
    ] = None
    fee_amount: typing_extensions.Annotated[typing.Optional[ObAmount13], FieldMetadata(alias="FeeAmount")] = None
    fee_applicable_range: typing_extensions.Annotated[
        typing.Optional[
            ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange
        ],
        FieldMetadata(alias="FeeApplicableRange"),
    ] = pydantic.Field(default=None)
    """
    Range or amounts or rates for which the fee/charge applies
    """

    fee_category: typing_extensions.Annotated[ObFeeCategory1Code, FieldMetadata(alias="FeeCategory")]
    fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem
            ]
        ],
        FieldMetadata(alias="FeeChargeCap"),
    ] = None
    fee_rate: typing_extensions.Annotated[typing.Optional[ObRate11], FieldMetadata(alias="FeeRate")] = None
    fee_rate_type: typing_extensions.Annotated[
        typing.Optional[ObInterestRateType1Code1], FieldMetadata(alias="FeeRateType")
    ] = None
    fee_type: typing_extensions.Annotated[ObFeeType1Code, FieldMetadata(alias="FeeType")]
    negotiable_indicator: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="NegotiableIndicator")
    ] = pydantic.Field(default=None)
    """
    Fee/charge which is usually negotiable rather than a fixed amount
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = None
    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType16], FieldMetadata(alias="OtherApplicationFrequency")
    ] = None
    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType17], FieldMetadata(alias="OtherCalculationFrequency")
    ] = None
    other_fee_category_type: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType10], FieldMetadata(alias="OtherFeeCategoryType")
    ] = None
    other_fee_rate_type: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType18], FieldMetadata(alias="OtherFeeRateType")
    ] = None
    other_fee_type: typing_extensions.Annotated[
        typing.Optional[ObOtherFeeChargeDetailType], FieldMetadata(alias="OtherFeeType")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
