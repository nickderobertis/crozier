

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_capping_period import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_fee_type_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_min_max_type import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_other_fee_type_item import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem,
)


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap(
    UniversalBaseModel
):
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge
    """

    capping_period: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapCappingPeriod
        ],
        FieldMetadata(alias="CappingPeriod"),
    ] = pydantic.Field(default=None)
    """
    Period e.g. day, week, month etc. for which the fee/charge is capped
    """

    fee_cap_amount: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="FeeCapAmount")] = (
        pydantic.Field(default=None)
    )
    """
    Cap amount charged for a fee/charge
    """

    fee_cap_occurrence: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="FeeCapOccurrence")] = (
        pydantic.Field(default=None)
    )
    """
    fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount
    """

    fee_type: typing_extensions.Annotated[
        typing.List[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapFeeTypeItem
        ],
        FieldMetadata(alias="FeeType"),
    ] = pydantic.Field()
    """
    Fee/charge type which is being capped
    """

    min_max_type: typing_extensions.Annotated[
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapMinMaxType,
        FieldMetadata(alias="MinMaxType"),
    ] = pydantic.Field()
    """
    Indicates that this is the minimum/ maximum fee/charge that can be applied by the financial institution
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = (
        pydantic.Field(default=None)
    )
    """
    Notes related to Overdraft fee charge cap
    """

    other_fee_type: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapOtherFeeTypeItem
            ]
        ],
        FieldMetadata(alias="OtherFeeType"),
    ] = pydantic.Field(default=None)
    """
    Other fee type code which is not available in the standard code set
    """

    overdraft_control_indicator: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="OverdraftControlIndicator")
    ] = pydantic.Field(default=None)
    """
    Specifies for the overdraft control feature/benefit
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
