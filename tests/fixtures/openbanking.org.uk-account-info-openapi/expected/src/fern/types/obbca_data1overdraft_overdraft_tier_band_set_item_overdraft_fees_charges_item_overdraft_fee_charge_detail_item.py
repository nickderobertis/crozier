

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_application_frequency import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_calculation_frequency import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_rate_type import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_fee_type import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_application_frequency import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_calculation_frequency import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_rate_type import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_other_fee_type import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType,
)
from .obbca_data1overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item import (
    ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem,
)


class ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(
    UniversalBaseModel
):
    """
    Details about the fees/charges
    """

    application_frequency: typing_extensions.Annotated[
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemApplicationFrequency,
        FieldMetadata(alias="ApplicationFrequency"),
        pydantic.Field(
            alias="ApplicationFrequency",
            description="Frequency at which the overdraft charge is applied to the account",
        ),
    ]
    """
    Frequency at which the overdraft charge is applied to the account
    """

    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemCalculationFrequency
        ],
        FieldMetadata(alias="CalculationFrequency"),
        pydantic.Field(
            alias="CalculationFrequency",
            description="How often is the overdraft fee/charge calculated for the account.",
        ),
    ] = None
    """
    How often is the overdraft fee/charge calculated for the account.
    """

    fee_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FeeAmount"),
        pydantic.Field(
            alias="FeeAmount",
            description="Amount charged for an overdraft fee/charge (where it is charged in terms of an amount rather than a rate)",
        ),
    ] = None
    """
    Amount charged for an overdraft fee/charge (where it is charged in terms of an amount rather than a rate)
    """

    fee_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FeeRate"),
        pydantic.Field(
            alias="FeeRate",
            description="Rate charged for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)",
        ),
    ] = None
    """
    Rate charged for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    fee_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeRateType
        ],
        FieldMetadata(alias="FeeRateType"),
        pydantic.Field(
            alias="FeeRateType",
            description="Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)",
        ),
    ] = None
    """
    Rate type for overdraft fee/charge (where it is charged in terms of a rate rather than an amount)
    """

    fee_type: typing_extensions.Annotated[
        ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemFeeType,
        FieldMetadata(alias="FeeType"),
        pydantic.Field(alias="FeeType", description="Overdraft fee type"),
    ]
    """
    Overdraft fee type
    """

    incremental_borrowing_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="IncrementalBorrowingAmount"),
        pydantic.Field(
            alias="IncrementalBorrowingAmount",
            description="Every additional tranche of an overdraft balance to which an overdraft fee is applied",
        ),
    ] = None
    """
    Every additional tranche of an overdraft balance to which an overdraft fee is applied
    """

    negotiable_indicator: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="NegotiableIndicator"),
        pydantic.Field(alias="NegotiableIndicator", description="Indicates whether fee and charges are negotiable"),
    ] = None
    """
    Indicates whether fee and charges are negotiable
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(
            alias="Notes", description="Free text for capturing any other info related to Overdraft Fees Charge Details"
        ),
    ] = None
    """
    Free text for capturing any other info related to Overdraft Fees Charge Details
    """

    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherApplicationFrequency
        ],
        FieldMetadata(alias="OtherApplicationFrequency"),
        pydantic.Field(
            alias="OtherApplicationFrequency",
            description="Other application frequencies that are not available in the standard code list",
        ),
    ] = None
    """
    Other application frequencies that are not available in the standard code list
    """

    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherCalculationFrequency
        ],
        FieldMetadata(alias="OtherCalculationFrequency"),
        pydantic.Field(
            alias="OtherCalculationFrequency",
            description="Other calculation frequency which is not available in the standard code set.",
        ),
    ] = None
    """
    Other calculation frequency which is not available in the standard code set.
    """

    other_fee_rate_type: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeRateType
        ],
        FieldMetadata(alias="OtherFeeRateType"),
        pydantic.Field(
            alias="OtherFeeRateType",
            description="Other fee rate type code which is not available in the standard code set",
        ),
    ] = None
    """
    Other fee rate type code which is not available in the standard code set
    """

    other_fee_type: typing_extensions.Annotated[
        typing.Optional[
            ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOtherFeeType
        ],
        FieldMetadata(alias="OtherFeeType"),
        pydantic.Field(
            alias="OtherFeeType", description="Other Fee type which is not available in the standard code set"
        ),
    ] = None
    """
    Other Fee type which is not available in the standard code set
    """

    overdraft_control_indicator: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="OverdraftControlIndicator"),
        pydantic.Field(
            alias="OverdraftControlIndicator",
            description="Indicates if the fee/charge is already covered by an 'Overdraft Control' fee or not.",
        ),
    ] = None
    """
    Indicates if the fee/charge is already covered by an 'Overdraft Control' fee or not.
    """

    overdraft_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObbcaData1OverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem
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

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
