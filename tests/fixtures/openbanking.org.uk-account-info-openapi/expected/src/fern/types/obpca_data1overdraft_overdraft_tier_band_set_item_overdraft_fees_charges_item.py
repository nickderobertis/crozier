

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem,
)


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItem(UniversalBaseModel):
    """
    Overdraft fees and charges details
    """

    overdraft_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem]
        ],
        FieldMetadata(alias="OverdraftFeeChargeCap"),
        pydantic.Field(
            alias="OverdraftFeeChargeCap",
            description="Details about any caps (maximum charges) that apply to a particular fee/charge",
        ),
    ] = None
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge
    """

    overdraft_fee_charge_detail: typing_extensions.Annotated[
        typing.List[ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem],
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
