

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
)


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItem(UniversalBaseModel):
    """
    Overdraft fees and charges
    """

    overdraft_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem
            ]
        ],
        FieldMetadata(alias="OverdraftFeeChargeCap"),
        pydantic.Field(
            alias="OverdraftFeeChargeCap",
            description="Details about any caps (maximum charges) that apply to a particular fee/charge. Capping can either be based on an amount (in gbp), an amount (in items) or a rate.",
        ),
    ] = None
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge. Capping can either be based on an amount (in gbp), an amount (in items) or a rate.
    """

    overdraft_fee_charge_detail: typing_extensions.Annotated[
        typing.List[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem
        ],
        FieldMetadata(alias="OverdraftFeeChargeDetail"),
        pydantic.Field(alias="OverdraftFeeChargeDetail", description="Details about the fees/charges"),
    ]
    """
    Details about the fees/charges
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
