

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_other_code_type10 import ObOtherCodeType10
from .ob_read_product2data_product_item_other_product_type_product_details_fee_free_length_period import (
    ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod,
)
from .ob_read_product2data_product_item_other_product_type_product_details_segment_item import (
    ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem,
)


class ObReadProduct2DataProductItemOtherProductTypeProductDetails(UniversalBaseModel):
    fee_free_length: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="FeeFreeLength"),
        pydantic.Field(alias="FeeFreeLength", description="The length/duration of the fee free period"),
    ] = None
    """
    The length/duration of the fee free period
    """

    fee_free_length_period: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeProductDetailsFeeFreeLengthPeriod],
        FieldMetadata(alias="FeeFreeLengthPeriod"),
        pydantic.Field(
            alias="FeeFreeLengthPeriod",
            description="The unit of period (days, weeks, months etc.) of the promotional length",
        ),
    ] = None
    """
    The unit of period (days, weeks, months etc.) of the promotional length
    """

    monthly_maximum_charge: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="MonthlyMaximumCharge"),
        pydantic.Field(
            alias="MonthlyMaximumCharge",
            description="The maximum relevant charges that could accrue as defined fully in Part 7 of the CMA order",
        ),
    ] = None
    """
    The maximum relevant charges that could accrue as defined fully in Part 7 of the CMA order
    """

    notes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="Notes"), pydantic.Field(alias="Notes")
    ] = None
    other_segment: typing_extensions.Annotated[
        typing.Optional[ObOtherCodeType10], FieldMetadata(alias="OtherSegment"), pydantic.Field(alias="OtherSegment")
    ] = None
    segment: typing_extensions.Annotated[
        typing.Optional[typing.List[ObReadProduct2DataProductItemOtherProductTypeProductDetailsSegmentItem]],
        FieldMetadata(alias="Segment"),
        pydantic.Field(alias="Segment"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
