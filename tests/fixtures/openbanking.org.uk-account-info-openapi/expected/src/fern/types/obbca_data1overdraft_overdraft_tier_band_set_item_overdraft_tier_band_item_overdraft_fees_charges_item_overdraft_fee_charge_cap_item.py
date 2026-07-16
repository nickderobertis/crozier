

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_capping_period import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_fee_type_item import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_min_max_type import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_tier_band_item_overdraft_fees_charges_item_overdraft_fee_charge_cap_item_other_fee_type_item import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem,
)


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItem(
    UniversalBaseModel
):
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge. Capping can either be based on an amount (in gbp), an amount (in items) or a rate.
    """

    capping_period: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemCappingPeriod
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
    Indicates whether the advertised overdraft rate is guaranteed to be offered to a borrower by the bank e.g. if it’s part of a government scheme, or whether the rate may vary dependent on the applicant’s circumstances.
    """

    fee_type: typing_extensions.Annotated[
        typing.List[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemFeeTypeItem
        ],
        FieldMetadata(alias="FeeType"),
    ] = pydantic.Field()
    """
    Fee/charge type which is being capped
    """

    min_max_type: typing_extensions.Annotated[
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemMinMaxType,
        FieldMetadata(alias="MinMaxType"),
    ] = pydantic.Field()
    """
    Min Max type
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
                ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftTierBandItemOverdraftFeesChargesItemOverdraftFeeChargeCapItemOtherFeeTypeItem
            ]
        ],
        FieldMetadata(alias="OtherFeeType"),
    ] = pydantic.Field(default=None)
    """
    Other fee type code which is not available in the standard code set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
