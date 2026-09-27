

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PreRegistrationFalloutStudent(UniversalBaseModel):
    """
    Pre Registration Fallout Student.
    """

    row_number: int
    student_id: str = pydantic.Field()
    """
    Student id.
    """

    student_name: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    school_name: str
    school_short_name: str
    school_color_hex: str
    year: int
    pre_registration_date: str
    withdrawal_date: str
    withdrew_same_year: bool
    is_ytd: bool
    student_status: str
    invoice_description: str
    room: str
    age_at_withdrawal: typing.Optional[float] = None
    start_date: str
    months_attended: typing.Optional[float] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
