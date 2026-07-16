

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
)
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
)


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem(
    UniversalBaseModel
):
    """
    Overdraft fees and charges details
    """

    overdraft_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem
            ]
        ],
        FieldMetadata(alias="OverdraftFeeChargeCap"),
    ] = None
    overdraft_fee_charge_detail: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem
        ],
        FieldMetadata(alias="OverdraftFeeChargeDetail"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
