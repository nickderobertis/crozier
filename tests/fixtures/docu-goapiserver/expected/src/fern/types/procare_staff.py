

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ProcareStaff(UniversalBaseModel):
    """
    Procare Staff.
    """

    id: str
    school_id: str = pydantic.Field()
    """
    School id.
    """

    name: str
    email: typing.Optional[str] = None
    procare_room_id: typing.Optional[str] = None
    ems_room_id: typing.Optional[str] = None
    siso_teacher_id: typing.Optional[str] = None
    is_signed_up: bool
    display_name: bool
    is_active: bool
    is_invited: bool
    is_admin: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
