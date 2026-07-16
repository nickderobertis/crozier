

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .obbca_data1other_fees_charges_item_fee_charge_cap_item import ObbcaData1OtherFeesChargesItemFeeChargeCapItem
from .obbca_data1other_fees_charges_item_fee_charge_detail_item import ObbcaData1OtherFeesChargesItemFeeChargeDetailItem
from .obbca_data1other_fees_charges_item_other_tariff_type import ObbcaData1OtherFeesChargesItemOtherTariffType
from .obbca_data1other_fees_charges_item_tariff_type import ObbcaData1OtherFeesChargesItemTariffType


class ObbcaData1OtherFeesChargesItem(UniversalBaseModel):
    """
    Contains details of fees and charges which are not associated with either Overdraft or features/benefits
    """

    fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[typing.List[ObbcaData1OtherFeesChargesItemFeeChargeCapItem]],
        FieldMetadata(alias="FeeChargeCap"),
    ] = pydantic.Field(default=None)
    """
    Details about any caps (maximum charges) that apply to a particular or group of fee/charge
    """

    fee_charge_detail: typing_extensions.Annotated[
        typing.List[ObbcaData1OtherFeesChargesItemFeeChargeDetailItem], FieldMetadata(alias="FeeChargeDetail")
    ] = pydantic.Field()
    """
    Other fees/charges details
    """

    other_tariff_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemOtherTariffType], FieldMetadata(alias="OtherTariffType")
    ] = pydantic.Field(default=None)
    """
    Other tariff type which is not in the standard list.
    """

    tariff_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TariffName")] = pydantic.Field(
        default=None
    )
    """
    Name of the tariff
    """

    tariff_type: typing_extensions.Annotated[
        typing.Optional[ObbcaData1OtherFeesChargesItemTariffType], FieldMetadata(alias="TariffType")
    ] = pydantic.Field(default=None)
    """
    TariffType which defines the fee and charges.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
