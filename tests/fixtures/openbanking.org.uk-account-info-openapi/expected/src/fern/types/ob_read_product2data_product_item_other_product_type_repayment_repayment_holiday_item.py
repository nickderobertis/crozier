

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .ob_read_product2data_product_item_other_product_type_repayment_repayment_holiday_item_max_holiday_period import (
    ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod,
)


class ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItem(UniversalBaseModel):
    """
    Details of capital repayment holiday if any
    """

    max_holiday_length: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="MaxHolidayLength")] = (
        pydantic.Field(default=None)
    )
    """
    The maximum length/duration of a Repayment Holiday
    """

    max_holiday_period: typing_extensions.Annotated[
        typing.Optional[ObReadProduct2DataProductItemOtherProductTypeRepaymentRepaymentHolidayItemMaxHolidayPeriod],
        FieldMetadata(alias="MaxHolidayPeriod"),
    ] = pydantic.Field(default=None)
    """
    The unit of period (days, weeks, months etc.) of the repayment holiday
    """

    notes: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="Notes")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
