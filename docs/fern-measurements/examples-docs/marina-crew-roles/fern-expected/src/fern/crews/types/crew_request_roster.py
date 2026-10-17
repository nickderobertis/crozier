

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .crew_request_roster_roles_value import CrewRequestRosterRolesValue


class CrewRequestRoster(UniversalBaseModel):
    roles: typing.Dict[str, CrewRequestRosterRolesValue]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
