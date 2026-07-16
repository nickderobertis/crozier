

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_amount11 import ObAmount11
from .ob_amount12 import ObAmount12
from .ob_fee_frequency1code0 import ObFeeFrequency1Code0
from .ob_fee_frequency1code1 import ObFeeFrequency1Code1
from .ob_interest_rate_type1code0 import ObInterestRateType1Code0
from .ob_other_code_type11 import ObOtherCodeType11
from .ob_other_code_type12 import ObOtherCodeType12
from .ob_other_code_type13 import ObOtherCodeType13
from .ob_other_code_type14 import ObOtherCodeType14
from .ob_overdraft_fee_type1code import ObOverdraftFeeType1Code
from .ob_rate10 import ObRate10
from .ob_read_product2data_product_item_other_product_type_overdraft_overdraft_tier_band_set_item_overdraft_fees_charges_item_overdraft_fee_charge_detail_item_overdraft_fee_charge_cap_item import (
    ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem,
)


class ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItem(
    UniversalBaseModel
):
    """
    Details about the fees/charges
    """

    application_frequency: typing_extensions.Annotated[
        ObFeeFrequency1Code0, FieldMetadata(alias="ApplicationFrequency")
    ]
    calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObFeeFrequency1Code1], FieldMetadata(alias="CalculationFrequency")
    ] = None
    fee_amount: typing_extensions.Annotated[typing.Optional[ObAmount12], FieldMetadata(alias="FeeAmount")] = None
    fee_rate: typing_extensions.Annotated[typing.Optional[ObRate10], FieldMetadata(alias="FeeRate")] = None
    fee_rate_type: typing_extensions.Annotated[
        typing.Optional[ObInterestRateType1Code0], FieldMetadata(alias="FeeRateType")
    ] = None
    fee_type: typing_extensions.Annotated[ObOverdraftFeeType1Code, FieldMetadata(alias="FeeType")]
    incremental_borrowing_amount: typing_extensions.Annotated[
        typing.Optional[ObAmount11], FieldMetadata(alias="IncrementalBorrowingAmount")
    ] = None
    negotiable_indicator: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="NegotiableIndicator")
    ] = pydantic.Field(default=None)
    """
    Indicates whether fee and charges are negotiable
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = None
    other_application_frequency: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType11], FieldMetadata(alias="OtherApplicationFrequency")
    ] = None
    other_calculation_frequency: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType12], FieldMetadata(alias="OtherCalculationFrequency")
    ] = None
    other_fee_rate_type: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType14], FieldMetadata(alias="OtherFeeRateType")
    ] = None
    other_fee_type: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType13], FieldMetadata(alias="OtherFeeType")
    ] = None
    overdraft_control_indicator: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="OverdraftControlIndicator")
    ] = pydantic.Field(default=None)
    """
    Indicates if the fee/charge is already covered by an 'Overdraft Control' fee or not.
    """

    overdraft_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeOverdraftOverdraftTierBandSetItemOverdraftFeesChargesItemOverdraftFeeChargeDetailItemOverdraftFeeChargeCapItem
            ]
        ],
        FieldMetadata(alias="OverdraftFeeChargeCap"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
