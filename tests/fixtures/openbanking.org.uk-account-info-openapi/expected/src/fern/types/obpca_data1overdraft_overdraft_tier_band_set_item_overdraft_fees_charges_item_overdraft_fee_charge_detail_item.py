

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType,
)
from .obpca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap import (
    ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap,
)


class ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(
    UniversalBaseModel
):
    """
    Details about the fees/charges
    """

    application_frequency: typing_extensions.Annotated[
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
        FieldMetadata(alias="ApplicationFrequency"),
    ] = pydantic.Field()
    """
    Frequency at which the overdraft charge is applied to the account
    """

    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency
        ],
        FieldMetadata(alias="CalculationFrequency"),
    ] = pydantic.Field(default=None)
    """
    How often is the overdraft fee/charge calculated for the account.
    """

    fee_amount: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="FeeAmount")] = pydantic.Field(
        default=None
    )
    """
    Amount charged for an overdraft fee/charge (where it is charged in terms of an amount rather than a rate)
    """

    fee_rate: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="FeeRate")] = pydantic.Field(
        default=None
    )
    """
    Rate charged for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    fee_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType
        ],
        FieldMetadata(alias="FeeRateType"),
    ] = pydantic.Field(default=None)
    """
    Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    fee_type: typing_extensions.Annotated[
        ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
        FieldMetadata(alias="FeeType"),
    ] = pydantic.Field()
    """
    Overdraft fee type
    """

    incremental_borrowing_amount: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="IncrementalBorrowingAmount")
    ] = pydantic.Field(default=None)
    """
    Every additional tranche of an overdraft balance to which an overdraft fee is applied
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = (
        pydantic.Field(default=None)
    )
    """
    Free text for capturing any other info related to Overdraft Fees Charge Details
    """

    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
        ],
        FieldMetadata(alias="OtherApplicationFrequency"),
    ] = pydantic.Field(default=None)
    """
    Other application frequencies that are not available in the standard code list
    """

    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
        ],
        FieldMetadata(alias="OtherCalculationFrequency"),
    ] = pydantic.Field(default=None)
    """
    Other calculation frequency which is not available in the standard code set.
    """

    other_fee_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
        ],
        FieldMetadata(alias="OtherFeeRateType"),
    ] = pydantic.Field(default=None)
    """
    Other fee rate type code which is not available in the standard code set
    """

    other_fee_type: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
        ],
        FieldMetadata(alias="OtherFeeType"),
    ] = pydantic.Field(default=None)
    """
    Other Fee type which is not available in the standard code set
    """

    overdraft_control_indicator: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="OverdraftControlIndicator")
    ] = pydantic.Field(default=None)
    """
    Specifies for the overdraft control feature/benefit
    """

    overdraft_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            ObpcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCap
        ],
        FieldMetadata(alias="OverdraftFeeChargeCap"),
    ] = pydantic.Field(default=None)
    """
    Details about any caps (maximum charges) that apply to a particular fee/charge
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
