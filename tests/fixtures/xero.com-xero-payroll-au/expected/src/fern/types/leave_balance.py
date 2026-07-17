

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LeaveBalance(UniversalBaseModel):
    leave_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LeaveName"),
        pydantic.Field(alias="LeaveName", description="The name of the leave type"),
    ] = None
    """
    The name of the leave type
    """

    leave_type_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="LeaveTypeID"),
        pydantic.Field(alias="LeaveTypeID", description="Identifier of the leave type (see PayItems)"),
    ] = None
    """
    Identifier of the leave type (see PayItems)
    """

    number_of_units: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="NumberOfUnits"),
        pydantic.Field(alias="NumberOfUnits", description="The balance of the leave available"),
    ] = None
    """
    The balance of the leave available
    """

    type_of_units: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeOfUnits"),
        pydantic.Field(
            alias="TypeOfUnits", description="The type of units as specified by the LeaveType (see PayItems)"
        ),
    ] = None
    """
    The type of units as specified by the LeaveType (see PayItems)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
