

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_repayment_amount_type import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType,
)
from .ob_read_product2data_product_item_other_product_type_repayment_other_amount_type import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType,
)
from .ob_read_product2data_product_item_other_product_type_repayment_other_repayment_frequency import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency,
)
from .ob_read_product2data_product_item_other_product_type_repayment_other_repayment_type import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType,
)
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_fee_charges import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges,
)
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_frequency import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency,
)
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem,
)
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_type import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType,
)


class ObReadProduct2DataProductItemOtherProductTypeRepayment(UniversalBaseModel):
    """
    Repayment details of the Loan product
    """

    amount_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentAmountType],
        FieldMetadata(alias="AmountType"),
        pydantic.Field(
            alias="AmountType",
            description="The repayment is for paying just the interest only or both interest and capital or bullet amount or balance to date etc",
        ),
    ] = None
    """
    The repayment is for paying just the interest only or both interest and capital or bullet amount or balance to date etc
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Notes"), pydantic.Field(alias="Notes")
    ] = None
    other_amount_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherAmountType],
        FieldMetadata(alias="OtherAmountType"),
        pydantic.Field(alias="OtherAmountType", description="Other amount type which is not in the standard code list"),
    ] = None
    """
    Other amount type which is not in the standard code list
    """

    other_repayment_frequency: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentFrequency],
        FieldMetadata(alias="OtherRepaymentFrequency"),
        pydantic.Field(
            alias="OtherRepaymentFrequency",
            description="Other repayment frequency which is not in the standard code list",
        ),
    ] = None
    """
    Other repayment frequency which is not in the standard code list
    """

    other_repayment_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentOtherRepaymentType],
        FieldMetadata(alias="OtherRepaymentType"),
        pydantic.Field(
            alias="OtherRepaymentType", description="Other repayment type which is not in the standard code list"
        ),
    ] = None
    """
    Other repayment type which is not in the standard code list
    """

    repayment_fee_charges: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFeeCharges],
        FieldMetadata(alias="RepaymentFeeCharges"),
        pydantic.Field(
            alias="RepaymentFeeCharges",
            description="Applicable fee/charges for repayment such as prepayment, full early repayment or non repayment.",
        ),
    ] = None
    """
    Applicable fee/charges for repayment such as prepayment, full early repayment or non repayment.
    """

    repayment_frequency: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentFrequency],
        FieldMetadata(alias="RepaymentFrequency"),
        pydantic.Field(alias="RepaymentFrequency", description="Repayment frequency"),
    ] = None
    """
    Repayment frequency
    """

    repayment_holiday: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem]],
        FieldMetadata(alias="RepaymentHoliday"),
        pydantic.Field(alias="RepaymentHoliday"),
    ] = None
    repayment_type: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentType],
        FieldMetadata(alias="RepaymentType"),
        pydantic.Field(alias="RepaymentType", description="Repayment type"),
    ] = None
    """
    Repayment type
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
