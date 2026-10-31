

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .team_minimal_response import TeamMinimalResponse


class UserResponse(UniversalBaseModel):
    id: int
    email: str
    name: str
    launchpad_handle: typing.Optional[str] = None
    teams: typing.List[TeamMinimalResponse]
    is_admin: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
