

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_application_frequency import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_calculation_frequency import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemCalculationFrequency,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_applicable_range import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_category import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_rate_type import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_type import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeType,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_application_frequency import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_calculation_frequency import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_category_type import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_rate_type import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_other_fee_type import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType,
)


class ObbcaData1OtherFeesChargesItemFeeChargeDetailItem(UniversalBaseModel):
    """
    Other fees/charges details
    """

    application_frequency: typing_extensions.Annotated[
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemApplicationFrequency,
        FieldMetadata(alias="ApplicationFrequency"),
        pydantic.Field(
            alias="ApplicationFrequency", description="How frequently the fee/charge is applied to the account"
        ),
    ]
    """
    How frequently the fee/charge is applied to the account
    """

    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemCalculationFrequency],
        FieldMetadata(alias="CalculationFrequency"),
        pydantic.Field(alias="CalculationFrequency", description="How frequently the fee/charge is calculated"),
    ] = None
    """
    How frequently the fee/charge is calculated
    """

    fee_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FeeAmount"),
        pydantic.Field(
            alias="FeeAmount",
            description="Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)",
        ),
    ] = None
    """
    Fee Amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    """

    fee_applicable_range: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeApplicableRange],
        FieldMetadata(alias="FeeApplicableRange"),
        pydantic.Field(
            alias="FeeApplicableRange", description="Range or amounts or rates for which the fee/charge applies"
        ),
    ] = None
    """
    Range or amounts or rates for which the fee/charge applies
    """

    fee_category: typing_extensions.Annotated[
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeCategory,
        FieldMetadata(alias="FeeCategory"),
        pydantic.Field(alias="FeeCategory", description="Categorisation of fees and charges into standard categories."),
    ]
    """
    Categorisation of fees and charges into standard categories.
    """

    fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[typing.List[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem]],
        FieldMetadata(alias="FeeChargeCap"),
        pydantic.Field(
            alias="FeeChargeCap",
            description="Details about any caps (maximum charges) that apply to a particular or group of fee/charge",
        ),
    ] = None
    """
    Details about any caps (maximum charges) that apply to a particular or group of fee/charge
    """

    fee_rate: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FeeRate"),
        pydantic.Field(
            alias="FeeRate",
            description="Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)",
        ),
    ] = None
    """
    Rate charged for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    """

    fee_rate_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeRateType],
        FieldMetadata(alias="FeeRateType"),
        pydantic.Field(
            alias="FeeRateType",
            description="Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)",
        ),
    ] = None
    """
    Rate type for Fee/Charge (where it is charged in terms of a rate rather than an amount)
    """

    fee_type: typing_extensions.Annotated[
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeType,
        FieldMetadata(alias="FeeType"),
        pydantic.Field(alias="FeeType", description="Fee/Charge Type"),
    ]
    """
    Fee/Charge Type
    """

    negotiable_indicator: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="NegotiableIndicator"),
        pydantic.Field(
            alias="NegotiableIndicator", description="Fee/charge which is usually negotiable rather than a fixed amount"
        ),
    ] = None
    """
    Fee/charge which is usually negotiable rather than a fixed amount
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Optional additional notes to supplement the fee/charge details."),
    ] = None
    """
    Optional additional notes to supplement the fee/charge details.
    """

    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherApplicationFrequency],
        FieldMetadata(alias="OtherApplicationFrequency"),
        pydantic.Field(
            alias="OtherApplicationFrequency",
            description="Other application frequencies not covered in the standard code list",
        ),
    ] = None
    """
    Other application frequencies not covered in the standard code list
    """

    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherCalculationFrequency],
        FieldMetadata(alias="OtherCalculationFrequency"),
        pydantic.Field(
            alias="OtherCalculationFrequency",
            description="Other calculation frequency which is not available in standard code set.",
        ),
    ] = None
    """
    Other calculation frequency which is not available in standard code set.
    """

    other_fee_category_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeCategoryType],
        FieldMetadata(alias="OtherFeeCategoryType"),
        pydantic.Field(alias="OtherFeeCategoryType"),
    ] = None
    other_fee_rate_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeRateType],
        FieldMetadata(alias="OtherFeeRateType"),
        pydantic.Field(
            alias="OtherFeeRateType", description="Other fee rate type which is not available in the standard code set"
        ),
    ] = None
    """
    Other fee rate type which is not available in the standard code set
    """

    other_fee_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemOtherFeeType],
        FieldMetadata(alias="OtherFeeType"),
        pydantic.Field(
            alias="OtherFeeType", description="Other Fee/charge type which is not available in the standard code set"
        ),
    ] = None
    """
    Other Fee/charge type which is not available in the standard code set
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
