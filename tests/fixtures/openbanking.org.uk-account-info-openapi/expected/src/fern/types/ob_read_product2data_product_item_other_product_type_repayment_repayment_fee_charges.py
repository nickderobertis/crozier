

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_cap_item import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem,
)
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges_repayment_fee_charge_detail_item import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetailItem,
)


class ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges(UniversalBaseModel):
    """
    Applicable fee/charges for repayment such as prepayment, full early repayment or non repayment.
    """

    repayment_fee_charge_cap: typing_extensions.Annotated[
        typing.Optional[
            typing.List[
                ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeCapItem
            ]
        ],
        FieldMetadata(alias="RepaymentFeeChargeCap"),
    ] = None
    repayment_fee_charge_detail: typing_extensions.Annotated[
        typing.List[
            ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeChargesRepaymentFeeChargeDetailItem
        ],
        FieldMetadata(alias="RepaymentFeeChargeDetail"),
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
