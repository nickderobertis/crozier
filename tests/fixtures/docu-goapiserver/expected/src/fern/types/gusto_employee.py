

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GustoEmployee(UniversalBaseModel):
    """
    Gusto Employee.
    """

    gusto_company_id: str
    current_employment_status: typing.Optional[str] = None
    dataddo_extraction_timestamp: str
    date_of_birth: str
    department: str
    email: typing.Optional[str] = None
    first_name: typing.Optional[str] = None
    jobs_id: str = pydantic.Field()
    """
    Jobs id.
    """

    last_name: typing.Optional[str] = None
    manager_id: str = pydantic.Field()
    """
    Manager id.
    """

    maximum_accrual_balance: int
    middle_initial: str
    onboarded: int
    terminated: int
    terminations_effective_date: str
    id: str
    title: str
    hire_date: str
    school_name: str
    rate: typing.Optional[float] = None
    monday_item_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="MondayItemId"), pydantic.Field(alias="MondayItemId")
    ]
    monday_assigned_room_id: typing.Optional[str] = None
    monday_assigned_room_name: typing.Optional[str] = None
    school_id: typing.Optional[str] = None
    monday_daily_hours: typing.Optional[str] = None
    monday_day_off: typing.Optional[str] = None
    monday_start_time: typing.Optional[str] = None
    monday_break_time: typing.Optional[str] = None
    monday_break_minutes: typing.Optional[str] = None
    custom_potential_final_date: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
