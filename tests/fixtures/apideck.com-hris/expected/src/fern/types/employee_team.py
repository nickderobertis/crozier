

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class EmployeeTeam(UniversalBaseModel):
    """
    The team the person is currently in.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique identifier of the team.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the team.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
