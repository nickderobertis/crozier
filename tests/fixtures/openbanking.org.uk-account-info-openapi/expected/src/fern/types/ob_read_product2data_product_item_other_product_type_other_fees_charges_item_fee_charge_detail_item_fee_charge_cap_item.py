

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .number1 import Number1
from .ob_amount14 import ObAmount14
from .ob_min_max_type1code import ObMinMaxType1Code
from .ob_period1code import ObPeriod1Code
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem,
)
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem,
)


class ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem(
    UniversalBaseModel
):
    """
    Details about any caps (maximum charges) that apply to a particular or group of fee/charge
    """

    capping_period: typing_extensions.Annotated[
        typing.Optional[ObPeriod1Code], FieldMetadata(alias="CappingPeriod"), pydantic.Field(alias="CappingPeriod")
    ] = None
    fee_cap_amount: typing_extensions.Annotated[
        typing.Optional[ObAmount14], FieldMetadata(alias="FeeCapAmount"), pydantic.Field(alias="FeeCapAmount")
    ] = None
    fee_cap_occurrence: typing_extensions.Annotated[
        typing.Optional[Number1], FieldMetadata(alias="FeeCapOccurrence"), pydantic.Field(alias="FeeCapOccurrence")
    ] = None
    fee_type: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem
        ],
        FieldMetadata(alias="FeeType"),
        pydantic.Field(alias="FeeType"),
    ]
    min_max_type: typing_extensions.Annotated[
        ObMinMaxType1Code, FieldMetadata(alias="MinMaxType"), pydantic.Field(alias="MinMaxType")
    ]
    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Notes"), pydantic.Field(alias="Notes")
    ] = None
    other_fee_type: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem
            ]
        ],
        FieldMetadata(alias="OtherFeeType"),
        pydantic.Field(alias="OtherFeeType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
