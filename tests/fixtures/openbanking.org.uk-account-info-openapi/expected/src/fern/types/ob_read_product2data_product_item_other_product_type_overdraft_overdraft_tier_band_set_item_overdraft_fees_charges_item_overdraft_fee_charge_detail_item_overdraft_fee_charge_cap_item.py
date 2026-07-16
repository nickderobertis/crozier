

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .number0 import Number0
from .ob_amount10 import ObAmount10
from .ob_min_max_type1code import ObMinMaxType1Code
from .ob_period1code import ObPeriod1Code
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_fee_type_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem,
)
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
)


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem(
    UniversalBaseModel
):
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge. Capping can either be based on an amount (in gbp), an amount (in items) or a rate.
    """

    capping_period: typing_extensions.Annotated[
        typing.Optional[ObPeriod1Code], FieldMetadata(alias="CappingPeriod")
    ] = None
    fee_cap_amount: typing_extensions.Annotated[typing.Optional[ObAmount10], FieldMetadata(alias="FeeCapAmount")] = None
    fee_cap_occurrence: typing_extensions.Annotated[
        typing.Optional[Number0], FieldMetadata(alias="FeeCapOccurrence")
    ] = None
    fee_type: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemFeeTypeItem
        ],
        FieldMetadata(alias="FeeType"),
    ]
    min_max_type: typing_extensions.Annotated[ObMinMaxType1Code, FieldMetadata(alias="MinMaxType")]
    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = None
    other_fee_type: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItemOtherFeeTypeItem
            ]
        ],
        FieldMetadata(alias="OtherFeeType"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
