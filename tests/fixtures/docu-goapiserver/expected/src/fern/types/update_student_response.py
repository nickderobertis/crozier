

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .student_data import StudentData


class UpdateStudentResponse(UniversalBaseModel):
    """
    Update Student Response.
    """

    company_id: str = pydantic.Field()
    """
    Company id.
    """

    school_id: str = pydantic.Field()
    """
    School id.
    """

    student_id: str = pydantic.Field()
    """
    Student id.
    """

    updated_by_email: str
    updated_by_user_id: str = pydantic.Field()
    """
    Updated by user id.
    """

    student_data: typing.Optional[StudentData] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
