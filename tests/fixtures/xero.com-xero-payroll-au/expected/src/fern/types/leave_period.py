

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .leave_period_status import LeavePeriodStatus


class LeavePeriod(UniversalBaseModel):
    leave_period_status: typing_extensions.Annotated[
        typing.Optional[LeavePeriodStatus],
        FieldMetadata(alias="LeavePeriodStatus"),
        pydantic.Field(alias="LeavePeriodStatus"),
    ] = None
    number_of_units: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NumberOfUnits"),
        pydantic.Field(alias="NumberOfUnits", description="The Number of Units for the leave"),
    ] = None
    """
    The Number of Units for the leave
    """

    pay_period_end_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayPeriodEndDate"),
        pydantic.Field(alias="PayPeriodEndDate", description="The Pay Period End Date (YYYY-MM-DD)"),
    ] = None
    """
    The Pay Period End Date (YYYY-MM-DD)
    """

    pay_period_start_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PayPeriodStartDate"),
        pydantic.Field(alias="PayPeriodStartDate", description="The Pay Period Start Date (YYYY-MM-DD)"),
    ] = None
    """
    The Pay Period Start Date (YYYY-MM-DD)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
