

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_capping_period import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemCappingPeriod,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_fee_type_item import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_min_max_type import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemMinMaxType,
)
from .obbca_data1other_fees_charges_item_fee_charge_detail_item_fee_charge_cap_item_other_fee_type_item import (
    ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem,
)


class ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItem(UniversalBaseModel):
    """
    Details about any caps (maximum charges) that apply to a particular or group of fee/charge
    """

    capping_period: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemCappingPeriod],
        FieldMetadata(alias="CappingPeriod"),
        pydantic.Field(
            alias="CappingPeriod", description="Period e.g. day, week, month etc. for which the fee/charge is capped"
        ),
    ] = None
    """
    Period e.g. day, week, month etc. for which the fee/charge is capped
    """

    fee_cap_amount: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="FeeCapAmount"),
        pydantic.Field(
            alias="FeeCapAmount",
            description="Cap amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)",
        ),
    ] = None
    """
    Cap amount charged for a fee/charge (where it is charged in terms of an amount rather than a rate)
    """

    fee_cap_occurrence: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="FeeCapOccurrence"),
        pydantic.Field(
            alias="FeeCapOccurrence",
            description="fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount",
        ),
    ] = None
    """
    fee/charges are captured dependent on the number of occurrences rather than capped at a particular amount
    """

    fee_type: typing_extensions.Annotated[
        typing.List[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemFeeTypeItem],
        FieldMetadata(alias="FeeType"),
        pydantic.Field(alias="FeeType", description="Fee/charge type which is being capped"),
    ]
    """
    Fee/charge type which is being capped
    """

    min_max_type: typing_extensions.Annotated[
        ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemMinMaxType,
        FieldMetadata(alias="MinMaxType"),
        pydantic.Field(alias="MinMaxType", description="Min Max type"),
    ]
    """
    Min Max type
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="Notes"),
        pydantic.Field(alias="Notes", description="Free text for adding  extra details for fee charge cap"),
    ] = None
    """
    Free text for adding  extra details for fee charge cap
    """

    other_fee_type: typing_extensions.Annotated[
        typing.Optional[typing.List[ObbcaData1OtherFeesChargesItemFeeChargeDetailItemFeeChargeCapItemOtherFeeTypeItem]],
        FieldMetadata(alias="OtherFeeType"),
        pydantic.Field(
            alias="OtherFeeType", description="Other fee type code which is not available in the standard code set"
        ),
    ] = None
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
