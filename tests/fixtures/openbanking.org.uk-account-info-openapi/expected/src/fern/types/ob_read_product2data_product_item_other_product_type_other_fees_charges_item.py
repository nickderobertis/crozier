

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_cap_item import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem,
)
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_fee_charge_detail_item import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItem,
)
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_other_tariff_type import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType,
)
from .ob_read_product2data_product_item_other_product_type_other_fees_charges_item_tariff_type import (
    ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType,
)


class ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItem(UniversalBaseModel):
    """
    Contains details of fees and charges which are not associated with either Overdraft or features/benefits
    """

    fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeCapItem]],
        FieldMetadata(alias="FeeChargeCap"),
        pydantic.Field(alias="FeeChargeCap"),
    ] = None
    fee_charge_detail: typing_extensions.Annotated[
        typing.List[ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemFeeChargeDetailItem],
        FieldMetadata(alias="FeeChargeDetail"),
        pydantic.Field(alias="FeeChargeDetail"),
    ]
    other_tariff_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemOtherTariffType],
        FieldMetadata(alias="OtherTariffType"),
        pydantic.Field(alias="OtherTariffType", description="Other tariff type which is not in the standard list."),
    ] = None
    """
    Other tariff type which is not in the standard list.
    """

    tariff_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TariffName"),
        pydantic.Field(alias="TariffName", description="Name of the tariff"),
    ] = None
    """
    Name of the tariff
    """

    tariff_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeOtherFeesChargesItemTariffType],
        FieldMetadata(alias="TariffType"),
        pydantic.Field(alias="TariffType", description="TariffType which defines the fee and charges."),
    ] = None
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
