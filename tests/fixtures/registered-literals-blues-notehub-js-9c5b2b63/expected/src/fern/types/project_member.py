

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .role import Role


class ProjectMember(UniversalBaseModel):
    email: str = pydantic.Field()
    """
    The email address of the project member.
    This property will only be populated if the viewer is an owner of the project.
    """

    name: str
    role: typing.Optional[Role] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
