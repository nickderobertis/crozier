

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class StudentData(UniversalBaseModel):
    """
    Student Data.
    """

    school_name: str
    student_complete_name: str
    birth_date: typing.Optional[str] = None
    ems_student_status: str
    start_date: typing.Optional[str] = None
    start_date_ems_entry: typing.Optional[str] = None
    procare_start_date: typing.Optional[str] = None
    ems_start_date: typing.Optional[str] = None
    preferred_start_date: typing.Optional[str] = None
    current_room: typing.Optional[str] = None
    current_room_id: typing.Optional[str] = None
    days_in_room: int
    transition_date: typing.Optional[str] = None
    transition_room: typing.Optional[str] = None
    transition_room_id: typing.Optional[str] = None
    transition_room_override: typing.Optional[str] = None
    transition_room_override_id: typing.Optional[str] = None
    transition_date2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transition_date_2"), pydantic.Field(alias="transition_date_2")
    ] = None
    transition_room2: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transition_room_2"), pydantic.Field(alias="transition_room_2")
    ] = None
    transition_room2id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="transition_room_2_id"), pydantic.Field(alias="transition_room_2_id")
    ] = None
    withdrawal_date: typing.Optional[str] = None
    withdrawal_date_ems_entry: typing.Optional[str] = None
    procare_withdrawal_date: typing.Optional[str] = None
    withdrawal_date_estimated: typing.Optional[str] = None
    ems_withdrawal_date: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
