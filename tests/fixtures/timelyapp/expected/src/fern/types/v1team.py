

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1Team(UniversalBaseModel):
    id: int = pydantic.Field()
    """
    Unique identifier for the team
    """

    name: str = pydantic.Field()
    """
    Name of the team
    """

    color: str = pydantic.Field()
    """
    Team display color (hex code)
    """

    emoji: typing.Optional[str] = pydantic.Field(default=None)
    """
    Team emoji
    """

    external_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    External ID for the team
    """

    user_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of user IDs in the team
    """

    users: typing.Optional[typing.List[typing.Any]] = pydantic.Field(default=None)
    """
    Array of team user objects with details
    """

    project_ids: typing.Optional[typing.List[int]] = pydantic.Field(default=None)
    """
    Array of project IDs associated with the team
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
