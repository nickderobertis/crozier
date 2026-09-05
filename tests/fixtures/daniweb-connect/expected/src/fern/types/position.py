

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .app import App
from .position_organization import PositionOrganization
from .position_role import PositionRole
from .user import User


class Position(UniversalBaseModel):
    app: typing.Optional[App] = None
    category: typing.Optional[str] = None
    id: int
    organization: typing.Optional[PositionOrganization] = None
    role: typing.Optional[PositionRole] = None
    user: typing.Optional[User] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
