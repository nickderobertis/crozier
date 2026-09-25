

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1TeamsPatchTeam(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the team
    """

    color: typing.Optional[str] = pydantic.Field(default=None)
    """
    Team display color (hex code)
    """

    emoji: typing.Optional[str] = pydantic.Field(default=None)
    """
    Team emoji
    """

    users: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Array of user objects with user_id, lead, and hide_hours properties
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
