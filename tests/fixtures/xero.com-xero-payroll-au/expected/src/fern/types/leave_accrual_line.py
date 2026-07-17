

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LeaveAccrualLine(UniversalBaseModel):
    auto_calculate: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="AutoCalculate"),
        pydantic.Field(alias="AutoCalculate", description="If you want to auto calculate leave."),
    ] = None
    """
    If you want to auto calculate leave.
    """

    leave_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LeaveTypeID"),
        pydantic.Field(alias="LeaveTypeID", description="Xero identifier for the Leave type."),
    ] = None
    """
    Xero identifier for the Leave type.
    """

    number_of_units: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NumberOfUnits"),
        pydantic.Field(alias="NumberOfUnits", description="Leave Accrual number of units"),
    ] = None
    """
    Leave Accrual number of units
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
