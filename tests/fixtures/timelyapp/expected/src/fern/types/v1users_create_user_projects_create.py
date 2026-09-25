

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v1users_create_user_projects_create_create_item import V1UsersCreateUserProjectsCreateCreateItem


class V1UsersCreateUserProjectsCreate(UniversalBaseModel):
    create: typing.Optional[typing.List[V1UsersCreateUserProjectsCreateCreateItem]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
